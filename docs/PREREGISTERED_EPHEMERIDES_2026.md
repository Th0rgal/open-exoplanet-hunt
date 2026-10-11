# Preregistered Autumn 2026 Transit Ephemerides (Falsification & Follow-Up Schedule)

Every candidate and watchlist dossier in `open-exoplanet-hunt` is accompanied by an exact linear ephemeris ($T_0, P$) fit exclusively on archived TESS 2-minute SPOC PDCSAP observations. To enable blind prospective falsification—either by upcoming TESS Extended Mission sectors (e.g., **TESS Sector 110**, October 31 – November 27, 2026) or by ground-based meter-class / space-based (CHEOPS) diffuser photometry—this document preregisters the predicted mid-transit epochs ($T_c$) across the **October 31 – November 27, 2026** window (**BTJD 4344.5 – 4371.5**, `JD 2461344.5 – 2461371.5`).

> **Falsification Protocol**: A genuine planetary transit must recur on its linear ephemeris with consistent depth ($\Delta F$) and duration ($D$) across unseen future epochs. If a target is observed across $\ge 3$ predicted transit windows with photometric precision $\sigma_{\text{window}} \le \Delta F / 3$ and yields an in-transit phase-folded significance $Z_{\text{holdout}} < +2.0\sigma$, the candidate is **falsified**.

## Summary of Preregistered Ephemerides

| Target | Host Star | Disposition | $P$ (days) | $T_0$ (BTJD) | Depth (ppm) | Duration (hr) | $R_p$ ($R_\oplus$) | Transits in Window (Oct 31 – Nov 27, 2026) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`TIC 4206066`](../candidates/TIC-4206066/REPORT.md) | StKM 1-561 (K-dwarf, 35.6 pc) | **10/10 Benchmark** | `3.1827846` | `1468.42382` | `448.9 ± 26.9` | `1.73` | `1.50` | `9` |
| [`TIC 69912980`](../candidates/TIC-69912980/REPORT.md) | G 86-28 (M3.0V, 12.4 pc) | **10/10 PASS** | `2.1965600` | `1816.36994` | `296.1 ± 38.7` | `0.96` | `0.52` | `13` |
| [`TIC 63349323`](../candidates/TIC-63349323/REPORT.md) | PM J02019+3413 (M0.5Ve, 54.0 pc) | **9/10 Watchlist** | `4.4722572` | `1791.36002` | `461.7 ± 44.6` | `3.36` | `1.43` | `6` |
| [`TIC 120844941`](../candidates/TIC-120844941/REPORT.md) | TYC 2898-1488-1 (K7V, 47.0 pc) | **9/10 Watchlist** | `5.2069719` | `2915.97443` | `532.3 ± 58.2` | `1.73` | `1.69` | `5` |
| [`TIC 125757128`](../candidates/TIC-125757128/REPORT.md) | HG 8-41 (K5V, 35.8 pc) | **9/10 Watchlist** | `1.9383440` | `2475.42348` | `171.3 ± 17.3` | `3.36` | `0.84` | `14` |
| [`TIC 252907497`](../candidates/TIC-252907497/REPORT.md) | G 192-59 (M2.0V, 33.2 pc) | **9/10 Watchlist** | `2.3237992` | `1844.33500` | `214.6 ± 25.5` | `2.98` | `0.83` | `12` |
| [`TIC 265756555`](../candidates/TIC-265756555/REPORT.md) | Ross 24 (M1.0V, 28.2 pc) | **9/10 Watchlist** | `3.2669382` | `1817.42473` | `277.3 ± 37.0` | `2.21` | `0.86` | `8` |
| [`TIC 457195191`](../candidates/TIC-457195191/REPORT.md) | G 82-48 (M0V, 26.1 pc) | **9/10 Watchlist** | `10.5147068` | `1448.00771` | `421.3 ± 36.5` | `3.36` | `1.22` | `3` |

## Per-Target Transit Windows (Oct 31 – Nov 27, 2026)

### [`TIC 4206066`](../candidates/TIC-4206066/REPORT.md) — StKM 1-561 (K-dwarf, 35.6 pc) (10/10 Benchmark)

