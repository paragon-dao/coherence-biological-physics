"""
First honest test of the "coupling breathes" hypothesis on REAL interacting brains.

Dataset: Figshare 10.6084/m9.figshare.c.7062272 -- 16 dyads (8 face-to-face = Recording01,
8 online = Recording02), each dyad = P01,P02 recorded simultaneously. 4-electrode montage
(C3,C4 scalp + A1,A2 refs), 250 Hz. Task03/Task04 = the two ~10 min interaction tasks
(collaboration puzzle / competition dominoes). Task01/02 = short baselines.

Honest design:
  * Envelope-based inter-brain coupling (robust to the small cross-device timing offset;
    these two brains were NOT hardware-synced, so we do NOT trust ms phase-locking).
  * Mu/alpha band 8-12 Hz on C3/C4 (sensorimotor -- apt for a hands-on joint task).
  * Sliding-window coupling r(t); its temporal fluctuation = "breathing".
  * SURROGATE-PAIR NULL: same computation on non-interacting partners (P01 of dyad i vs
    P02 of dyad j!=i). Genuine coupling and genuine breathing must beat this null.
  * Nothing tuned to make the hypothesis win; we report whatever the data says.
"""
import numpy as np, scipy.io as sio, scipy.signal as sig, json, os, itertools

OUT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(OUT, "..", "data", "collab_compete_figshare", "EEG.mat")
SF = 250.0
BAND = (8.0, 12.0)          # mu/alpha
WIN = int(15 * SF)          # 15 s coupling window
STEP = int(1 * SF)          # 1 s step
SCALP = ["C3", "C4"]        # homologous inter-brain channels

def load():
    m = sio.loadmat(DATA, squeeze_me=True, struct_as_record=False)
    return m["EEG"]

def chan_data(task):
    """Return dict label->1D signal for the scalp channels, robust to channel order."""
    d = np.asarray(task.data, float)
    labs = [str(getattr(c, "labels", "")).strip() for c in np.atleast_1d(task.chanlocs)]
    out = {}
    for lab in SCALP:
        if lab in labs:
            out[lab] = d[labs.index(lab)]
    return out

def env(x):
    """Band-limited Hilbert amplitude envelope, with drift/line removed by the bandpass."""
    b, a = sig.butter(4, [BAND[0]/(SF/2), BAND[1]/(SF/2)], btype="band")
    xf = sig.filtfilt(b, a, x)
    e = np.abs(sig.hilbert(xf))
    # robust clip of gross artifact spikes (envelope only)
    hi = np.percentile(e, 99.5)
    return np.clip(e, 0, hi)

def coupling_timeseries(sig1, sig2):
    """Sliding-window Pearson r between two envelopes -> r(t)."""
    n = min(len(sig1), len(sig2))
    e1, e2 = env(sig1[:n]), env(sig2[:n])
    rs = []
    for s in range(0, n - WIN, STEP):
        a1 = e1[s:s+WIN]; a2 = e2[s:s+WIN]
        if a1.std() > 1e-9 and a2.std() > 1e-9:
            rs.append(np.corrcoef(a1, a2)[0, 1])
    return np.array(rs)

def dyad_coupling(pA, pB, task_field):
    """Average homologous-channel r(t) between two participants for one task."""
    tA = getattr(pA, task_field); tB = getattr(pB, task_field)
    cA, cB = chan_data(tA), chan_data(tB)
    curves = []
    for lab in SCALP:
        if lab in cA and lab in cB:
            r = coupling_timeseries(cA[lab], cB[lab])
            if len(r) > 5:
                curves.append(r)
    if not curves:
        return None
    L = min(len(c) for c in curves)
    return np.mean([c[:L] for c in curves], axis=0)

def summarize(r):
    """Coupling level + 'breathing' (how much it rises and falls) of an r(t) curve."""
    r = r[np.isfinite(r)]
    if len(r) < 6:
        return None
    mean_r = float(np.mean(r))
    breathing = float(np.std(r))                       # temporal fluctuation of coupling
    # slow rhythmicity: fraction of r(t) fluctuation power in a slow band (0.01-0.08 Hz ~ 12-100 s)
    rr = r - r.mean()
    f, P = sig.welch(rr, fs=1.0/(STEP/SF), nperseg=min(len(rr), 64))
    slow = (f >= 0.01) & (f <= 0.08)
    rhythmicity = float(P[slow].sum() / (P.sum() + 1e-12))
    return dict(mean_r=mean_r, breathing=breathing, rhythmicity=rhythmicity, npts=len(r))

