# Index of Existing Exoplanet Discoveries, AI/ML Pipelines & Citizen Science Projects

This document indexes the current landscape of exoplanet discovery across official NASA catalogs, deep-learning/machine-learning pipelines, citizen science, and independent AI-agent workflows as of **October 2026**.

All `15,025` unique TIC stars with known planets or candidates across NASA's `pscomppars`, official `TOI`, ExoFOP `CTOI`, and external AI/ML catalogs are machine-indexed in [`catalog/known_tics.json.gz`](../catalog/known_tics.json.gz) and [`catalog/external_discoveries.json`](../catalog/external_discoveries.json) so that automated scanners never waste compute or claim already-known signals.

---

## 1. Deep-Dive Review: Pavel Rabtsevich's `TIC 4206066` (`StKM 1-561`) Discovery (October 2026)

### 1.1 Overview of the Claim
- **Announcement**: [X Thread by `@p_rabtsevich` (Oct 7, 2026)](https://x.com/p_rabtsevich/status/2107803696058822742) & [Reddit `r/ClaudeAI` write-up](https://www.reddit.com/r/ClaudeAI/comments/1wzw8zd/i_think_i_found_a_planet_nobody_knew_existed_i/)
- **Preprint**: *"Two Transit-like Signals in TESS Photometry of the Nearby K Dwarf TIC 4206066"* ([`doi:10.5281/zenodo.22967456`](https://doi.org/10.5281/zenodo.22967456))
- **Supporting Code & Data**: [`doi:10.5281/zenodo.22967099`](https://doi.org/10.5281/zenodo.22967099)
- **Preregistered Sector 110 Predictions**: [`doi:10.5281/zenodo.23175179`](https://doi.org/10.5281/zenodo.23175179) (Approved as **NASA TESS Director's Discretionary Target Program #100** for 2-minute cadence observations from **October 31 to November 26, 2026**)
- **Host Star**: `TIC 4206066` (`StKM 1-561`), a bright ($T_{\text{mag}} = 9.68$), nearby ($d = 35.62\text{ pc} \approx 116.2\text{ ly}$) late-K dwarf ($T_{\text{eff}} = 4010\text{ K}$, $R_\star = 0.648\,R_\odot$, $M_\star = 0.63\,M_\odot$).

### 1.2 Why Official Automated Pipelines Missed `TIC 4206066`
Our independent inspection of the MAST archive (`Mast.Caom.Filtered`) reveals the exact structural blind spot that hid `TIC 4206066` for seven years:
1. **Sector 6 (2018)**: `TIC 4206066` was *not* on the 2-minute SPOC target list; it was only recorded in 30-minute Full-Frame Images (`HLSP/tess-spoc` and `HLSP/qlp`, $1800\text{ s}$ cadence).
2. **Sector 32 (2020)**: Observed at 2-minute SPOC cadence (`tess2020324010417-s0032-0000000004206066-0200-s_lc.fits`), where 8 transits of ~450 ppm depth yielded a single-sector SNR around the SPOC alert boundary without multi-sector 2-minute reinforcement.
3. **Sector 98 (late 2025)**: Again observed only in 200-second Full-Frame Images (`hlsp_qlp_tess_ffi_s0098-0000000004206066_tess_v01_llc.fits`), not in 2-minute SPOC target files.

Because official SPOC multi-sector searches primarily stitch 2-minute target files, and FFI pipelines typically process sectors or single years in isolation, **stitching cross-pipeline products (`S6 TESS-SPOC` + `S32 SPOC 2-min` + `S98 QLP 200s`) across a 7-year baseline (2018–2025)** boosts the coherent transit SNR from ~8.5–11$\sigma$ per sector to **$16.55\sigma$ combined**.

### 1.3 Our Independent Raw-FITS Reproduction & Audit (`candidates/TIC-4206066/`)
We downloaded the raw MAST FITS files for Sectors 6, 32, and 98 and ran our 10-gate adversarial falsification engine ([`candidates/TIC-4206066/REPORT.md`](../candidates/TIC-4206066/REPORT.md)):
- **Primary Signal (`TIC 4206066.01`)**:
  - **Period**: $P = 3.1827828\text{ d}$, $T_0 = 1468.42382\text{ BTJD}$, duration $T_{14} = 1.73\text{ h}$ ($85.5\%$ of circular $b=0$ duration).
  - **Weighted Transit Depth**: $447.3 \pm 26.9\text{ ppm}$ ($\text{BLS SNR} = 16.55\sigma$), corresponding to **$R_p = 1.50\,R_\oplus$** if on the target star.
  - **Blind Leave-One-Epoch-Out (LOEO) Cross-Validation**:
    - Train on `2020 + 2025` $\to$ Predict hidden `2018 (Sector 6)`: **$+441.0 \pm 57.8\text{ ppm}$ ($+7.63\sigma$)**
    - Train on `2018 + 2025` $\to$ Predict hidden `2020 (Sector 32)`: **$+401.6 \pm 46.2\text{ ppm}$ ($+8.69\sigma$)**
    - Train on `2018 + 2020` $\to$ Predict hidden `2025 (Sector 98)`: **$+345.5 \pm 41.7\text{ ppm}$ ($+8.29\sigma$)**
  - **Odd vs. Even Depth**: $428.8 \pm 38.6\text{ ppm}$ (odd) vs. $462.5 \pm 34.8\text{ ppm}$ (even) — **$0.65\sigma$ difference**.
  - **Secondary Eclipse at $0.5 P$**: $51.6 \pm 27.5\text{ ppm}$ ($1.88\sigma$, null).
  - **In-Transit Centroid Shift**: $0.0037''$ ($1.81\sigma$, null).
  - **Per-Transit Coherence**: $23/24$ transits positive; Jackknife SNR $= 15.62\sigma$.
- **Tentative Secondary Signal (`TIC 4206066.02`)**:
  - After masking Signal A, BLS recovers $P_B = 11.132736\text{ d}$ ($T_0 = 1473.73182\text{ BTJD}$, $R_p \approx 2.11\,R_\oplus$), which has only ~2 transits per sector (~6 total) and will be decisively tested by the 3 predicted transits in Sector 110.

---

## 2. Survey of Similar Projects Across the Internet (2018–2026)

### 2.1 Institutional & Academic AI/ML Pipelines
| Project / Team | Methodology | Scale & Discoveries | Links |
| :--- | :--- | :--- | :--- |
| **RAVEN** (Univ. of Warwick — Hadjigeorghiou, Armstrong et al., Mar 2026) | Gradient Boosted Decision Trees (`XGBoost`) + Gaussian Process classifiers + Bayesian positional probabilities | Applied to 2.2M TESS Year 1–4 FFI stars; **118 newly validated exoplanets** (31 brand-new) and **2,000+ candidates** | [GitHub](https://github.com/ahadjigeorghiou/RAVEN) · [arXiv:2603.22597](https://arxiv.org/abs/2603.22597) |
| **ExoMiner & ExoMiner++** (NASA Ames — Valizadegan et al., 2021–2026) | Multi-branch deep neural network using transfer learning from Kepler to TESS DV reports | Validated **370+ Kepler planets** and flagged **~7,000 TESS multi-sector candidates** | [GitHub](https://github.com/nasa/ExoMiner) · [arXiv:2502.09790](https://arxiv.org/abs/2502.09790) |
| **Princeton T16 Survey** (Princeton Univ., Apr 2026) | Random-forest ML classifier on difference-image FFI photometry down to $T=16$ (`mast:HLSP/t16`) | Surveyed **83,717,159 TESS Year-1 stars**; identified **11,554 candidates** (**10,091 new**); confirmed hot Jupiter `TIC 183374187 b` | [MAST HLSP T16](https://archive.stsci.edu/hlsp/t16) |
| **AstroNet / AstroNet-Triage** (Shallue & Vanderburg 2018; Yu et al. 2019; Dattilo et al. 2019) | 1D CNNs on global & local phase-folded transit views | Discovered `Kepler-90 i`, `Kepler-80 g`, `K2-293 b`, `K2-294 b`, and triaged TESS FFI sectors | [GitHub](https://github.com/google-research/exoplanet-ml) |
| **TGLC** (Han & Brandt, `mast:HLSP/tglc`) | Gaia DR3 prior PSF/PRF deblended FFI light curves | High-precision deblended FFI light curves enabling faint-star transit searches | [MAST HLSP TGLC](https://archive.stsci.edu/hlsp/tglc) |

### 2.2 Citizen Science & Community Open-Source Pipelines
| Project / Author | Methodology & Tools | Key Contributions | Links |
| :--- | :--- | :--- | :--- |
| **Planet Hunters TESS (PHT)** (Nora L. Eisner et al., Zooniverse) | Crowd-sourced visual inspection of TESS light curves + `LATTE` Python vetting suite | Discovered `TOI-1338 b` (circumbinary), `TOI-813 b`, `HD 152843 b/c`, `TOI-4633 c` ("Percival"), `TOI-791 b/c`, compact triple `TIC 290061484` | [Zooniverse](https://www.zooniverse.org/projects/nora-dot-eisner/planet-hunters-tess) · [LATTE](https://github.com/noraeisner/LATTE) |
| **SHERLOCK Pipeline** (F. J. Pozuelos, M. Dévora-Pajares et al.) | End-to-end `Lightkurve` + `Wōtan` multi-detrend + `TLS` + `TRICERATOPS` + `Allesfitter` | Discovered 3-planet binary system `TOI-2267` and dozens of M-dwarf CTOIs | [GitHub](https://github.com/SHERLOCK-pipeline/sherlockpipe) |
| **TRICERATOPS** (Steven Giacalone et al.) | Bayesian False Positive Probability (FPP) calculator across 18 astrophysical scenarios | Standard statistical validation tool for TESS candidates (`FPP < 0.015`) | [GitHub](https://github.com/stevengiacalone/triceratops) |
| **TESS-Centroid_vetting** (Rafael Rodrigues, Sam Lee, Michelle Kunimoto) | PRF difference-image centroid offset vetting on TESS Target Pixel Files | Open-source Python package replicating SPOC DV centroid offset checks | [GitHub](https://github.com/exo-pt/TESS-Centroid_vetting) |
| **PH_TESS_I_LightCurveViewer** (Sam Lee / `orionlee`) | Interactive viewer & userscripts for TESS TCEs, CTOIs, and multi-sector stitching | Used daily by Planet Hunters TESS vetters to inspect ExoFOP candidates | [GitHub](https://github.com/orionlee/PH_TESS_I_LightCurveViewer) |

### 2.3 Recent Independent Developer & Agentic Pipelines on GitHub (2025–2026)
- **[`kzhu2099/Exoplanets`](https://github.com/kzhu2099/Exoplanets)** (*Kevin Zhu*, 2025–2026): Multi-sector TESS BLS analyzer (`FinnyExoplanetAnalyzer.py`), `batman` limb-darkened fitting, `TRICERATOPS` vetting, `ExoRM` mass estimation, and CTOI preparation across Sectors 60–89.
- **[`HashirHussain12/TESS-Exoplanet-Finder`](https://github.com/HashirHussain12/TESS-Exoplanet-Finder)** (*Muhammad Hashir Hussain*, Sept 2026): Automated batch pipeline (`tess_exoplanet_hunter.py`) and single-star deep dive (`tess_deep_dive.py`) combining upward-only MAD flare clipping, `astropy` BLS period narrowing, `Transit Least Squares (TLS)`, and multi-sector coherence vetting (e.g., rejecting `TIC 270415707` as starspot modulation).
- **[`thekayrasari/exoplanet-detector`](https://github.com/thekayrasari/exoplanet-detector)** (*Kayra Sari*, Sept 2026): AFK batch scanner querying real MAST TESS targets, running 2-pass multi-planet BLS masking, odd/even depth tests, and automatic ExoFOP `KNOWN_TOI` vs. `NEW_UNREPORTED_CANDIDATE` tagging.
- **[`3equalspi/TESS-Exoplanet-Search`](https://github.com/3equalspi/TESS-Exoplanet-Search)** (Sept 2026): SPOC light-curve TLS/BLS pipeline with per-transit coherence rejection of stellar variability.

---

## 3. Master Catalog Counts Indexed in This Repository

Generated by [`scripts/sync_catalogs.py`](../scripts/sync_catalogs.py) and stored in [`catalog/catalog_summary.json`](../catalog/catalog_summary.json):

| Catalog Source | Total Entries | Indexed in `known_tics.json.gz` |
| :--- | :--- | :--- |
| **NASA Exoplanet Archive Confirmed Planets (`pscomppars`)** | `6,445` | `6,138` (with TIC ID) |
| **Official NASA TESS Objects of Interest (`toi`)** | `8,148` (`814 CP`, `606 KP`, `4,824 PC`, `488 APC`, `1,314 FP`, `100 FA`) | `8,148` |
| **ExoFOP-TESS Community TOIs (`ctoi`)** | `5,138` | `5,138` |
| **Curated External Literature / AI Candidates** | `4` (`TIC 4206066.01/.02`, `TIC 183374187 b`, `TIC 290061484`) | `4` |
| **Total Unique Known TIC Stars Indexed** | — | **`15,025` unique TIC IDs** |