- **Linear Ephemeris**: $T_c(E) = 1468.42382 + E \times 3.1827846\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 448.9 \pm 26.9\text{ ppm}$ ($R_p \approx 1.50\,R_\oplus$), Duration $D = 1.73\text{ hr}$
- **Archived TESS Sectors**: `[6, 32, 98]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `904` | `4345.66110` | `2026-11-01 03:51 UTC` | `4345.62506` | `4345.69714` |
| `905` | `4348.84388` | `2026-11-04 08:15 UTC` | `4348.80784` | `4348.87992` |
| `906` | `4352.02667` | `2026-11-07 12:38 UTC` | `4351.99063` | `4352.06271` |
| `907` | `4355.20945` | `2026-11-10 17:01 UTC` | `4355.17341` | `4355.24549` |
| `908` | `4358.39224` | `2026-11-13 21:24 UTC` | `4358.35620` | `4358.42828` |
| `909` | `4361.57502` | `2026-11-17 01:48 UTC` | `4361.53898` | `4361.61106` |
| `910` | `4364.75781` | `2026-11-20 06:11 UTC` | `4364.72176` | `4364.79385` |
| `911` | `4367.94059` | `2026-11-23 10:34 UTC` | `4367.90455` | `4367.97663` |
| `912` | `4371.12338` | `2026-11-26 14:57 UTC` | `4371.08733` | `4371.15942` |

### [`TIC 69912980`](../candidates/TIC-69912980/REPORT.md) — G 86-28 (M3.0V, 12.4 pc) (10/10 PASS)

- **Linear Ephemeris**: $T_c(E) = 1816.36994 + E \times 2.1965600\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 296.1 \pm 38.7\text{ ppm}$ ($R_p \approx 0.52\,R_\oplus$), Duration $D = 0.96\text{ hr}$
- **Archived TESS Sectors**: `[19, 43, 44, 71]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `1151` | `4344.61050` | `2026-10-31 02:39 UTC` | `4344.59050` | `4344.63050` |
| `1152` | `4346.80706` | `2026-11-02 07:22 UTC` | `4346.78706` | `4346.82706` |
| `1153` | `4349.00362` | `2026-11-04 12:05 UTC` | `4348.98362` | `4349.02362` |
| `1154` | `4351.20018` | `2026-11-06 16:48 UTC` | `4351.18018` | `4351.22018` |
| `1155` | `4353.39674` | `2026-11-08 21:31 UTC` | `4353.37674` | `4353.41674` |
| `1156` | `4355.59330` | `2026-11-11 02:14 UTC` | `4355.57330` | `4355.61330` |
| `1157` | `4357.78986` | `2026-11-13 06:57 UTC` | `4357.76986` | `4357.80986` |
| `1158` | `4359.98642` | `2026-11-15 11:40 UTC` | `4359.96642` | `4360.00642` |
| `1159` | `4362.18298` | `2026-11-17 16:23 UTC` | `4362.16298` | `4362.20298` |
| `1160` | `4364.37954` | `2026-11-19 21:06 UTC` | `4364.35954` | `4364.39954` |
| `1161` | `4366.57610` | `2026-11-22 01:49 UTC` | `4366.55610` | `4366.59610` |
| `1162` | `4368.77266` | `2026-11-24 06:32 UTC` | `4368.75266` | `4368.79266` |
| `1163` | `4370.96922` | `2026-11-26 11:15 UTC` | `4370.94922` | `4370.98922` |

### [`TIC 63349323`](../candidates/TIC-63349323/REPORT.md) — PM J02019+3413 (M0.5Ve, 54.0 pc) (9/10 Watchlist)

