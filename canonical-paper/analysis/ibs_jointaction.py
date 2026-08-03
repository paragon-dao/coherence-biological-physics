"""
The real test: does inter-brain coupling BREATHE, and does breathing track joint performance?

Dataset: OpenNeuro ds007471 "Joint agency EEG dataset" (Zhou, Zamm, Christensen, Rao, Loehr).
  32 pairs, musical joint-action. ONE 64-ch BrainVision file per pair (both partners on a single
  amplifier -> HARDWARE-SYNCED; channels suffixed _R/_L). 1000 Hz. CC0.
  Per-trial behaviour: MeanSynchronizationPerformance (coordination) & JointAgencyRatings.

Honest design: envelope coupling (theta, mu/alpha) on homologous scalp channels; sliding-window
inter-brain coupling r(t); breathing = std of r(t); tempo = slow spectral peak of r(t);
SURROGATE-PAIR NULL (R_i vs L_j, i!=j); PRIMARY test = does coupling/breathing correlate with the
pair's synchronization performance and joint-agency rating across pairs. Reported as-is.

Memory-safe: each pair is loaded once, resampled to 250 Hz, reduced to a 25 Hz band-envelope, then
freed -- so all 32 pairs' envelopes fit in ~1 GB and surrogate permutations are cheap.
"""
import numpy as np, os, glob, json, itertools, warnings
warnings.filterwarnings("ignore")
import mne, scipy.signal as sig
mne.set_log_level("ERROR")

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "ds007471")
OUT = os.path.dirname(os.path.abspath(__file__))
BANDS = {"theta": (4, 7), "mu_alpha": (8, 12)}
SF = 250.0                 # resample target
DECIM = 10                 # envelope -> 25 Hz
ESF = SF / DECIM           # 25 Hz envelope sample rate
WIN, STEP = int(12*ESF), int(1*ESF)   # 12 s window, 1 s step
CORE = ["F3","Fz","F4","FC1","FCz","FC2","C3","Cz","C4","CP1","CPz","CP2","P3","Pz","P4","O1","O2"]

def pair_envelopes(vhdr):
    raw = mne.io.read_raw_brainvision(vhdr, preload=True, verbose=False)
    raw.resample(SF, verbose=False)
    names = raw.ch_names
    env = {}   # (side, band, chan) -> float32 envelope @25Hz
    for side in ("R", "L"):
        picks = [f"{c}_{side}" for c in CORE if f"{c}_{side}" in names]
        if not picks:
            continue
        data = raw.get_data(picks=picks)   # (nch, N) @250
        for band_name, (lo, hi) in BANDS.items():
            b, a = sig.butter(4, [lo/(SF/2), hi/(SF/2)], btype="band")
            for ci, ch in enumerate(picks):
                base = ch[:-2]
                e = np.abs(sig.hilbert(sig.filtfilt(b, a, data[ci])))
                e = sig.decimate(e, DECIM, ftype="fir", zero_phase=True)
                env[(side, band_name, base)] = e.astype(np.float32)
    del raw
    return env

def coupling_curve(envA, envB, band):
    """R-side of envA vs L-side of envB (envA==envB for real pairs)."""
    chans = [c for (s, bn, c) in envA if s == "R" and bn == band]
    per = []
    for c in chans:
        ea = envA.get(("R", band, c)); eb = envB.get(("L", band, c))
        if ea is None or eb is None:
            continue
        n = min(len(ea), len(eb))
        rs = [np.corrcoef(ea[s:s+WIN], eb[s:s+WIN])[0,1]
              for s in range(0, n-WIN, STEP)
              if ea[s:s+WIN].std() > 1e-9 and eb[s:s+WIN].std() > 1e-9]
        if len(rs) > 6:
            per.append(np.array(rs))
    if not per:
        return None
    L = min(len(p) for p in per)
    return np.mean([p[:L] for p in per], axis=0)

def summarize(r):
    r = r[np.isfinite(r)]
    if len(r) < 8:
        return None
    rr = r - r.mean()
    f, P = sig.welch(rr, fs=ESF/STEP if False else 1.0, nperseg=min(len(rr), 64))
    slow = (f >= 0.01) & (f <= 0.10)
    return dict(mean_r=float(r.mean()), breathing=float(r.std()),
                tempo_power=float(P[slow].sum()/(P.sum()+1e-12)), npts=len(r))

def read_beh(path):
    import csv
    rows = list(csv.DictReader(open(path), delimiter="\t"))
    def col(name):
        v = []
        for r in rows:
            try: v.append(float(r[name]))
            except: pass
        return float(np.mean(v)) if v else np.nan
    return dict(sync_perf=col("MeanSynchronizationPerformance"),
                joint_agency=col("JointAgencyRatings"))

# ---------------------------------------------------------------- load all pairs (compact)
vhdrs = sorted(glob.glob(os.path.join(ROOT, "sub-*/eeg/*_eeg.vhdr")))
print(f"pairs found: {len(vhdrs)}", flush=True)
envs, behs = {}, {}
for i, v in enumerate(vhdrs):
    sub = os.path.basename(v).split("_")[0]
    try:
        envs[sub] = pair_envelopes(v)
        bp = glob.glob(os.path.join(ROOT, sub, "beh", "*_beh.tsv"))
        behs[sub] = read_beh(bp[0]) if bp else None
        print(f"  [{i+1}/{len(vhdrs)}] {sub} loaded", flush=True)
    except Exception as e:
        print(f"  [{i+1}] {sub} FAILED: {e}", flush=True)

# ---------------------------------------------------------------- analyze
allout = {}
for band in BANDS:
    real, surr = [], []
    for sub, env in envs.items():
        r = coupling_curve(env, env, band)
        s = summarize(r) if r is not None else None
        if s and behs.get(sub):
            s.update(sub=sub, **behs[sub]); real.append(s)
    subs = list(envs)
    for a, b in itertools.permutations(subs, 2):
        r = coupling_curve(envs[a], envs[b], band)
        s = summarize(r) if r is not None else None
        if s: surr.append(s)

    def arr(lst,k): return np.array([x[k] for x in lst], float)
    print("\n" + "="*66)
    print(f"BAND {band}   real pairs={len(real)}  surrogate={len(surr)}")
    print("="*66)
    for m in ["mean_r","breathing","tempo_power"]:
        rv, sv = arr(real,m), arr(surr,m)
        z = (rv.mean()-sv.mean())/(sv.std()+1e-12)
        print(f"  {m:12s} real={rv.mean():.4f}  surrogate={sv.mean():.4f}  z={z:+.2f}")
    print("  --- coupling/breathing vs pair OUTCOME (Pearson across pairs) ---")
    corrs={}
    for pred in ["mean_r","breathing","tempo_power"]:
        for outcome in ["sync_perf","joint_agency"]:
            x, y = arr(real,pred), arr(real,outcome)
            ok = np.isfinite(x)&np.isfinite(y)
            if ok.sum() > 4:
                rho = float(np.corrcoef(x[ok], y[ok])[0,1])
                corrs[f"{pred}~{outcome}"]=rho
                print(f"     {pred:12s} x {outcome:12s}: r = {rho:+.3f}  (n={ok.sum()})")
    allout[band]={"real":real,"surrogate_n":len(surr),"corrs":corrs}

with open(os.path.join(OUT,"jointaction_results.json"),"w") as f:
    json.dump(allout, f, indent=2)
print("\nwrote jointaction_results.json")
