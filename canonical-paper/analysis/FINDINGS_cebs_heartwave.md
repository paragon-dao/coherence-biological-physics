# CEBS Layer-1 finding: the heart's mechanical wave (20 basal-rest subjects)
Computed 2026-07-21. CEBS (PhysioNet cebsdb 1.0.0), chest seismocardiogram +
ECG + respiration @ 5000 Hz. Pipeline: analysis/cebs_heartwave.py. Reported as-is.
This is the RIGHT organ (heart, mechanical) after the brain-EEG detour.

## What was tested (Layer 1 of the program pivot)
n = 20 basal-rest subjects, first 180 s each. Beat-locked SCG (R-peaks from ECG
via gqrs), ensemble template, spectral structure, post-systolic damped-sine fit
(ring-down / Q), and respiration-vs-beat-amplitude coupling. Single chest site,
supine, awake -- establishes the METHOD; cannot isolate marrow resonance (that
needs multi-site bone, Layer 3).

## Results (honest)
Q1 REPRODUCIBLE BEAT-LOCKED WAVE -- ROBUST.
  Beat-to-beat correlation to the subject's own ensemble template: mean r = 0.909
  (sd 0.033); ALL 20/20 subjects above 0.80. The heart launches a structured,
  highly repeatable mechanical wave into the body. Method works; phenomenon solid.
Q2 SPECTRAL: mean template-SNR ~5.2; mean 6.8% of 0-60 Hz power in the 0.5-4 Hz
  band. Cardiac-mechanical energy is broadband with the expected low-frequency
  component; not dominated by the sub-Hz-few-Hz band alone.
Q3 RING-DOWN (the discriminating precursor) -- PRESENT BUT NOT UNIVERSAL.
  A clean post-systolic damped-sinusoid fit (r2 > 0.6) appears in only 8/20
  subjects; Q scatters 1.2-15.1 at 9-13 Hz. The striking Q~15 in subject b001 was
  the HIGH END, not typical. So there is genuine resonant ring-down structure in a
  minority of people, but no universal high-Q resonance on chest SCG. A lead, not
  a finding.
Q5 RESPIRATORY MODULATION -- PRESENT BUT VARIABLE.
  |r| > 0.4 between per-beat SCG amplitude and respiration phase in 8/20 subjects,
  mixed sign. Real in some, absent/negative in others.

## Reading
- The reproducible cardiac mechanical wave is established and robust -- the
  pipeline is trustworthy and reusable, and the heart-wave phenomenon is real.
- The resonance/ring-down is the CMH-relevant precursor, and running n=20 (not
  celebrating n=1) correctly demoted it to "present in a minority, variable." This
  is exactly the NECESSARY-BUT-NOT-SUFFICIENT precursor: chest SCG cannot separate
  "marrow-bone cavity rings" from "chest wall / heart sounds," so a variable
  minority ring is what we'd expect either way. It MOTIVATES, does not confirm, the
  multi-site bone rig (Layer 3).
- No overclaim survived contact with the full dataset. Good.

## Caveats
Single chest site; supine; awake; first 180 s; ring-down Q from a single-window
damped-sine fit (b018 gave Q=55.7 at r2=0.25 -- a garbage fit, correctly excluded
by the r2>0.6 gate). Music/post state-comparison pending full download.

## Next
1. STATE COMPARISON (this dataset): does music-listening vs basal vs post move the
   wave (amplitude, spectrum, ring, resp-coupling)? Needs the m/p records
   downloaded; run with the completeness guard.
2. REPLICATION (the real gate before any preprint): same pipeline on FOSTER (40)
   and SCG-RHC. Convergence across independent SCG datasets is required.
3. Then, and only then, the modest bioRxiv methods/precursor preprint -- NOT
   "CMH validated." 4-agent claims panel gates every number first.