- **Linear Ephemeris**: $T_c(E) = 1791.36002 + E \times 4.4722572\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 461.7 \pm 44.6\text{ ppm}$ ($R_p \approx 1.43\,R_\oplus$), Duration $D = 3.36\text{ hr}$
- **Archived TESS Sectors**: `[18, 58, 85]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `571` | `4345.01888` | `2026-10-31 12:27 UTC` | `4344.94888` | `4345.08888` |
| `572` | `4349.49114` | `2026-11-04 23:47 UTC` | `4349.42114` | `4349.56114` |
| `573` | `4353.96340` | `2026-11-09 11:07 UTC` | `4353.89340` | `4354.03340` |
| `574` | `4358.43565` | `2026-11-13 22:27 UTC` | `4358.36565` | `4358.50565` |
| `575` | `4362.90791` | `2026-11-18 09:47 UTC` | `4362.83791` | `4362.97791` |
| `576` | `4367.38017` | `2026-11-22 21:07 UTC` | `4367.31017` | `4367.45017` |

### [`TIC 120844941`](../candidates/TIC-120844941/REPORT.md) — TYC 2898-1488-1 (K7V, 47.0 pc) (9/10 Watchlist)

- **Linear Ephemeris**: $T_c(E) = 2915.97443 + E \times 5.2069719\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 532.3 \pm 58.2\text{ ppm}$ ($R_p \approx 1.69\,R_\oplus$), Duration $D = 1.73\text{ hr}$
- **Archived TESS Sectors**: `[59, 73, 86]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `275` | `4347.89170` | `2026-11-03 09:24 UTC` | `4347.85566` | `4347.92774` |
| `276` | `4353.09867` | `2026-11-08 14:22 UTC` | `4353.06263` | `4353.13472` |
| `277` | `4358.30565` | `2026-11-13 19:20 UTC` | `4358.26960` | `4358.34169` |
| `278` | `4363.51262` | `2026-11-19 00:18 UTC` | `4363.47658` | `4363.54866` |
| `279` | `4368.71959` | `2026-11-24 05:16 UTC` | `4368.68355` | `4368.75563` |

### [`TIC 125757128`](../candidates/TIC-125757128/REPORT.md) — HG 8-41 (K5V, 35.8 pc) (9/10 Watchlist)

- **Linear Ephemeris**: $T_c(E) = 2475.42348 + E \times 1.9383440\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 171.3 \pm 17.3\text{ ppm}$ ($R_p \approx 0.84\,R_\oplus$), Duration $D = 3.36\text{ hr}$
- **Archived TESS Sectors**: `[43, 44, 70, 71]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `965` | `4345.92544` | `2026-11-01 10:12 UTC` | `4345.85544` | `4345.99544` |
| `966` | `4347.86378` | `2026-11-03 08:43 UTC` | `4347.79378` | `4347.93378` |
| `967` | `4349.80213` | `2026-11-05 07:15 UTC` | `4349.73213` | `4349.87213` |
| `968` | `4351.74047` | `2026-11-07 05:46 UTC` | `4351.67047` | `4351.81047` |
| `969` | `4353.67882` | `2026-11-09 04:17 UTC` | `4353.60882` | `4353.74882` |
| `970` | `4355.61716` | `2026-11-11 02:48 UTC` | `4355.54716` | `4355.68716` |
| `971` | `4357.55550` | `2026-11-13 01:19 UTC` | `4357.48550` | `4357.62550` |
| `972` | `4359.49385` | `2026-11-14 23:51 UTC` | `4359.42385` | `4359.56385` |
| `973` | `4361.43219` | `2026-11-16 22:22 UTC` | `4361.36219` | `4361.50219` |
| `974` | `4363.37054` | `2026-11-18 20:53 UTC` | `4363.30054` | `4363.44054` |
| `975` | `4365.30888` | `2026-11-20 19:24 UTC` | `4365.23888` | `4365.37888` |
| `976` | `4367.24722` | `2026-11-22 17:56 UTC` | `4367.17722` | `4367.31722` |
| `977` | `4369.18557` | `2026-11-24 16:27 UTC` | `4369.11557` | `4369.25557` |
| `978` | `4371.12391` | `2026-11-26 14:58 UTC` | `4371.05391` | `4371.19391` |

### [`TIC 252907497`](../candidates/TIC-252907497/REPORT.md) — G 192-59 (M2.0V, 33.2 pc) (9/10 Watchlist)

- **Linear Ephemeris**: $T_c(E) = 1844.33500 + E \times 2.3237992\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 214.6 \pm 25.5\text{ ppm}$ ($R_p \approx 0.83\,R_\oplus$), Duration $D = 2.98\text{ hr}$
- **Archived TESS Sectors**: `[20, 47, 60, 73]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `1076` | `4344.74294` | `2026-10-31 05:49 UTC` | `4344.68086` | `4344.80502` |
| `1077` | `4347.06674` | `2026-11-02 13:36 UTC` | `4347.00466` | `4347.12882` |
| `1078` | `4349.39054` | `2026-11-04 21:22 UTC` | `4349.32845` | `4349.45262` |
| `1079` | `4351.71434` | `2026-11-07 05:08 UTC` | `4351.65225` | `4351.77642` |
| `1080` | `4354.03814` | `2026-11-09 12:54 UTC` | `4353.97605` | `4354.10022` |
| `1081` | `4356.36194` | `2026-11-11 20:41 UTC` | `4356.29985` | `4356.42402` |
| `1082` | `4358.68573` | `2026-11-14 04:27 UTC` | `4358.62365` | `4358.74782` |
| `1083` | `4361.00953` | `2026-11-16 12:13 UTC` | `4360.94745` | `4361.07162` |
| `1084` | `4363.33333` | `2026-11-18 19:59 UTC` | `4363.27125` | `4363.39542` |
| `1085` | `4365.65713` | `2026-11-21 03:46 UTC` | `4365.59505` | `4365.71922` |
| `1086` | `4367.98093` | `2026-11-23 11:32 UTC` | `4367.91885` | `4368.04301` |
| `1087` | `4370.30473` | `2026-11-25 19:18 UTC` | `4370.24265` | `4370.36681` |