# ---------------------------------------------------------------- run
EEG = load()
recs = ["Recording01", "Recording02"]   # face-to-face, online
INTERACTION = ["_Task03", "_Task04"]     # resolved to task field names below

results = {"real": [], "surrogate": []}
for rec in recs:
    R = getattr(EEG, rec)
    dyads = R._fieldnames
    # resolve actual task field names (they are prefixed, e.g. ALAS_Recording01_P01_Dyad01_Task03)
    for dy in dyads:
        D = getattr(R, dy)
        P1, P2 = getattr(D, "P01"), getattr(D, "P02")
        for ti, tsuffix in enumerate(["Task03", "Task04"]):
            f1 = [f for f in P1._fieldnames if f.endswith(tsuffix)]
            f2 = [f for f in P2._fieldnames if f.endswith(tsuffix)]
            if not f1 or not f2:
                continue
            # partner fields differ in name (encode P01/P02); use each own field
            tA = getattr(P1, f1[0]); tB = getattr(P2, f2[0])
            cA, cB = chan_data(tA), chan_data(tB)
            curves = []
            for lab in SCALP:
                if lab in cA and lab in cB:
                    rr = coupling_timeseries(cA[lab], cB[lab])
                    if len(rr) > 5: curves.append(rr)
            if not curves: continue
            L = min(len(c) for c in curves)
            rcurve = np.mean([c[:L] for c in curves], axis=0)
            s = summarize(rcurve)
            if s:
                s.update(rec=rec, dyad=dy, task=tsuffix)
                results["real"].append(s)

# surrogate: P01 of a dyad vs P02 of every OTHER dyad, same rec+task
for rec in recs:
    R = getattr(EEG, rec)
    dyads = R._fieldnames
    for tsuffix in ["Task03", "Task04"]:
        for da, db in itertools.permutations(dyads, 2):
            P1 = getattr(getattr(R, da), "P01")
            P2 = getattr(getattr(R, db), "P02")
            f1 = [f for f in P1._fieldnames if f.endswith(tsuffix)]
            f2 = [f for f in P2._fieldnames if f.endswith(tsuffix)]
            if not f1 or not f2: continue
            cA, cB = chan_data(getattr(P1, f1[0])), chan_data(getattr(P2, f2[0]))
            curves = []
            for lab in SCALP:
                if lab in cA and lab in cB:
                    rr = coupling_timeseries(cA[lab], cB[lab])
                    if len(rr) > 5: curves.append(rr)
            if not curves: continue
            L = min(len(c) for c in curves)
            s = summarize(np.mean([c[:L] for c in curves], axis=0))
            if s:
                s.update(rec=rec, pair=f"{da}P01-{db}P02", task=tsuffix)
                results["surrogate"].append(s)

def arr(lst, k): return np.array([d[k] for d in lst], float)

real, surr = results["real"], results["surrogate"]
print("="*68)
print(f"REAL interacting dyad-tasks: {len(real)}   |   SURROGATE non-partner pairings: {len(surr)}")
print("="*68)
for metric in ["mean_r", "breathing", "rhythmicity"]:
    rv, sv = arr(real, metric), arr(surr, metric)
    # z of real mean vs surrogate distribution
    z = (rv.mean() - sv.mean()) / (sv.std() + 1e-12)
    print(f"\n{metric}:")
    print(f"   REAL       mean={rv.mean():.4f}  sd={rv.std():.4f}  (n={len(rv)})")
    print(f"   SURROGATE  mean={sv.mean():.4f}  sd={sv.std():.4f}  (n={len(sv)})")
    print(f"   real vs surrogate-null z = {z:+.2f}")

# collaboration vs competition (Task03 vs Task04) on real dyads
print("\n" + "-"*68)
print("Task03 vs Task04 (interaction-type contrast), REAL dyads:")
for metric in ["mean_r", "breathing", "rhythmicity"]:
    t3 = arr([d for d in real if d["task"]=="Task03"], metric)
    t4 = arr([d for d in real if d["task"]=="Task04"], metric)
    print(f"   {metric:12s}  Task03={t3.mean():.4f}   Task04={t4.mean():.4f}   diff={t3.mean()-t4.mean():+.4f}")

with open(os.path.join(OUT, "ibs_results.json"), "w") as f:
    json.dump({"real": real, "surrogate": surr}, f, indent=2)
print("\nwrote ibs_results.json")
