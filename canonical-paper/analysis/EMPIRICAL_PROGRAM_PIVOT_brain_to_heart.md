# CMH empirical program pivot: stop measuring brain, measure the heart's wave
Written 2026-07-21. Corrects a real design error caught by Phil.

## The error (owned)
CMH says the substrate is the HEART -> MARROW -> BONE triad; the brain only
"interprets or modulates" (paper Section 7.3). Our first empirical work used
inter-brain EEG hyperscanning (ds007471, ds007822, Figshare) because that data
was on hand. That tests the WRONG ORGAN, in the WRONG STATE (awake task, not
sleep), at the WRONG DISTANCE (same room, not the nonlocal claim), with the
WRONG METRIC (coupling amplitude, when the only hint was rhythm). The null we
got says almost nothing about the actual hypothesis. Do not mine more EEG for
the marrow claim -- it is structurally incapable of reaching it.

## The right channel (and it is reachable + cheap)
The heart's mechanical wave -- the thing Phil means by "the wave inside the
heart chamber" -- is directly measurable non-invasively:
- SEISMOCARDIOGRAPHY (SCG): a MEMS accelerometer on the chest captures the
  chest-wall vibration the heart produces each beat. This IS the mechanical
  wave the heart launches into the body/skeleton (paper 5.2 mechanical
  coupling pathway).
- BALLISTOCARDIOGRAPHY (BCG): whole-body recoil from blood ejection; bed/force
  sensors. The body-scale version of the same wave.
Both live in the sub-Hz to few-Hz band CMH predicts (paper 5.6, 6.3).

## Open datasets to prototype on (the RIGHT organ)
Single-person heart-mechanical wave:
- CEBS (PhysioNet): 20 healthy volunteers, simultaneous ECG + respiration +
  SCG, supine. Cleanest starting set for the heart-wave pipeline.
- FOSTER / forcecardiography (Nature Sci Data 2025): 40 participants, SCG +
  phonocardiogram + ECG + respiration.
- SCG-RHC (PhysioNet): wearable SCG + right-heart-catheter pressure (ground
  truth intracardiac pressure alongside the surface wave).
- Valvular-heart-disease cardio-mechanical DB (Frontiers 2021).

Coupling on the heart channel, during SLEEP, between people (the honest analog
of what we tried with brains):
- Yoon et al. -- co-sleeping COUPLES, heart-rhythm synchrony during sleep,
  found bidirectional causal coupling. This is dyad + sleep + cardiac = exactly
  the condition CMH predicts is BEST.
- Global heart-rhythm synchronization study (Nature Sci Rep 2024): 104
  participants, 5 countries, 15-day continuous ambulatory heart rhythm --
  touches the long-range/distributed angle.
- Fetal-maternal cardiac dynamics (bilateral interaction) -- a within-body
  two-oscillator control case.
(Caveat: these were built to study cardiac HEALTH or HRV synchrony, mostly
interbeat-interval level, not the mechanical marrow-resonance signature. They
prototype the pipeline; the marrow-specific test likely needs our own
acquisition -- see below.)

## The DISCRIMINATING design point (do not skip)
Measuring the heart wave (SCG) is necessary but NOT sufficient for the marrow
claim. "The heart shakes the body" is trivially true and already known. CMH's
novel claim is that the marrow-bone cavity SUSTAINS A STANDING WAVE -- a
resonator, not just forced vibration. The test that separates the two:
- Record at MULTIPLE skeletal sites (sternum, tibia, patella, iliac crest),
  not just chest.
- Look for RESONANCE signatures: site-specific spectral peaks / high-Q modes /
  ring-down (decay) that outlast the cardiac forcing, not just a copy of the
  ECG rhythm.
- Test the predicted TEMPERATURE dependence (small safe core-temp shifts
  change viscosity -> should change the resonance) and SLEEP amplification.
Only site-specific resonance + temperature sensitivity distinguishes "marrow
cavity rings" from "accelerometer near a beating heart."

## The three layers (test at the right one)
1. HEART WAVE (single person): characterize SCG's sub-Hz-few-Hz structure,
   cardiac-cycle locking, and any resonance vs pure forcing. Reachable NOW on
   open data (CEBS).
2. COUPLING on the heart channel (dyad, sleep): phase-locking of two people's
   heart-mechanical rhythms during co-sleep. Reachable via couple datasets;
   the honest analog of the failed EEG test, on the right organ + state.
3. MARROW RESONATOR (the actual novel claim): multi-site bone accelerometry +
   temperature modulation + sleep; ultimately OPM magnetometry / ultrasound
   elastography of marrow cavities. Needs our own cheap acquisition (a few
   research MEMS accelerometers) or a lab. This is the expensive/vision leg the
   vehicles (ASAI/Paragon/raise) are meant to fund.

## Next step (design-first this time -- do NOT rush to available data again)
Phil's fork:
A. Prototype the HEART-WAVE pipeline on CEBS now (cheap, honest, builds the
   analysis we will reuse) -- answers "can we even see structured cardiac
   mechanical waves and any resonance in open data."
B. Go straight for the COUPLING-during-sleep question on couple cardiac data.
C. Spec our OWN minimal acquisition (2-4 MEMS accelerometers at bone sites,
   overnight, temperature logged) designed to CMH -- the first study actually
   built for the hypothesis rather than borrowed.
Recommendation: A first (it is this week's honest, reachable, reusable step),
then C (the first study we design rather than inherit), with B as the coupling
test once the single-person wave pipeline is trustworthy. Claims discipline
applies to every number before any external word.
