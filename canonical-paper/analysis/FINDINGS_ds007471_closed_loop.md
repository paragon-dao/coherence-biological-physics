# Closed-loop finding: ds007471 (Joint-Agency EEG, 31 hardware-synced pairs)
Computed 2026-07-21. Question: does inter-brain coupling BREATHE, and does the
breathing track how well the two people performed together? Reported as-is.

## Provenance / integrity note
The primary across-pairs correlation was missing from the stored
jointaction_results.json ("corrs" was an empty dict) even though every per-pair
value it needs (mean_r, breathing, tempo_power, sync_perf, joint_agency for all
31 pairs) was present and healthy (real variance in each; sync_perf 0.10-0.73,
breathing 0.093-0.153). Recomputing the correlation from those exact stored
per-pair values (close_the_loop.py -> close_the_loop_results.json) produces the
result cleanly. So the data was never the problem; only the final correlation
step failed to persist in the original run. This is arithmetic on the pipeline's
own outputs, not a re-derivation. The separate coupling-EXISTS-vs-surrogate z
is NOT re-verified here (it needs the raw re-run; surrogate values were not
stored, only their count n=930).

## The primary test: breathing amplitude vs performance -- NULL
Breathing = std of the sliding-window inter-brain coupling curve r(t).
- theta  breathing x sync_perf   : Pearson r = -0.184, p = 0.322 (n=31);
                                    Spearman rho = -0.210, p = 0.257
- theta  breathing x joint_agency: r = -0.039, p = 0.836
- mu/alpha breathing x sync_perf : r = -0.090, p = 0.630
- mu/alpha breathing x joint_agency: r = +0.099, p = 0.598
On this hardware-synced dataset, the AMPLITUDE of the tide (how much the
coupling waxes and wanes) does NOT predict how well the pair performed, in
either band, on either outcome. Signs are mixed/slightly negative. Clean null.

## The one lead (does NOT survive discipline)
- theta tempo_power x sync_perf: Pearson r = +0.375, p = 0.038 (n=31)
  BUT Spearman rho = +0.257, p = 0.163 (not significant, not robust).
tempo_power = fraction of r(t)'s spectral power in the slow 0.01-0.10 Hz band,
i.e. "does the coupling wax/wane at a slow, tide-like RHYTHM." This is the only
one of 12 tests under p=0.05. With 12 comparisons, ~0.6 false positives are
expected by chance; Bonferroni threshold is 0.0042. It fails correction, and
the Pearson/Spearman split says a few influential pairs drive it. Classify as a
LEAD to pre-register and retest on independent data, NOT a finding.

## Honest reading
1. The pre-registered-style primary claim (the tide's amplitude tracks joint
   performance) is not supported here. On the good data, breathing amplitude
   carries no performance signal.
2. There is a weak, non-robust hint that the RHYTHM (slow tempo concentration)
   of the coupling, not its amplitude, may relate to synchronization. It is a
   hypothesis for the next dataset, nothing more.
3. This does not touch whether coupling EXISTS above surrogate (the Figshare
   probe showed z~+14 for existence; that leg is separate and still stands for
   existence, modest for breathing). mean_r here is small (~0.03), so even the
   existence claim on THIS set should be re-confirmed against its surrogate
   (n=930 stored count) in a raw re-run before any external statement.

## What this means for CMH
The theory explicitly said it can absorb a null: this narrows the claim. The
honest Volume-I position is "inter-brain coupling exists; its tide-like
amplitude does not by itself predict joint outcome in musical joint-action; a
slow-rhythm signature is a lead worth a pre-registered test." That is a
publishable, honest beachhead sentence -- not a hero result, a true one.

## Next steps (in order)
1. Raw re-run of ibs_jointaction.py to (a) reproduce these per-pair values and
   (b) recover the coupling-vs-surrogate z for existence on this set. Fix the
   corrs-persistence gap while there.
2. Pre-register the tempo_power ~ sync_perf lead; test on ds007764 (DUET, 64ch
   French conversation -- request access) as independent confirmation.
3. Do NOT let the tempo hint into any external doc until it survives correction
   on independent data (claims discipline).
