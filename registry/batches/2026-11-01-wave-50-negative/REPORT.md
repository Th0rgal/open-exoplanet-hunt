# Negative TESS batch: 50 nearby cool stars

## Results

The frozen hosted wave completed 50 primary periodic TESS screens and 200 preregistered period-alias evaluations. All 50 primary results and all 200 aliases were rejected by the unchanged falsification gates. No candidate survived. These results apply only to the recorded data and search configuration and do not show that the targets have no planets.

## Search and falsification scope

The metadata-only plan selected 50 unique targets from a fixed 96-probe window using Tmag 11.0 to 11.2, effective temperature 3300 to 4300 K, and distance at most 55 pc. The seven partitions contain six groups of eight and one group of two. The frozen search spans 1.1 to 15 days, requires three to twelve observed sectors, and uses fixed aliases 2, 0.5, 1.5, and 2/3. The scientific engine is pinned by commit and per-script SHA-256 in provenance. No target, sector, epoch, threshold, or alias was changed after inspecting results. Failed targets resumed from the same frozen plan.

All primary rows have verdict REJECTED_BY_FALSIFICATION. Primary failed-gate counts are: gate 2, 3; gate 3, 29; gate 4, 50; gate 5, 14; gate 6, 7; gate 7, 5; gate 8, 7; gate 9, 40; gate 10, 21. Counts overlap because targets can fail multiple gates. All 200 aliases fail at least one gate. Alias failed-gate counts are: gate 2, 30; gate 3, 140; gate 4, 199; gate 5, 73; gate 6, 41; gate 7, 14; gate 8, 26; gate 9, 184; gate 10, 83.

The screen tests multi-sector baseline, combined BLS significance, leave-one-epoch-out repeatability, odd/even consistency, secondary eclipses, physical plausibility, centroid stability, per-transit coherence, and rotational modulation. All 50 primary signals fail leave-one-epoch-out repeatability. Passing null and centroid measurements are conservatively marked UNKNOWN in interpretation.json because they do not independently eliminate eclipsing-binary or background-blend explanations. Failed values remain failures.

## Catalog and duplicate checks

The search-time catalog snapshot and source hashes are recorded in catalog-check.json and refresh-evidence.json. At selection time, the hosted refresh reported no known-object or upstream-registry collision. The later post-scan refresh reports only the expected local_coverage matches for these 50 already recorded private results. Before submission, the current upstream main registry and every open scan PR from 4 through 12 were checked again. No overlap was found. These TIC-based checks do not replace an exhaustive literature or coordinate-based novelty review.

## Reproduction and limitations

Run one frozen partition with `python -B registry/batches/2026-11-01-wave-50-negative/replay.py --partition 0`, replacing 0 with a partition number from 0 through 6. The replay downloads public MAST products, verifies their SHA-256 values, and reproduces each primary and fixed alias result exactly. Dependencies are pinned in replay-requirements.txt. The included workflow runs repository verification, adversarial tests once, and all seven replay partitions on GitHub-hosted runners.

Neighbor-query receipts are included but are not independently re-queried by replay.py. Centroid and secondary-eclipse checks use the pipeline measurements and are not a pixel-level background-blend or eclipsing-binary audit. This batch has no separate momentum-dump timing audit or injection-recovery sensitivity calibration. Only six per-target wall-time samples were available for 50 targets, so they are not representative timing statistics.

Credit belongs to TESS, MAST, SPOC, QLP, catalog providers, and Open Exoplanet Hunt contributors. Codex assisted with execution and preparation. No independent human scientific review or confirmation is claimed.
