"""
CLOSE THE LOOP: does inter-brain coupling BREATHE, and does the breathing track
how well the two people actually performed together?

This reads the per-pair values already computed by ibs_jointaction.py (stored in
jointaction_results.json for all 31 hardware-synced ds007471 pairs) and runs the
PRIMARY across-pairs test that came back empty in the stored file. Nothing is
re-derived from raw here; these are the exact per-pair numbers the pipeline wrote.
Honest stats: Pearson AND Spearman, two-sided p, n, for both bands and both
outcomes. Reported as-is, whatever it says.
"""
import json, os, numpy as np
from scipy import stats

OUT = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(OUT, "jointaction_results.json")))

PREDS = ["mean_r", "breathing", "tempo_power"]
OUTCOMES = ["sync_perf", "joint_agency"]

def col(rows, k):
    return np.array([r.get(k, np.nan) for r in rows], float)

report = {}
for band in d:
    rows = d[band]["real"]
    n_all = len(rows)
    print("=" * 70)
    print(f"BAND {band}   (n = {n_all} hardware-synced real pairs)")
    print("=" * 70)
    report[band] = {"n": n_all, "results": {}}
    for pred in PREDS:
        for outc in OUTCOMES:
            x, y = col(rows, pred), col(rows, outc)
            ok = np.isfinite(x) & np.isfinite(y)
            n = int(ok.sum())
            if n < 5:
                print(f"  {pred:11s} x {outc:12s}: n={n} too few")
                continue
            xr, yr = x[ok], y[ok]
            pr, pp = stats.pearsonr(xr, yr)
            sr, sp = stats.spearmanr(xr, yr)
            flag = "  <-- p<.05" if pp < 0.05 or sp < 0.05 else ""
            print(f"  {pred:11s} x {outc:12s}: "
                  f"Pearson r={pr:+.3f} p={pp:.3f} | "
                  f"Spearman rho={sr:+.3f} p={sp:.3f}  (n={n}){flag}")
            report[band]["results"][f"{pred}~{outc}"] = dict(
                pearson_r=float(pr), pearson_p=float(pp),
                spearman_rho=float(sr), spearman_p=float(sp), n=n)
    print()

# The single anchor sentence the preprint hangs on: breathing ~ sync_perf, theta.
anchor = report.get("theta", {}).get("results", {}).get("breathing~sync_perf")
if anchor:
    print("-" * 70)
    print("ANCHOR (theta breathing vs synchronization performance):")
    print(f"  Pearson r = {anchor['pearson_r']:+.3f}, p = {anchor['pearson_p']:.3f}, "
          f"n = {anchor['n']}")
    print(f"  Spearman rho = {anchor['spearman_rho']:+.3f}, p = {anchor['spearman_p']:.3f}")
    print("-" * 70)

with open(os.path.join(OUT, "close_the_loop_results.json"), "w") as f:
    json.dump(report, f, indent=2)
print("wrote close_the_loop_results.json")
