# Negative TESS periodic screen: 63 nearby cool stars

## Results

The frozen hosted wave completed 63 primary TESS screens and 252 preregistered alias evaluations. All 63 primary evaluations and all 252 fixed alias evaluations were rejected by the recorded falsification gates. No unconfirmed candidate survived. This is a negative result for the recorded products and search configuration. It does not show that these stars have no planets.

The eight frozen partitions are reproduced from the primary receipts in this directory. Each target has a final evaluation receipt, four fixed-alias results, and a neighbor-query receipt. `manifest.json` checks every packaged file. The compact target catalog preserves the exact search-time catalog entries for these target TICs.

## Frozen search and provenance

- Frozen parent plan SHA-256: `b85295878c971dbab84bdb913990e7e458bbfabeefd7dfa2f99739ad32bf6a3c`
- Scientific engine commit used by the hosted screen: `b0fbd108375bdcb479689f5477e4d42f9fbdaa11`
- Period range: 1.1 to 15 days
- Product policy: at least three sectors, a six-sector screen, and conditional expansion up to twelve sectors
- Fixed alias multipliers: 2, 0.5, 1.5, and 2/3
- Frozen target set: 63 targets in eight disjoint partitions
- Criteria: unchanged frozen scientific scripts identified by SHA-256 in `provenance.json`

The search-time catalog refresh contains all 63 targets with no known-object collisions. Before submission, the current upstream registry, current upstream known-object index, and open scan PRs 4 through 13 were checked again. No TIC overlap was found. `catalog-check.json` records the hashes and target list. This is a TIC-based catalog and registry check, not an exhaustive coordinate-based literature review.

## Falsification summary

Every primary row has verdict `REJECTED_BY_FALSIFICATION`. Primary failed-gate counts are gate 2: 2, gate 3: 39, gate 4: 63, gate 5: 14, gate 6: 8, gate 7: 6, gate 8: 11, gate 9: 47, and gate 10: 25. All aliases were also rejected. Alias failed-gate counts are gate 2: 25, gate 3: 197, gate 4: 249, gate 5: 83, gate 6: 58, gate 7: 42, gate 8: 39, gate 9: 236, and gate 10: 112. Counts overlap because one evaluation can fail several gates.

All 315 primary and alias evaluations had measured secondary-eclipse and centroid quantities. No missing-measurement fallback was used in this wave. Every primary and 249 aliases failed the frozen leave-one-epoch-out gate. The frozen implementation searches the held-out period near a period selected from all data, so this is a repeatability falsification rather than a fully independent blind period search. The gate counts are not calibrated false-alarm probabilities and do not measure completeness.

Neighbor-query receipts are included but are not repeated by the numerical replay. No separate injection-recovery completeness cohort, momentum-dump audit, or pixel-level independent blend analysis is part of this negative screen.

## Reproduction

`replay.py` downloads the public MAST products recorded by the receipts, verifies their SHA-256 values, and reproduces every primary and fixed-alias evaluation. It fetches the pinned public engine source and verifies all scientific script hashes against the search provenance. The engine files at public upstream commit `19e5e9e8ca72c8e584fd08a92276d285ca474888` were verified to match the recorded script hashes. Run one partition with `python -B registry/batches/2026-11-03-wave-63-negative/replay.py --partition 0`.

The source wave experienced MAST timeouts and recovered workers resumed the same frozen partitions without substitutions. Exact private hosted replay succeeded for all eight partitions before this release was prepared. Public PR CI runs repository verification and adversarial tests once, then exact replay for the eight frozen partitions. FITS files and caches are not included in git.

TESS, MAST, SPOC, QLP, catalog providers, and Open Exoplanet Hunt contributors retain attribution. Codex assisted with execution and preparation. No human scientific review or independent confirmation is claimed.
