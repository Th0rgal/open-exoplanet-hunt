# Gaia DR3 / TIC Neighbor Blend & Period-Alias Falsification Audit

This document provides the quantitative results of two critical astrophysical falsification tests across all 9 candidate and watchlist dossiers in `open-exoplanet-hunt` (addressing [Issue #2](https://github.com/Th0rgal/open-exoplanet-hunt/issues/2)):

1. **Gaia DR3 / MAST TIC Neighbor Dilution & Centroid-Torque Exclusion ($r \le 120''$)**:
   - Queries every known star in the TESS Input Catalog / Gaia DR3 within $120''$ ($\sim 5.7$ TESS pixels) of each host star.
   - **Flux-Sufficiency Test**: Computes the maximum diluted eclipse depth $\Delta F_{\text{max}, j}$ (in ppm) if neighbor $j$ (with magnitude difference $\Delta T_j = T_j - T_{\text{target}}$ and PSF/aperture coupling $w_j$) were a $100\%$ eclipsing binary. If $\Delta F_{\text{max}, j} < \Delta F_{\text{obs}}$, neighbor $j$ is **mathematically incapable** of producing the transit depth (`RULED_OUT_BY_FLUX`).
   - **Centroid-Torque Test**: If neighbor $j$ at angular separation $d_j$ produces a fractional depth $\Delta F_{\text{obs}}$, it must pull the center of light during transit by $\Delta r_{\text{req}, j} = d_j \times (\Delta F_{\text{obs}} \times 10^{-6})$. If $\Delta r_{\text{req}, j} > \Delta r_{\text{obs}} + 3\sigma_r$, neighbor $j$ is **ruled out at $>3\sigma$ by SPOC/QLP centroid astrometry** (`RULED_OUT_BY_CENTROID`).
2. **Rational Period-Alias Matrix ($P, 2P, P/2, \frac{3}{2}P, \frac{2}{3}P$)**:
   - Evaluates the multi-sector light curve at exact rational multiples of the primary BLS period to test for period-doubling (e.g., equal-depth eclipsing binaries at $2P$) or sub-harmonic aliasing.

## Executive Summary Table

| Target | Host Star | Observed Depth (ppm) | Centroid $3\sigma$ Limit | TIC/Gaia Stars ($\le 120''$) | Ruled Out by Flux | Ruled Out by Centroid | Unresolved ($<31.5''$ & bright) | Preferred Ephemeris |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`TIC 4206066`](../candidates/TIC-4206066/REPORT.md) | StKM 1-561 (K-dwarf, 35.6 pc) | `448.9` | `0.010″` | `41` | `35` | `6` | **`0`** | `1P = 3.18278 d` (`10/10` gates, O/E `0.58σ`) |
| [`TIC 69912980`](../candidates/TIC-69912980/REPORT.md) | G 86-28 (M3.0V, 12.4 pc) | `296.1` | `0.009″` | `114` | `89` | `17` | **`8`** | `1P = 2.19656 d` (`10/10` gates, O/E `1.78σ`) |
| [`TIC 63349323`](../candidates/TIC-63349323/REPORT.md) | PM J02019+3413 (M0.5Ve, 54.0 pc) | `461.7` | `0.012″` | `22` | `18` | `3` | **`1`** | `1P = 4.47226 d` (`9/10` gates, O/E `0.21σ`) |
| [`TIC 119487103`](../candidates/TIC-119487103/REPORT.md) | G 214-12 (M3.0V, 23.1 pc) | `309.8` | `0.009″` | `111` | `91` | `18` | **`2`** | `1P = 5.66920 d` (`9/10` gates, O/E `0.90σ`) |
| [`TIC 120844941`](../candidates/TIC-120844941/REPORT.md) | TYC 2898-1488-1 (K7V, 47.0 pc) | `532.3` | `0.012″` | `208` | `179` | `24` | **`5`** | `1P = 5.20697 d` (`9/10` gates, O/E `0.99σ`) |
| [`TIC 125757128`](../candidates/TIC-125757128/REPORT.md) | HG 8-41 (K5V, 35.8 pc) | `171.3` | `0.005″` | `33` | `25` | `5` | **`3`** | `1P = 1.93834 d` (`9/10` gates, O/E `2.91σ`) |
| [`TIC 252907497`](../candidates/TIC-252907497/REPORT.md) | G 192-59 (M2.0V, 33.2 pc) | `214.6` | `0.011″` | `30` | `21` | `4` | **`5`** | `1P = 2.32380 d` (`9/10` gates, O/E `0.17σ`) |
| [`TIC 265756555`](../candidates/TIC-265756555/REPORT.md) | Ross 24 (M1.0V, 28.2 pc) | `277.3` | `0.009″` | `110` | `88` | `17` | **`5`** | `1P = 3.26694 d` (`9/10` gates, O/E `1.13σ`) |
| [`TIC 457195191`](../candidates/TIC-457195191/REPORT.md) | G 82-48 (M0V, 26.1 pc) | `421.3` | `0.009″` | `31` | `27` | `3` | **`1`** | `1P = 10.51471 d` (`9/10` gates, O/E `3.71σ`) |

## Detailed Per-Target Neighbor & Alias Audits

### [`TIC 4206066`](../candidates/TIC-4206066/REPORT.md) — StKM 1-561 (K-dwarf, 35.6 pc)

- **Observed Transit Depth**: `448.9 ppm` | **Observed In-Transit Centroid Shift**: `0.0037″` (`1.81σ`; $3\sigma$ upper bound: `0.0098″`)
- **Neighbor Exclusion ($r \le 120''$)**: **41** cataloged TIC/Gaia stars within $120''$ — **35** ruled out by flux dilution, **6** ruled out by centroid torque, **0** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 4206057` | `3220385243255181184` | `83.07″` | `13.05` | `+3.37` | `1094.2` | `2188.3` | `0.0373″` | `RULED_OUT_BY_CENTROID` |
| `TIC 4206059` | `3220385243255181952` | `55.00″` | `16.32` | `+6.64` | `590.5` | `1180.9` | `0.0247″` | `RULED_OUT_BY_CENTROID` |
| `TIC 4206077` | `3220388296975320448` | `44.60″` | `17.02` | `+7.34` | `475.3` | `950.6` | `0.0200″` | `RULED_OUT_BY_CENTROID` |
| `TIC 4206064` | `3220385277614918912` | `49.86″` | `16.99` | `+7.31` | `405.7` | `811.4` | `0.0224″` | `RULED_OUT_BY_CENTROID` |
| `TIC 4206073` | `3220388262615571968` | `54.39″` | `17.06` | `+7.38` | `308.4` | `616.8` | `0.0244″` | `RULED_OUT_BY_CENTROID` |
| `TIC 712986149` | `3220385273320363520` | `50.42″` | `17.29` | `+7.61` | `302.5` | `604.9` | `0.0226″` | `RULED_OUT_BY_CENTROID` |
| `TIC 712986249` | `3220388296975929984` | `12.24″` | `18.13` | `+8.45` | `208.8` | `417.6` | `0.0055″` | `RULED_OUT_BY_FLUX` |
| `TIC 4206074` | `3220388266911997952` | `68.63″` | `16.54` | `+6.85` | `189.7` | `379.5` | `0.0308″` | `RULED_OUT_BY_FLUX` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `3.182785` | `448.9 ± 26.9` | `1.50` | `16.56σ` | `+7.63σ` | `+8.15σ` | `0.58σ` | `+1.84σ` | `10/10` |
| **2.0 P (Double Period)** | `6.365564` | `472.6 ± 36.4` | `1.54` | `12.70σ` | `+5.75σ` | `+6.37σ` | `1.74σ` | `+11.02σ` | `9/10` |
| **0.5 P (Half Period)** | `1.591391` | `226.0 ± 19.2` | `1.06` | `12.08σ` | `+5.06σ` | `+5.25σ` | `10.80σ` | `+0.64σ` | `8/10` |
| **1.5 P (3:2 Resonance/Alias)** | `4.770076` | `209.9 ± 24.9` | `1.02` | `8.91σ` | `+0.06σ` | `+0.72σ` | `4.29σ` | `-1.31σ` | `7/10` |
| **0.667 P (2:3 Resonance/Alias)** | `2.121855` | `186.4 ± 21.7` | `0.97` | `9.05σ` | `+0.71σ` | `+2.36σ` | `0.52σ` | `+6.25σ` | `6/10` |

### [`TIC 69912980`](../candidates/TIC-69912980/REPORT.md) — G 86-28 (M3.0V, 12.4 pc)

- **Observed Transit Depth**: `296.1 ppm` | **Observed In-Transit Centroid Shift**: `0.0024″` (`1.04σ`; $3\sigma$ upper bound: `0.0093″`)
- **Neighbor Exclusion ($r \le 120''$)**: **114** cataloged TIC/Gaia stars within $120''$ — **89** ruled out by flux dilution, **17** ruled out by centroid torque, **8** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 69912984` | `156150171773467392` | `25.78″` | `14.66` | `+4.54` | `7553.7` | `15107.4` | `0.0076″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 69912982` | `156150236195426944` | `6.62″` | `14.71` | `+4.59` | `7208.1` | `14416.3` | `0.0020″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 69912963` | `156150171773470336` | `30.35″` | `15.55` | `+5.43` | `3335.7` | `6671.3` | `0.0090″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 69912953` | `156149583360111616` | `68.42″` | `14.09` | `+3.97` | `2741.3` | `5482.5` | `0.0203″` | `RULED_OUT_BY_CENTROID` |
| `TIC 69913643` | `156149965615789952` | `94.66″` | `11.31` | `+1.19` | `1807.2` | `3614.5` | `0.0280″` | `RULED_OUT_BY_CENTROID` |
| `TIC 69913004` | `156150274852680832` | `52.22″` | `15.77` | `+5.65` | `1678.0` | `3356.1` | `0.0155″` | `RULED_OUT_BY_CENTROID` |
| `TIC 504073251` | `156149965613148800` | `94.27″` | `11.92` | `+1.80` | `1089.0` | `2178.1` | `0.0279″` | `RULED_OUT_BY_CENTROID` |
| `TIC 69912968` | `156150236195144192` | `20.85″` | `16.99` | `+6.87` | `890.4` | `1780.8` | `0.0062″` | `UNRESOLVED_WITHIN_PSF` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `2.196560` | `296.1 ± 38.7` | `0.52` | `8.10σ` | `+2.87σ` | `+3.71σ` | `1.78σ` | `+0.37σ` | `10/10` |
| **2.0 P (Double Period)** | `4.393222` | `299.9 ± 42.3` | `0.52` | `7.01σ` | `-0.47σ` | `+1.37σ` | `1.85σ` | `+3.02σ` | `5/10` |
| **0.5 P (Half Period)** | `1.100380` | `109.7 ± 20.4` | `0.32` | `6.69σ` | `-0.17σ` | `+1.12σ` | `1.36σ` | `+1.99σ` | `5/10` |
| **1.5 P (3:2 Resonance/Alias)** | `3.295742` | `187.5 ± 41.0` | `0.41` | `6.28σ` | `-1.55σ` | `+0.05σ` | `1.73σ` | `-2.45σ` | `6/10` |
| **0.667 P (2:3 Resonance/Alias)** | `1.467795` | `103.0 ± 19.2` | `0.31` | `4.92σ` | `+1.51σ` | `+2.34σ` | `1.53σ` | `+0.66σ` | `5/10` |

### [`TIC 63349323`](../candidates/TIC-63349323/REPORT.md) — PM J02019+3413 (M0.5Ve, 54.0 pc)

- **Observed Transit Depth**: `461.7 ppm` | **Observed In-Transit Centroid Shift**: `0.0045″` (`1.81σ`; $3\sigma$ upper bound: `0.0120″`)
- **Neighbor Exclusion ($r \le 120''$)**: **22** cataloged TIC/Gaia stars within $120''$ — **18** ruled out by flux dilution, **3** ruled out by centroid torque, **1** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 63349318` | `329100498962559232` | `33.84″` | `15.76` | `+5.04` | `4742.1` | `9484.2` | `0.0156″` | `RULED_OUT_BY_CENTROID` |
| `TIC 63349324` | `329100498962557824` | `22.59″` | `16.59` | `+5.87` | `2232.1` | `4464.1` | `0.0104″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 63349319` | `329100533322297728` | `84.26″` | `14.61` | `+3.90` | `587.8` | `1175.7` | `0.0389″` | `RULED_OUT_BY_CENTROID` |
| `TIC 63349321` | `329100529026368640` | `64.65″` | `17.66` | `+6.94` | `241.2` | `482.4` | `0.0298″` | `RULED_OUT_BY_CENTROID` |
| `TIC 621054440` | `329100872623753216` | `17.46″` | `19.36` | `+8.65` | `174.0` | `348.0` | `0.0081″` | `RULED_OUT_BY_FLUX` |
| `TIC 621054441` | `329100876919038336` | `11.77″` | `19.46` | `+8.74` | `159.7` | `319.4` | `0.0054″` | `RULED_OUT_BY_FLUX` |
| `TIC 621054438` | `329100567682032256` | `69.34″` | `18.37` | `+7.65` | `85.7` | `171.4` | `0.0320″` | `RULED_OUT_BY_FLUX` |
| `TIC 621054430` | `329100121004896640` | `51.39″` | `19.93` | `+9.21` | `65.9` | `131.8` | `0.0237″` | `RULED_OUT_BY_FLUX` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `4.472257` | `461.7 ± 44.6` | `1.43` | `9.08σ` | `+1.56σ` | `+4.39σ` | `0.21σ` | `+0.41σ` | `9/10` |
| **2.0 P (Double Period)** | `8.928524` | `559.1 ± 75.7` | `1.58` | `7.51σ` | `-0.10σ` | `+1.36σ` | `3.33σ` | `+2.09σ` | `6/10` |
| **0.5 P (Half Period)** | `2.236023` | `238.6 ± 34.3` | `1.03` | `6.48σ` | `-3.47σ` | `+0.71σ` | `5.71σ` | `+2.34σ` | `5/10` |
| **1.5 P (3:2 Resonance/Alias)** | `6.728098` | `323.9 ± 64.2` | `1.20` | `6.02σ` | `-0.77σ` | `+0.05σ` | `2.50σ` | `+0.82σ` | `5/10` |
| **0.667 P (2:3 Resonance/Alias)** | `2.980890` | `289.9 ± 61.2` | `1.14` | `6.32σ` | `+0.79σ` | `+1.93σ` | `0.01σ` | `+1.71σ` | `7/10` |

### [`TIC 119487103`](../candidates/TIC-119487103/REPORT.md) — G 214-12 (M3.0V, 23.1 pc)

- **Observed Transit Depth**: `309.8 ppm` | **Observed In-Transit Centroid Shift**: `0.0021″` (`0.98σ`; $3\sigma$ upper bound: `0.0085″`)
- **Neighbor Exclusion ($r \le 120''$)**: **111** cataloged TIC/Gaia stars within $120''$ — **91** ruled out by flux dilution, **18** ruled out by centroid torque, **2** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 119487115` | `1956721064940975616` | `44.00″` | `12.88` | `+2.63` | `34470.5` | `68940.9` | `0.0136″` | `RULED_OUT_BY_CENTROID` |
| `TIC 119487094` | `1956720996221500416` | `34.94″` | `13.23` | `+2.99` | `29668.3` | `59336.5` | `0.0108″` | `RULED_OUT_BY_CENTROID` |
| `TIC 119487123` | `1956724019878473728` | `68.95″` | `13.13` | `+2.89` | `7014.9` | `14029.8` | `0.0214″` | `RULED_OUT_BY_CENTROID` |
| `TIC 119487099` | `1956723916799137280` | `49.61″` | `15.12` | `+4.88` | `3821.8` | `7643.6` | `0.0154″` | `RULED_OUT_BY_CENTROID` |
| `TIC 119487118` | `1956724019878474368` | `46.72″` | `15.73` | `+5.49` | `2436.2` | `4872.5` | `0.0145″` | `RULED_OUT_BY_CENTROID` |
| `TIC 119487085` | `1956720888843396736` | `45.09″` | `16.23` | `+5.99` | `1629.6` | `3259.2` | `0.0140″` | `RULED_OUT_BY_CENTROID` |
| `TIC 119487095` | `1956721064940977024` | `26.32″` | `16.84` | `+6.59` | `1152.8` | `2305.7` | `0.0082″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 119399151` | `1956723882439399040` | `73.42″` | `14.74` | `+4.50` | `1083.9` | `2167.9` | `0.0227″` | `RULED_OUT_BY_CENTROID` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `5.669195` | `309.8 ± 40.8` | `0.84` | `8.52σ` | `+2.41σ` | `+4.00σ` | `0.90σ` | `+0.34σ` | `9/10` |
| **2.0 P (Double Period)** | `11.341240` | `386.2 ± 55.2` | `0.94` | `7.41σ` | `-1.48σ` | `+0.91σ` | `2.04σ` | `+2.08σ` | `6/10` |
| **0.5 P (Half Period)** | `2.835267` | `237.4 ± 29.9` | `0.73` | `7.97σ` | `-0.82σ` | `+1.48σ` | `1.51σ` | `-0.53σ` | `6/10` |
| **1.5 P (3:2 Resonance/Alias)** | `8.508494` | `360.2 ± 51.9` | `0.90` | `6.43σ` | `-0.97σ` | `+1.26σ` | `2.80σ` | `-2.22σ` | `6/10` |
| **0.667 P (2:3 Resonance/Alias)** | `3.781638` | `229.7 ± 39.0` | `0.72` | `7.04σ` | `+2.32σ` | `+2.82σ` | `0.93σ` | `-1.65σ` | `6/10` |

### [`TIC 120844941`](../candidates/TIC-120844941/REPORT.md) — TYC 2898-1488-1 (K7V, 47.0 pc)

- **Observed Transit Depth**: `532.3 ppm` | **Observed In-Transit Centroid Shift**: `0.0058″` (`2.81σ`; $3\sigma$ upper bound: `0.0120″`)
- **Neighbor Exclusion ($r \le 120''$)**: **208** cataloged TIC/Gaia stars within $120''$ — **179** ruled out by flux dilution, **24** ruled out by centroid torque, **5** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 120844948` | `200307211581405952` | `12.07″` | `12.86` | `+2.74` | `37061.5` | `74123.0` | `0.0064″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 120844905` | `200307314660608000` | `48.24″` | `12.94` | `+2.82` | `25759.8` | `51519.6` | `0.0257″` | `RULED_OUT_BY_CENTROID` |
| `TIC 120844937` | `200307963199768320` | `40.08″` | `13.22` | `+3.10` | `25174.8` | `50349.6` | `0.0213″` | `RULED_OUT_BY_CENTROID` |
| `TIC 120844898` | `200307967495641472` | `65.62″` | `12.56` | `+2.44` | `13762.6` | `27525.2` | `0.0349″` | `RULED_OUT_BY_CENTROID` |
| `TIC 120844928` | `200307241643324672` | `54.41″` | `13.62` | `+3.50` | `10765.5` | `21531.0` | `0.0290″` | `RULED_OUT_BY_CENTROID` |
| `TIC 120844983` | `200307177221676544` | `68.29″` | `13.43` | `+3.31` | `5063.0` | `10126.1` | `0.0364″` | `RULED_OUT_BY_CENTROID` |
| `TIC 120844954` | `200307933135916032` | `43.71″` | `15.31` | `+5.19` | `3531.9` | `7063.8` | `0.0233″` | `RULED_OUT_BY_CENTROID` |
| `TIC 120844987` | `200307177221679744` | `85.23″` | `12.49` | `+2.37` | `2125.0` | `4250.0` | `0.0454″` | `RULED_OUT_BY_CENTROID` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `5.206972` | `532.3 ± 58.2` | `1.69` | `8.29σ` | `+3.30σ` | `+4.57σ` | `0.99σ` | `+3.42σ` | `9/10` |
| **2.0 P (Double Period)** | `10.414389` | `661.3 ± 76.9` | `1.88` | `6.96σ` | `-1.15σ` | `+1.07σ` | `1.09σ` | `+5.55σ` | `6/10` |
| **0.5 P (Half Period)** | `2.607941` | `310.4 ± 29.9` | `1.29` | `9.38σ` | `-3.54σ` | `+0.11σ` | `0.58σ` | `+1.47σ` | `8/10` |
| **1.5 P (3:2 Resonance/Alias)** | `7.822827` | `425.3 ± 50.6` | `1.51` | `6.95σ` | `-5.47σ` | `-2.14σ` | `1.70σ` | `+2.51σ` | `7/10` |
| **0.667 P (2:3 Resonance/Alias)** | `3.461921` | `246.9 ± 35.6` | `1.15` | `6.40σ` | `+1.40σ` | `+3.39σ` | `1.39σ` | `-0.18σ` | `6/10` |

### [`TIC 125757128`](../candidates/TIC-125757128/REPORT.md) — HG 8-41 (K5V, 35.8 pc)

- **Observed Transit Depth**: `171.3 ppm` | **Observed In-Transit Centroid Shift**: `0.0019″` (`1.93σ`; $3\sigma$ upper bound: `0.0049″`)
- **Neighbor Exclusion ($r \le 120''$)**: **33** cataloged TIC/Gaia stars within $120''$ — **25** ruled out by flux dilution, **5** ruled out by centroid torque, **3** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 125757124` | `67270530866703488` | `64.59″` | `15.49` | `+5.59` | `839.7` | `1679.3` | `0.0111″` | `RULED_OUT_BY_CENTROID` |
| `TIC 125757127` | `67270530864023680` | `53.00″` | `17.09` | `+7.19` | `394.6` | `789.1` | `0.0091″` | `RULED_OUT_BY_CENTROID` |
| `TIC 125757120` | `67270565226440064` | `59.63″` | `17.20` | `+7.30` | `245.8` | `491.7` | `0.0102″` | `RULED_OUT_BY_CENTROID` |
| `TIC 640667619` | `67270462144545664` | `10.52″` | `18.35` | `+8.45` | `209.3` | `418.5` | `0.0018″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 640667622` | `67270492210617984` | `42.54″` | `18.50` | `+8.60` | `158.3` | `316.7` | `0.0073″` | `RULED_OUT_BY_CENTROID` |
| `TIC 506522009` | `67270427787489536` | `53.13″` | `18.27` | `+8.37` | `131.7` | `263.3` | `0.0091″` | `RULED_OUT_BY_CENTROID` |
| `TIC 640667491` | `67267502913375104` | `28.16″` | `19.08` | `+9.18` | `106.3` | `212.5` | `0.0048″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 640667621` | `67270492210615424` | `21.25″` | `19.26` | `+9.36` | `90.5` | `181.0` | `0.0036″` | `UNRESOLVED_WITHIN_PSF` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `1.938344` | `171.3 ± 17.3` | `0.84` | `9.24σ` | `+3.05σ` | `+4.54σ` | `2.91σ` | `+2.25σ` | `9/10` |
| **2.0 P (Double Period)** | `3.876761` | `243.2 ± 25.5` | `1.00` | `9.14σ` | `+1.91σ` | `+4.14σ` | `1.09σ` | `+2.68σ` | `7/10` |
| **0.5 P (Half Period)** | `0.967932` | `96.3 ± 12.3` | `0.63` | `7.52σ` | `+0.77σ` | `+2.25σ` | `1.84σ` | `+1.24σ` | `5/10` |
| **1.5 P (3:2 Resonance/Alias)** | `2.915069` | `138.7 ± 21.0` | `0.76` | `6.66σ` | `+0.68σ` | `+1.40σ` | `1.33σ` | `+1.46σ` | `6/10` |
| **0.667 P (2:3 Resonance/Alias)** | `1.292234` | `103.7 ± 13.7` | `0.66` | `7.08σ` | `-1.00σ` | `+2.16σ` | `0.76σ` | `+1.66σ` | `6/10` |

### [`TIC 252907497`](../candidates/TIC-252907497/REPORT.md) — G 192-59 (M2.0V, 33.2 pc)

- **Observed Transit Depth**: `214.6 ppm` | **Observed In-Transit Centroid Shift**: `0.0061″` (`3.96σ`; $3\sigma$ upper bound: `0.0107″`)
- **Neighbor Exclusion ($r \le 120''$)**: **30** cataloged TIC/Gaia stars within $120''$ — **21** ruled out by flux dilution, **4** ruled out by centroid torque, **5** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 252907489` | `981020596841670400` | `39.89″` | `15.48` | `+5.13` | `4063.4` | `8126.7` | `0.0086″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 252907502` | `981020734280622848` | `55.31″` | `15.65` | `+5.29` | `2004.1` | `4008.1` | `0.0119″` | `RULED_OUT_BY_CENTROID` |
| `TIC 252910210` | `981019978366377216` | `64.30″` | `15.42` | `+5.07` | `1386.1` | `2772.1` | `0.0138″` | `RULED_OUT_BY_CENTROID` |
| `TIC 252907487` | `981020562481933440` | `61.34″` | `16.41` | `+6.05` | `690.1` | `1380.3` | `0.0132″` | `RULED_OUT_BY_CENTROID` |
| `TIC 252907492` | `981019939710827392` | `36.67″` | `17.90` | `+7.55` | `464.2` | `928.5` | `0.0079″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 252907498` | `981020661265338112` | `66.82″` | `16.55` | `+6.20` | `402.7` | `805.4` | `0.0143″` | `RULED_OUT_BY_CENTROID` |
| `TIC 252907495` | `—` | `49.93″` | `17.84` | `+7.48` | `346.3` | `692.7` | `0.0107″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 742695608` | `981020592545854848` | `34.14″` | `18.30` | `+7.94` | `329.9` | `659.8` | `0.0073″` | `UNRESOLVED_WITHIN_PSF` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `2.323799` | `214.6 ± 25.5` | `0.83` | `8.06σ` | `+2.00σ` | `+3.88σ` | `0.17σ` | `-0.94σ` | `9/10` |
| **2.0 P (Double Period)** | `4.649624` | `262.6 ± 37.1` | `0.92` | `7.73σ` | `-2.84σ` | `+0.32σ` | `3.56σ` | `+0.53σ` | `6/10` |
| **0.5 P (Half Period)** | `1.162338` | `126.9 ± 16.9` | `0.64` | `6.94σ` | `-0.15σ` | `+1.46σ` | `2.54σ` | `+2.86σ` | `3/10` |
| **1.5 P (3:2 Resonance/Alias)** | `3.485958` | `190.7 ± 28.5` | `0.79` | `6.68σ` | `+0.10σ` | `+1.32σ` | `1.80σ` | `+0.75σ` | `6/10` |
| **0.667 P (2:3 Resonance/Alias)** | `1.552427` | `147.7 ± 21.0` | `0.69` | `6.62σ` | `+0.76σ` | `+1.82σ` | `0.70σ` | `+0.97σ` | `6/10` |

### [`TIC 265756555`](../candidates/TIC-265756555/REPORT.md) — Ross 24 (M1.0V, 28.2 pc)

- **Observed Transit Depth**: `277.3 ppm` | **Observed In-Transit Centroid Shift**: `0.0020″` (`0.90σ`; $3\sigma$ upper bound: `0.0087″`)
- **Neighbor Exclusion ($r \le 120''$)**: **110** cataloged TIC/Gaia stars within $120''$ — **88** ruled out by flux dilution, **17** ruled out by centroid torque, **5** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 265756556` | `251688317661230464` | `56.20″` | `15.34` | `+5.11` | `2259.3` | `4518.5` | `0.0156″` | `RULED_OUT_BY_CENTROID` |
| `TIC 265756558` | `251687527387239552` | `33.17″` | `16.22` | `+5.99` | `1990.2` | `3980.5` | `0.0092″` | `RULED_OUT_BY_CENTROID` |
| `TIC 265756557` | `251688283301484928` | `13.78″` | `16.28` | `+6.05` | `1894.8` | `3789.6` | `0.0038″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 265756599` | `251687836624888320` | `92.27″` | `12.20` | `+1.97` | `1238.7` | `2477.4` | `0.0256″` | `RULED_OUT_BY_CENTROID` |
| `TIC 265756580` | `251688214582019968` | `71.59″` | `15.04` | `+4.81` | `964.3` | `1928.6` | `0.0199″` | `RULED_OUT_BY_CENTROID` |
| `TIC 265756503` | `251688558179385856` | `87.95″` | `13.21` | `+2.98` | `864.9` | `1729.7` | `0.0244″` | `RULED_OUT_BY_CENTROID` |
| `TIC 265756577` | `251688145862541824` | `65.93″` | `16.34` | `+6.11` | `469.9` | `939.8` | `0.0183″` | `RULED_OUT_BY_CENTROID` |
| `TIC 265756584` | `251687488728768896` | `35.87″` | `17.88` | `+7.65` | `426.2` | `852.3` | `0.0099″` | `RULED_OUT_BY_CENTROID` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `3.266938` | `277.3 ± 37.0` | `0.86` | `7.70σ` | `+2.15σ` | `+4.16σ` | `1.13σ` | `+2.05σ` | `9/10` |
| **2.0 P (Double Period)** | `6.549214` | `407.2 ± 43.3` | `1.04` | `6.96σ` | `-6.28σ` | `-1.33σ` | `2.15σ` | `+5.88σ` | `7/10` |
| **0.5 P (Half Period)** | `1.633483` | `165.6 ± 22.2` | `0.66` | `7.41σ` | `+1.62σ` | `+2.85σ` | `2.54σ` | `+0.61σ` | `5/10` |
| **1.5 P (3:2 Resonance/Alias)** | `4.900624` | `274.4 ± 39.8` | `0.85` | `6.95σ` | `-1.43σ` | `-0.15σ` | `1.63σ` | `-0.61σ` | `7/10` |
| **0.667 P (2:3 Resonance/Alias)** | `2.181418` | `209.6 ± 37.9` | `0.75` | `5.62σ` | `-1.51σ` | `-0.47σ` | `0.34σ` | `+2.16σ` | `7/10` |

### [`TIC 457195191`](../candidates/TIC-457195191/REPORT.md) — G 82-48 (M0V, 26.1 pc)

- **Observed Transit Depth**: `421.3 ppm` | **Observed In-Transit Centroid Shift**: `0.0017″` (`0.69σ`; $3\sigma$ upper bound: `0.0091″`)
- **Neighbor Exclusion ($r \le 120''$)**: **31** cataloged TIC/Gaia stars within $120''$ — **27** ruled out by flux dilution, **3** ruled out by centroid torque, **1** unresolved blending stars capable of mimicking the dip.

#### Brightest / Closest Cataloged Neighbors ($r \le 120''$, Top 8 by Max Diluted Depth)

| Neighbor TIC | Gaia DR3 ID | Sep ($''$) | $T_{\text{mag}}$ | $\Delta T$ | Max Depth (50% EB, ppm) | Max Depth (100% Occ, ppm) | Req. Centroid Shift ($''$) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TIC 457195185` | `3232579548761177984` | `36.25″` | `14.17` | `+4.61` | `6862.9` | `13725.8` | `0.0153″` | `RULED_OUT_BY_CENTROID` |
| `TIC 457195196` | `3232581026229926528` | `43.88″` | `16.25` | `+6.69` | `885.6` | `1771.2` | `0.0185″` | `RULED_OUT_BY_CENTROID` |
| `TIC 457195190` | `3232581026229926784` | `48.57″` | `17.22` | `+7.66` | `309.3` | `618.6` | `0.0205″` | `RULED_OUT_BY_CENTROID` |
| `TIC 457195187` | `3232579544464889344` | `17.33″` | `17.98` | `+8.42` | `214.4` | `428.8` | `0.0073″` | `UNRESOLVED_WITHIN_PSF` |
| `TIC 457195199` | `3232591299790004736` | `34.38″` | `18.56` | `+9.00` | `124.4` | `248.8` | `0.0145″` | `RULED_OUT_BY_FLUX` |
| `TIC 457193525` | `3232591295495408384` | `19.71″` | `18.65` | `+9.09` | `115.8` | `231.6` | `0.0083″` | `RULED_OUT_BY_FLUX` |
| `TIC 457195194` | `3232581026229926400` | `50.52″` | `18.31` | `+8.75` | `104.6` | `209.2` | `0.0213″` | `RULED_OUT_BY_FLUX` |
| `TIC 672407344` | `3232591299790802048` | `10.96″` | `19.20` | `+9.64` | `69.6` | `139.3` | `0.0046″` | `RULED_OUT_BY_FLUX` |

#### Rational Period-Alias Evaluation ($P, 2P, P/2, 3P/2, 2P/3$)

| Tested Alias | Period (d) | Depth (ppm) | $R_p$ ($R_\oplus$) | BLS SNR | LOEO Min $Z$ | LOEO Mean $Z$ | Odd/Even ($\sigma$) | Phase-0.5 Sec ($\sigma$) | Gates Passed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.0 P (Certified Primary)** | `10.514707` | `421.3 ± 36.5` | `1.22` | `10.71σ` | `+2.09σ` | `+6.11σ` | `3.71σ` | `+2.15σ` | `9/10` |
| **2.0 P (Double Period)** | `21.029398` | `610.6 ± 50.0` | `1.47` | `10.59σ` | `+0.43σ` | `+1.49σ` | `1.69σ` | `+6.47σ` | `7/10` |
| **0.5 P (Half Period)** | `5.257350` | `212.3 ± 24.4` | `0.87` | `7.57σ` | `-1.79σ` | `-0.37σ` | `7.33σ` | `+1.35σ` | `6/10` |
| **1.5 P (3:2 Resonance/Alias)** | `15.796541` | `564.2 ± 56.9` | `1.42` | `9.46σ` | `-9.14σ` | `-2.84σ` | `4.68σ` | `+1.72σ` | `6/10` |
| **0.667 P (2:3 Resonance/Alias)** | `6.991236` | `250.5 ± 43.0` | `0.94` | `7.46σ` | `-1.14σ` | `-0.07σ` | `2.30σ` | `-0.51σ` | `7/10` |

