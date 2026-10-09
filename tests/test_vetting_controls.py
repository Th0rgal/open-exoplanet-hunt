#!/usr/bin/env python3
"""Adversarial regression tests for the 10-gate exoplanet vetting pipeline.

Following the principle: 'Break your tests on purpose. If a check never fails,
you do not know if it is actually working or just hardcoded to return True.'
"""
import sys
if sys.flags.optimize:
    raise ValueError("Assertions must remain enabled")

from pathlib import Path
import subprocess
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from vet_candidate import evaluate_signal_from_arrays  # noqa: E402


def make_synthetic_sectors(
    period_d: float = 3.1828,
    t0: float = 1468.42,
    dur_d: float = 0.072,
    odd_depth: float = 480e-6,
    even_depth: float = 480e-6,
    sec_depth: float = 0.0,
    drop_last_sector_signal: bool = False,
    centroid_shift_pix: float = 0.0,
    sin_mod_amp: float = 0.0,
    seed: int = 42,
) -> tuple[dict, list[dict]]:
    rng = np.random.default_rng(seed)
    tic_meta = {
        "tic_id": 999999999,
        "ra_deg": 80.0,
        "dec_deg": -1.0,
        "tmag": 9.7,
        "teff_k": 4000.0,
        "rad_rsun": 0.65,
        "mass_msun": 0.63,
        "dist_pc": 35.0,
        "plx_mas": 28.5,
        "contratio": 0.01,
    }
    sector_epochs = [
        (6, 1468.0, 1493.0, 600.0),
        (32, 2174.0, 2199.0, 120.0),
        (98, 3990.0, 4015.0, 200.0),
    ]
    sectors = []
    for idx_s, (sec, t_start, t_end, dt_s) in enumerate(sector_epochs):
        dt_d = dt_s / 86400.0
        t = np.arange(t_start, t_end, dt_d)
        sigma = 220e-6 if dt_s <= 200 else 160e-6
        f = 1.0 + rng.normal(0.0, sigma, size=len(t))
        dx = rng.normal(0.0, 0.002, size=len(t))
        dy = rng.normal(0.0, 0.002, size=len(t))

        epoch_num = np.round((t - t0) / period_d).astype(int)
        ph = (t - t0) - epoch_num * period_d
        in_tr = np.abs(ph) <= 0.5 * dur_d

        if not (drop_last_sector_signal and idx_s == 2):
            odd_m = in_tr & ((epoch_num % 2) == 1)
            even_m = in_tr & ((epoch_num % 2) == 0)
            f[odd_m] -= odd_depth
            f[even_m] -= even_depth
            dx[in_tr] += centroid_shift_pix

        if sec_depth > 0:
            ph_sec = ((t - (t0 + 0.5 * period_d) + 0.5 * period_d) % period_d) - 0.5 * period_d
            f[np.abs(ph_sec) <= 0.5 * dur_d] -= sec_depth

        if sin_mod_amp > 0:
            f += sin_mod_amp * np.sin(2.0 * np.pi * t / period_d)

        sectors.append({
            "sector": sec,
            "pipeline": "SYNTH",
            "exptime_s": dt_s,
            "uri": f"synth://s{sec}",
            "flux_col": "PDCSAP_FLUX",
            "sha256": "0" * 64,
            "n_points": len(t),
            "mad_ppm": sigma * 1e6,
            "t": t,
            "f": f,
            "f_sap": f.copy(),
            "e": np.full(len(t), sigma),
            "dx": dx,
            "dy": dy,
        })
    return tic_meta, sectors


class TestAdversarialVettingGates(unittest.TestCase):
    def test_positive_control_passes_all_10_gates(self) -> None:
        meta, secs = make_synthetic_sectors()
        res = evaluate_signal_from_arrays(meta, secs, target_period=3.1828)
        self.assertTrue(res["all_gates_passed"], f"Expected all 10 gates to pass, got: {res['gates']}")

    def test_negative_control_odd_even_eb_rejected_by_gate5(self) -> None:
        meta, secs = make_synthetic_sectors(odd_depth=950e-6, even_depth=200e-6)
        res = evaluate_signal_from_arrays(meta, secs, target_period=3.1828)
        self.assertFalse(res["gates"]["gate5_odd_even_consistency"]["pass"])
        self.assertFalse(res["all_gates_passed"])

    def test_negative_control_secondary_eclipse_rejected_by_gate6(self) -> None:
        meta, secs = make_synthetic_sectors(odd_depth=600e-6, even_depth=600e-6, sec_depth=300e-6)
        res = evaluate_signal_from_arrays(meta, secs, target_period=3.1828)
        self.assertFalse(res["gates"]["gate6_secondary_eclipse_null"]["pass"])
        self.assertFalse(res["all_gates_passed"])

    def test_negative_control_missing_epoch_rejected_by_gate4_loeo(self) -> None:
        meta, secs = make_synthetic_sectors(drop_last_sector_signal=True)
        res = evaluate_signal_from_arrays(meta, secs, target_period=3.1828)
        self.assertFalse(res["gates"]["gate4_leave_one_epoch_out"]["pass"])
        self.assertFalse(res["all_gates_passed"])

    def test_negative_control_centroid_offset_beb_rejected_by_gate8(self) -> None:
        meta, secs = make_synthetic_sectors(centroid_shift_pix=0.20)
        res = evaluate_signal_from_arrays(meta, secs, target_period=3.1828)
        self.assertFalse(res["gates"]["gate8_centroid_stability"]["pass"])
        self.assertFalse(res["all_gates_passed"])

    def test_negative_control_rotational_modulation_rejected_by_gate10(self) -> None:
        meta, secs = make_synthetic_sectors(odd_depth=450e-6, even_depth=450e-6, sin_mod_amp=400e-6)
        res = evaluate_signal_from_arrays(meta, secs, target_period=3.1828)
        self.assertFalse(res["gates"]["gate10_rotational_modulation_guard"]["pass"])
        self.assertFalse(res["all_gates_passed"])

    def test_optimized_python_rejected_on_all_entrypoints(self) -> None:
        for script in ("sync_catalogs.py", "vet_candidate.py", "hunt_sectors.py", "verify_all.py"):
            proc = subprocess.run(
                [sys.executable, "-O", str(ROOT / "scripts" / script), "--help"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(proc.returncode, 0, f"{script} did not reject -O")
            self.assertIn("Assertions must remain enabled", proc.stderr)


if __name__ == "__main__":
    unittest.main()
