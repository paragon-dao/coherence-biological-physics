# 9. Experimental Roadmap

This section converts CMH into concrete, reproducible science: a staged program of experiments, instrumentation, analysis pipelines, ethical safeguards, and success criteria that will allow the community to validate or falsify the hypothesis. The plan is modular so teams from different disciplines can run parts in parallel and share data.

## Guiding Principles (applies to every experiment)

- Pre-registration of protocols and analysis plans (to avoid p-hacking).
- Blinded analysis where possible (data analysts blind to condition).
- Synchronized timestamps using GPS-disciplined clocks or atomic-clock references for multi-site correlation.
- High signal-to-noise first: build instrumentation and controls before large-scale studies.
- Open data & code (when ethically feasible) for independent reanalysis.
- IRB / ethics approval required for human subjects; special approvals for temperature manipulations and sleep protocols.
- Safety bounds: temperature manipulations limited to medically safe windows (e.g., ±0.2–0.5 °C) and with medical monitoring.
- Replication as requirement: any positive result must replicate in an independent lab before claims.

## Overview of Phases (modular, non-temporal labels)

### Phase A — Bench & In Vitro (feasibility / mechanism)

**Goals:** demonstrate that marrow-analog fluids in resonant cavities support long-lived, temperature-sensitive waves and electromechanical transduction.

**Experiments:**

1. **Marrow analog cavity tests**
   - Build resonant cavities approximating bone geometry. Fill with marrow-analog fluids (viscous lipid suspensions, particulate components).
   - Periodic forcing at cardiac-like frequencies (0.5–3 Hz) and measure mechanical (accelerometers/laser vibrometry), electrical (microelectrodes), and magnetic (near-field sensors) responses.
   - Vary temperature in small steps (0.1 °C) to map decoherence thresholds.

2. **Electro-mechano coupling tests**
   - Measure piezoelectric response of bone samples / bone analogs with marrow fluid under forcing.
   - Test magnetohydrodynamic coupling by using ionic content and measuring induced magnetic fields.

**Instrumentation:**

Precision mechanical shakers; laser Doppler vibrometer; micro-electrodes; sensitive magnetometers (SQUID for best sensitivity in lab) or shielded OPMs; temperature bath with ±0.05 °C control.

**Outcome metrics:**

Q-factor vs temperature curves; decay times of standing modes; thresholds where coherence collapses.

### Phase B — Single-Site Human Pilot (proof-of-principle)

**Goals:** detect marrow-adjacent signatures phase-locked to cardiac rhythms and sensitive to small temperature shifts; validate noninvasive measurement approaches.

**Participants:**

N ≈ 20–40 healthy adult volunteers (range includes well-trained meditators and controls). Use a within-subject design.

**Measurements:**

- Core temp (ingestible thermometer or continuous skin+calibrated core estimate).
- ECG/HRV (high-resolution).
- Localized magnetometry near marrow sites (femur/tibia/sternum) using OPMs or SQUIDs in a magnetically shielded room (MSR).
- High-resolution ultrasound elastography of marrow cavities.
- Whole-body accelerometers to capture mechanical modes.
- EEG for concurrent brain state.
- Environmental monitoring (ELF/ULF antennas, geomagnetic indices, Schumann monitoring).

**Protocols:**

Rest baseline → sleep nap protocol (monitored) → small, medically safe thermal modulation (e.g., warming/cooling blanket to target ±0.2–0.5 °C under supervision) → meditation/relaxation tasks → controlled EM noise injection (safe levels) as decoherence test.

**Data analysis:**

- Time–frequency analyses (wavelets, multitaper) for marrow-adjacent sensors.
- Coherence and phase-locking value (PLV) between ECG and marrow signals.
- Temperature-dependent effect sizes via mixed-effects models (subject random effects).
- Nonparametric permutation tests for significance.
- Pre-specified effect-size target and power calculation guidance (expect small effects — plan analyses accordingly; use conservative alpha, e.g., 0.01, and correct for multiple comparisons).

**Success criteria:**

- Replicable phase-locked marrow–ECG coherence with temperature dependence (statistically significant decline when temp shifts exceed threshold).
- Sleep increases coherence metrics compared to wake baseline.

### Phase C — Multi-Site Synchronized Sleep Study (correlation tests)

**Goals:** test cross-person phase correlations and lunar/geomagnetic modulation.

**Design:**

- 4–8 geographically dispersed sites (urban & rural) with synchronized instrumentation and GPS time stamping.
- Participant groups per site: N ≈ 20; overall sample size large enough for small effect detection (target dozens–hundreds total depending on power calc).

**Measurements:**

- Same sensor array as Phase B at each site (ECG, localized magnetometers, accelerometers, ingestible or continuous core temp sensors, EEG).
- Site-level ELF/ULF and Schumann resonance receivers.
- Ground truth environmental indices (geomagnetic Kp, seismic activity).

**Protocol:**

Simultaneous multi-night sleep recordings across lunar phases (pre-registered windows), blind to analysts.
Include control nights with deliberate EM noise injection at some sites (careful ethics).

**Analysis:**

- Cross-correlation, coherence, and time-lagged analyses between participants across sites.
- Cluster-based permutation tests to establish significance across populations.
- Tests for alignment with lunar phase, perigee/apogee, and geomagnetic quiet windows (account for covariates).

**Success criteria:**

Small but statistically significant cross-site correlations aligned with specific lunar/geophysical windows, robust to controls and replication across sites.

### Phase D — Large-Scale Field Studies & Group Coherence Events

**Goals:** detect population-level modulation of ELF/ULF signals during organized coherence events and test bidirectionality.

**Design:**

