# Negative TESS batch: 60 non-overlapping targets

## Results

The frozen hosted wave completed a 64-target periodic TESS screen. All 64 primary signals were rejected by the unchanged falsification gates. Each target also had four preregistered period aliases tested, and all 256 alias evaluations were rejected. This public contribution contains the 60 targets not already present in an open upstream contribution. Four targets are withheld because upstream PR 11 already records TIC 62468883, 71254978, 101070518, 101448163.

This records the tested targets and false-positive results. It does not establish that the stars have no planets and it makes no discovery claim. No candidate survived this screen.

## Search and falsification scope

The immutable plan searched periods from 1.1 to 15 days, required at least three observed sectors, and retained the unchanged upstream scientific scripts identified by SHA-256 in `provenance.json`. It used the fixed alias multipliers 2, 0.5, 1.5, and 2/3. No signal-dependent target, sector, epoch, threshold, or alias choices were made after inspecting results. Four targets were withheld only because the duplicate registry review found them already covered. Failed or interrupted targets resumed from their exact checkpoint without substitutions.

The sixty primary evaluations fail between two and six gates. Failed primary gate counts: {"gate10_rotational_modulation_guard": 23, "gate2_multi_sector_baseline": 8, "gate3_combined_bls_snr": 37, "gate4_leave_one_epoch_out": 58, "gate5_odd_even_consistency": 16, "gate6_secondary_eclipse_null": 12, "gate7_physical_plausibility": 9, "gate8_centroid_stability": 13, "gate9_per_transit_coherence": 45}. All 240 aliases fail at least one gate. Failed alias gate counts: {"gate10_rotational_modulation_guard": 92, "gate2_multi_sector_baseline": 44, "gate3_combined_bls_snr": 178, "gate4_leave_one_epoch_out": 235, "gate5_odd_even_consistency": 78, "gate6_secondary_eclipse_null": 50, "gate7_physical_plausibility": 37, "gate8_centroid_stability": 33, "gate9_per_transit_coherence": 216}. Full evaluations, public MAST product hashes, alias receipts, and neighbor-query receipts are included. The aliases do not constitute independent detections.

Passing phase-0.5 and centroid checks are conservatively recorded as `UNKNOWN` in `interpretation.json` because a null measurement alone does not rule out an eclipsing-binary or blend explanation. Failed values remain failures. Nonzero TESS quality-flag cadences are excluded by the engine, but this batch does not include a separate momentum-dump timing or pixel-level reduction audit. The multi-sector and per-transit gates test single-sector and localized-artifact explanations. The leave-one-epoch-out calculation reuses the period selected on the full data and is a repeatability check, not a fully blind period search. Neighbor-query receipts are retained but are not independently repeated by the replay script. Transit sensitivity has not been calibrated by injection recovery.

## Catalog and duplicate checks

The scan-time known-object index and its source receipts are recorded in `catalog-check.json`. A hosted catalog refresh was run before submission. The latest upstream main registry and open scan PRs were checked again before preparation. Four overlaps with open upstream PR 11 are excluded from this contribution. The catalog check is limited to the indexed sources and TIC identities. It is not an exhaustive literature or coordinate-based novelty review.

## Reproduction and verification

The public replay uses the pinned public engine commit listed in `provenance.json`. Its scientific script hashes match the versions used for the hosted scan. `replay.py` downloads each recorded MAST product, verifies its SHA-256, and reproduces every primary result and fixed alias exactly. Run one partition with `python -B registry/batches/2026-11-01-wave-60-negative/replay.py --partition 0`. Dependencies are pinned in `replay-requirements.txt`.

The original wave completed with hosted `verify_all.py` checks on all resumed workers. The exact MAST replay runs across the eight frozen partitions in `replay-wave-60.yml`. The upstream repository verification and adversarial tests run in `verify-candidates.yml`. Their hosted results are visible in the pull request checks.

Credit belongs to TESS, MAST, SPOC, QLP, catalog providers, and Open Exoplanet Hunt contributors. Codex assisted with execution and preparation. No human scientific review or independent confirmation is claimed.
