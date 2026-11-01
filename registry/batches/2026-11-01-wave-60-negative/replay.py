"""Reproduce a frozen negative TESS wave partition from public MAST data."""
import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.request


def load_engine(batch, provenance):
    source = provenance["engine_source"]
    engine_sources = {}
    for name, expected in provenance["scientific_scripts"].items():
        url = source["raw_base"] + f"/{source['commit']}/scripts/{name}"
        with urllib.request.urlopen(url, timeout=60) as response:
            data = response.read()
        if sha256(data).hexdigest() != expected:
            raise RuntimeError(f"Pinned scientific engine source hash mismatch: {name}")
        engine_sources[name] = data
    root = Path(tempfile.gettempdir()) / "tess-wave-60-engine"
    scripts = root / "scripts"
    scripts.mkdir(parents=True, exist_ok=True)
    name = "vet_candidate.py"
    path = scripts / name
    path.write_bytes(engine_sources[name])
    sys.path.insert(0, str(scripts))
    spec = importlib.util.spec_from_file_location("vet_candidate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load pinned scientific engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.KNOWN_TICS_GZ = batch / "target-catalog.json.gz"
    cache = os.environ.get("TESS_REPLAY_CACHE")
    module.CACHE_DIR = Path(cache) if cache else root / ".cache" / "mast"
    module.CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return module


def replay_target(args):
    vet, receipts, batch = args
    for path in receipts:
        receipt = json.loads(path.read_text())
        tic = receipt["tic_id"]
        sectors = []
        for product in receipt["sectors_used"]:
            sector = vet.download_and_load_sector(tic, product)
            if sector["sha256"] != product["sha256"]:
                raise RuntimeError(f"Public FITS changed for TIC {tic}, sector {product['sector']}")
            sectors.append(sector)
        result = vet.evaluate_signal_from_arrays(receipt["stellar_parameters"], sectors, **receipt["search_arguments"])
        clean = {key: value for key, value in result.items() if key != "_arrays"}
        if clean != receipt["result"]:
            raise RuntimeError(f"Scientific result differs: {path.name}")
        aliases_path = batch / f"TIC-{tic}-aliases.json"
        if aliases_path.exists() and path == receipts[-1]:
            for alias in json.loads(aliases_path.read_text()):
                period = receipt["result"]["ephemeris"]["period_d"] * alias["multiplier"]
                result = vet.evaluate_signal_from_arrays(
                    receipt["stellar_parameters"], sectors, target_period=period,
                    period_min=max(0.4, period * 0.98), period_max=period * 1.02, allow_known=False,
                )
                clean = {key: value for key, value in result.items() if key != "_arrays"}
                if clean != alias["result"]:
                    raise RuntimeError(f"Alias result differs for TIC {tic}, multiplier {alias['multiplier']}")
    return [path.name for path in receipts]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--partition", type=int, choices=range(8))
    args = parser.parse_args()
    batch = Path(__file__).resolve().parent
    manifest = json.loads((batch / "manifest.json").read_text())
    for name, expected in manifest.items():
        path = (batch / name).resolve()
        if not path.is_relative_to(batch) or sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"Receipt integrity failure: {name}")
    provenance = json.loads((batch / "provenance.json").read_text())
    for name, expected in provenance["scientific_scripts"].items():
        if len(expected) != 64:
            raise RuntimeError(f"Invalid source hash for {name}")
    snapshot = batch / "target-catalog.json.gz"
    if sha256(snapshot.read_bytes()).hexdigest() != provenance["target_catalog_sha256"]:
        raise RuntimeError("Target catalog snapshot hash mismatch")
    vet = load_engine(batch, provenance)
    receipts = sorted(batch.glob("TIC-*-evaluation-*.json"))
    if args.partition is not None:
        allowed = set(provenance["unique_targets_by_partition"][str(args.partition)])
        receipts = [path for path in receipts if str(json.loads(path.read_text())["tic_id"]) in allowed]
    groups = {}
    for path in receipts:
        tic = json.loads(path.read_text())["tic_id"]
        groups.setdefault(tic, []).append(path)
    if not groups:
        raise RuntimeError("No scientific evaluations selected for replay")
    for paths in groups.values():
        for name in replay_target((vet, paths, batch)):
            print(f"Exact public-MAST replay passed: {name}", flush=True)


if __name__ == "__main__":
    main()