### [`TIC 265756555`](../candidates/TIC-265756555/REPORT.md) — Ross 24 (M1.0V, 28.2 pc) (9/10 Watchlist)

- **Linear Ephemeris**: $T_c(E) = 1817.42473 + E \times 3.2669382\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 277.3 \pm 37.0\text{ ppm}$ ($R_p \approx 0.86\,R_\oplus$), Duration $D = 2.21\text{ hr}$
- **Archived TESS Sectors**: `[19, 59, 86]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `774` | `4346.03490` | `2026-11-01 12:50 UTC` | `4345.98886` | `4346.08094` |
| `775` | `4349.30184` | `2026-11-04 19:14 UTC` | `4349.25579` | `4349.34788` |
| `776` | `4352.56877` | `2026-11-08 01:39 UTC` | `4352.52273` | `4352.61481` |
| `777` | `4355.83571` | `2026-11-11 08:03 UTC` | `4355.78967` | `4355.88175` |
| `778` | `4359.10265` | `2026-11-14 14:27 UTC` | `4359.05661` | `4359.14869` |
| `779` | `4362.36959` | `2026-11-17 20:52 UTC` | `4362.32355` | `4362.41563` |
| `780` | `4365.63653` | `2026-11-21 03:16 UTC` | `4365.59048` | `4365.68257` |
| `781` | `4368.90346` | `2026-11-24 09:40 UTC` | `4368.85742` | `4368.94951` |

### [`TIC 457195191`](../candidates/TIC-457195191/REPORT.md) — G 82-48 (M0V, 26.1 pc) (9/10 Watchlist)

- **Linear Ephemeris**: $T_c(E) = 1448.00771 + E \times 10.5147068\text{ BTJD}$
- **Expected Transit Depth**: $\Delta F = 421.3 \pm 36.5\text{ ppm}$ ($R_p \approx 1.22\,R_\oplus$), Duration $D = 3.36\text{ hr}$
- **Archived TESS Sectors**: `[5, 32, 98]`

| Cycle $E$ | Mid-Transit $T_c$ (BTJD) | Mid-Transit (UTC, Barycentric) | Ingress $T_1$ (BTJD) | Egress $T_4$ (BTJD) |
| :--- | :--- | :--- | :--- | :--- |
| `276` | `4350.06679` | `2026-11-05 13:36 UTC` | `4349.99679` | `4350.13679` |
| `277` | `4360.58149` | `2026-11-16 01:57 UTC` | `4360.51149` | `4360.65149` |
| `278` | `4371.09620` | `2026-11-26 14:18 UTC` | `4371.02620` | `4371.16620` |