- Large meditation/ritual/coherence groups (hundreds to thousands) with local sensor arrays and remote monitoring of ELF/ULF stations.
- Pre/post-event baseline recordings.

**Measurements:**

Ambient ELF/ULF antennas, magnetometers, distributed wearable ECG/accelerometers on subset of participants, continuous environmental monitoring.

**Analysis:**

- Compare ELF/ULF spectral content and Schumann harmonic amplitude during events vs matched control periods using time–frequency and interference pattern analyses.
- Bayesian hierarchical models to relate participant-level coherence to global field metrics.

**Success criteria:**

Detectable, reproducible ELF/ULF modulations during high-coherence events beyond chance and environmental confounds.

### Phase E — Space / Gravity Variation Tests (extreme test)

**Goals:** evaluate gravity dependence (astronauts, parabolic flights, centrifuge) for coherence signatures.

**Design:**

- Small-N astronaut studies (subject to mission constraints) and/or parabolic flight tests with bone-adjacent sensors.
- In vitro marrow-analog tests under altered gravity (centrifuge or clinostat).

**Measurements & Outcomes:**

Compare onboard marrow-coherence proxies with Earth-based baselines and look for predicted modulation/decrease in coupling.

## Instrumentation & Sensitivity Notes (practical guidance)

- **Magnetometers:** SQUIDs offer fT/√Hz sensitivity (best for lab); modern OPMs (SERF or spin-exchange) can reach low-fT–10 fT/√Hz and operate without cryogenics—useful for field studies.
- **Temperature control & sensors:** ingestible core thermometers or high-precision skin-to-core calibrated sensors; environmental temp logged with ±0.05 °C.
- **Accelerometers / vibrometers:** high dynamic range for sub-Hz to tens of Hz.
- **Ultrasound elastography & MRI/MRS:** for marrow rheology and composition mapping.
- **ELF/ULF receivers:** broadband antennas and preamplifiers; calibrate for Schumann band.
- **Timing:** GPS-disciplined clocks with sub-microsecond resolution for cross-site fusion.

(Exact instrument models and procurement depend on budgets and lab access; team engineers should specify exact sensor models and shielding.)

## Data Analysis & Statistical Methods (standardized pipeline)

- **Preprocessing:** artifact rejection, band-pass filtering aligned to target bands (sub-Hz to ~30 Hz), notch filters for mains hum, movement artifact removal.
- **Time–frequency:** wavelet transforms, multitaper spectral estimation.
- **Coherence metrics:** coherence spectrum, phase-locking value (PLV), imaginary part of coherence to avoid volume conduction artifacts.
- **Causality / directionality:** time-lagged cross-correlation, transfer entropy, Granger causality for directed interactions (use nonparametric variants).
- **Significance:** permutation testing, cluster-based correction, control for multiple comparisons (FDR or family-wise error).
- **Effect-size focus:** report Cohen's d, confidence intervals, Bayesian credible intervals; pre-specify smallest effect size of interest.
- **Replication tests:** independent-holdout datasets; meta-analytic combination across sites.

## Controls & Confounds (must be addressed)

- **Environmental EM noise:** measure and control (shielded rooms, baseline subtraction).
- **Shared external cues:** time-of-day, social media events, broadcast signals — log and control.
- **Movement & muscle artifacts:** include motion sensors and EMG to regress out contamination.
- **Physiological covariates:** respiration, body position, medication, caffeine, prior sleep — record and model.
- **Expectation/placebo effects:** use blinded analysts and where feasible participant blinding to study hypotheses.

## Ethics, Safety & Human-Subject Protections

- IRB approvals required for all human experiments.
- Informed consent documents must explain novel nature, risks of small temperature changes, sleep protocols, and recording modalities.
- Medical monitoring for any temperature modulation; emergency protocols in place.
- Privacy: strict de-identification, secure storage, and participant control over data sharing.
- Vulnerable populations: exclude or take special care (pregnant subjects, minors, severe medical conditions).
- Space / extreme environment studies require additional safety authorities and medical clearances.

## Success Criteria, Decision Rules, and Replication Thresholds

- **Phase A/B success:** reproducible, temperature-sensitive resonant modes in marrow analogs and measurable marrow-adjacent signatures in humans (p < 0.01, effect robust to artifact controls).
- **Phase C success:** cross-site correlations aligned to planetary cycles with pre-registered effect sizes, replication across at least two independent site networks.
- **Phase D/E success:** reproducible ELF/ULF modulation during group coherence events and gravity-dependent alterations.
- **Falsification:** failure to observe predicted temperature sensitivity, sleep amplification, and cross-site correlations in adequately powered, well-controlled studies will falsify CMH or force model revision.

## Data-Sharing / Community Practices

- Pre-registered protocols & data repositories (e.g., OSF, institutional repositories) with metadata standards.
- Standardized data formats and analysis notebooks (to enable reproducibility).
- Consortium-style collaborations for multi-site studies (shared SOPs, calibration standards, central analysis pipelines).
- Open challenge: release a curated dataset that independent teams analyze blind to the hypothesis for verification.

## Key Deliverables for the Author & Community (action-oriented)

- Publish Phase A results (bench validation) with raw data and analysis code.
- Publish Phase B pilot human findings with full methods and pre-registered analyses.
- Convene multi-disciplinary workshops to standardize instrumentation and protocols for Phase C.
- Seek partnerships with labs having SQUID/OPM facilities, sleep labs, and geophysics centers.
- Pursue ethical approvals and grant proposals to fund multi-site replication.

## Final Methodological Note

This roadmap is intentionally conservative and rigorous. CMH predicts small, delicate effects in noisy systems; detecting them requires meticulous instrumentation, stringent controls, and honest statistical practice. That is the only robust path to meaningful results that the broader scientific community will accept.





