# Candidate Vetting Dossier: TIC 4206066

- **Status**: `reference_benchmark_ddt100` (`all_gates_passed = True`)
- **Generated UTC**: `2026-10-09T17:34:44Z`
- **Host Star**: TIC 4206066 ($T_{\text{mag}} = 9.6817$, $T_{\text{eff}} = 4010\text{ K}$, $R_\star = 0.6481\,R_\odot$, $M_\star = 0.630\,M_\odot$, $d = 35.62\text{ pc}$)
- **Sectors Analyzed**: `[6, 32, 98]`

## Primary Signal Ephemeris & Physical Parameters

| Parameter | Value |
| :--- | :--- |
| **Orbital Period ($P$)** | `3.1827846 d` |
| **Mid-Transit Epoch ($T_0$)** | `1468.42382 BTJD` |
| **Transit Duration ($T_{14}$)** | `1.73 h` (`0.07200 d`) |
| **Weighted Transit Depth ($\Delta F$)** | `448.9 ± 26.9 ppm` (BLS box: `410.8 ppm`) |
| **Combined Multi-Sector BLS SNR** | `16.56 σ` |
| **Inferred Planet Radius ($R_p$)** | **`1.50 R_earth`** (assuming target star host) |

## 10-Gate Adversarial Falsification Scorecard

| Gate | Falsification Test | Key Metric | Result |
| :--- | :--- | :--- | :--- |
| **1** | Catalog & Alert De-duplication | `is_known_in_toi_ctoi_ps = False` | PASS |
| **2** | Multi-Sector / Multi-Epoch Baseline | `3` sectors, `24` transits | PASS |
| **3** | Combined Detrended BLS SNR | `16.56 σ` (min `8.0 σ`) | PASS |
| **4** | Blind Leave-One-Epoch-Out (LOEO) Prediction | `min Z = 7.63 σ`, `mean Z = 8.15 σ` | PASS |
| **5** | Odd vs. Even Transit Depth Consistency | Odd `432.5 ppm` vs Even `462.3 ppm` (`0.58 σ`) | PASS |
| **6** | Secondary Eclipse Null Test (Phase 0.5) | `50.5 ± 27.5 ppm` (`1.84 σ`) | PASS |
| **7** | Physical Radius & Keplerian Duration | `$R_p = 1.498 R_\oplus$`, `$T_{14}/T_{14,\text{circ}} = 0.855$` | PASS |
| **8** | In/Out-of-Transit Centroid Stability | `Δr = 0.0037 arcsec` (`1.81 σ`) | PASS |
| **9** | Per-Transit Coherence & Jackknife Stability | `23/24` positive, Jackknife SNR `15.74 σ` | PASS |
| **10** | Rotational Modulation / Starspot Guard | Detrended OOT sin amp `48.0 ppm` (`10.7%` of dip) | PASS |

## Blind Leave-One-Epoch-Out (LOEO) Cross-Validation Breakdown

| Held-Out Sector | Trained Period (d) | Trained $T_0$ (BTJD) | In-Transit Cadences | Predicted Dip in Held-Out Sector | Z-Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Sector 6 | `3.1827940` | `2174.99676` | `17` | `+441.0 ± 57.8 ppm` | **`+7.63 σ`** |
| Sector 32 | `3.1827770` | `1468.43022` | `415` | `+401.6 ± 46.2 ppm` | **`+8.69 σ`** |
| Sector 98 | `3.1827447` | `1468.43022` | `280` | `+339.1 ± 41.8 ppm` | **`+8.12 σ`** |

## Additional Tentative Signals (After Masking Primary Transit)

- **Signal `TIC 4206066.02`**: $P = 11.132741\text{ d}$, $T_0 = 1473.73182\text{ BTJD}$, depth $= 885.8 \pm 59.7\text{ ppm}$, $R_p \approx 2.10\,R_\oplus$, BLS SNR $= 15.39\,\sigma$ (`Tentative multi-sector signal after masking primary transit`)

## Diagnostic Plots

![Diagnostic Plots](diagnostics.png)
