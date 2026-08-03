"""
CEBS Layer-1: characterize the heart's mechanical wave (seismocardiogram).
The RIGHT organ this time -- heart, not brain. Honest, reproducible, reported as-is.

Questions (Layer 1 of EMPIRICAL_PROGRAM_PIVOT_brain_to_heart.md):
  Q1 Is there a REPRODUCIBLE beat-locked mechanical wave? (ensemble average + beat-to-beat r)
  Q2 What is its spectral structure? (PSD; where is the energy vs CMH's sub-Hz-few-Hz claim)
  Q3 Does it RING? (post-systolic damped-sinusoid fit -> frequency + Q)  <- the discriminating test
  Q4 Does inner STATE modulate it? (basal rest vs music-listening vs post)
  Q5 Does it breathe with REAL respiration? (beat-amplitude vs respiration phase)

Data: CEBS (PhysioNet cebsdb 1.0.0). 20 subjects x {b=basal, m=music, p=post}.
Channels: ECG I, ECG II, RESP, SCG @ 5000 Hz. Reads local data/cebsdb if present,
else streams via wfdb pn_dir. Chest SCG is single-site -> establishes METHOD;
the marrow-resonance claim still needs multi-site bone (Layer 3).
"""
import os, json, numpy as np, warnings
warnings.filterwarnings("ignore")
import wfdb
from wfdb import processing
from scipy import signal as sig
from scipy.optimize import curve_fit

HERE = os.path.dirname(os.path.abspath(__file__))
LOCAL = os.path.join(HERE, "..", "data", "cebsdb")
FS = 5000
COND = {"b": "basal_rest", "m": "music", "p": "post_music"}

def is_complete(rec):
    """True only if the local .dat is fully downloaded (size matches header)."""
    hea, dat = os.path.join(LOCAL, rec + ".hea"), os.path.join(LOCAL, rec + ".dat")
    if not (os.path.exists(hea) and os.path.exists(dat)):
        return False
    try:
        parts = open(hea).readline().split()
        nsig, nsamp = int(parts[1]), int(parts[3])
        return os.path.getsize(dat) >= nsig * nsamp * 2  # 16-bit samples
    except Exception:
        return False

def load(rec, sampto=None):
    p = os.path.join(LOCAL, rec)
    if os.path.exists(p + ".hea") and os.path.exists(p + ".dat"):
        r = wfdb.rdrecord(p, sampto=sampto)
    else:
        r = wfdb.rdrecord(rec, pn_dir="cebsdb/1.0.0", sampto=sampto)
    ch = {n: i for i, n in enumerate(r.sig_name)}
    return r.p_signal[:, ch["II"]], r.p_signal[:, ch["RESP"]], r.p_signal[:, ch["SCG"]]

def rpeaks(ecg):
    x = np.nan_to_num(ecg)
    q = np.array([])
    try:
        q = np.asarray(processing.gqrs_detect(x, fs=FS))
    except Exception:
        q = np.array([])
    if len(q) < 20:  # fallback: bandpass envelope peaks
        b, a = sig.butter(2, [8/(FS/2), 20/(FS/2)], "band")
        f = np.abs(sig.hilbert(sig.filtfilt(b, a, x)))
        q, _ = sig.find_peaks(f, distance=int(0.4*FS), height=np.nanstd(f)*2)
        q = np.asarray(q)
    return q

def bandpass(x, lo, hi):
    # sos form: numerically stable even for very low cutoffs (resp band) at fs=5000
    sos = sig.butter(4, [lo/(FS/2), hi/(FS/2)], "band", output="sos")
    return sig.sosfiltfilt(sos, np.nan_to_num(x))

def beat_matrix(scg_bp, R, pre=0.10, post=0.60):
    a, bwin = int(pre*FS), int(post*FS)
    segs = [scg_bp[r-a:r+bwin] for r in R if r-a >= 0 and r+bwin < len(scg_bp)]
    return np.array(segs) if segs else np.empty((0, a+bwin))

def damped_sine(t, A, tau, f, phi, c):
    return A*np.exp(-t/tau)*np.cos(2*np.pi*f*t+phi)+c

def analyze(rec, sampto):
    ecg, resp, scg = load(rec, sampto=sampto)
    R = rpeaks(ecg)
    if len(R) < 20:
        return None
    hr = FS/np.median(np.diff(R))*60.0

    # Q1 reproducible beat-locked wave (SCG in the mechanical-complex band 8-45 Hz)
    scg_c = bandpass(scg, 8, 45)
    M = beat_matrix(scg_c, R)
    if len(M) < 15:
        return None
    ens = M.mean(0)
    # beat-to-beat reproducibility = mean corr of each beat to the ensemble
    rs = [np.corrcoef(m, ens)[0, 1] for m in M if m.std() > 1e-9]
    repro = float(np.nanmean(rs))
    # signal energy explained by the reproducible template vs residual
    tvar, rvar = ens.var(), (M - ens).var()
    snr_template = float(tvar / (rvar + 1e-12))

    # Q2 spectral structure of the raw SCG (0-60 Hz)
    f, P = sig.welch(np.nan_to_num(scg), fs=FS, nperseg=int(10*FS))
    band = f <= 60
    fpk = float(f[band][1:][np.argmax(P[band][1:])])
    # fraction of 0-60Hz power in CMH's sub-Hz-to-few-Hz window (0.5-4 Hz)
    lowband = (f >= 0.5) & (f <= 4.0)
    frac_low = float(P[lowband].sum() / (P[band].sum() + 1e-12))

    # Q3 does it RING? fit damped sinusoid to the post-systolic tail of the ensemble
    a = int(0.10*FS)
    tail = ens[a+int(0.12*FS): a+int(0.45*FS)]  # ~120-450 ms after R
    t = np.arange(len(tail))/FS
    ring = None
    try:
        p0 = [tail.std(), 0.05, 20.0, 0.0, 0.0]
        popt, _ = curve_fit(damped_sine, t, tail, p0=p0, maxfev=8000,
                            bounds=([0,1e-3,3,-np.pi,-abs(tail).max()],
                                    [abs(tail).max()*5,1.0,60,np.pi,abs(tail).max()]))
        A, tau, fr, phi, c = popt
        Q = float(np.pi*fr*tau)
        fit = damped_sine(t, *popt)
        r2 = 1 - np.sum((tail-fit)**2)/(np.sum((tail-tail.mean())**2)+1e-12)
        ring = dict(ring_freq_hz=float(fr), tau_s=float(tau), Q=Q, fit_r2=float(r2))
    except Exception:
        ring = None

    # Q5 respiratory modulation of beat amplitude (real breathing)
    ramp = M.std(1)  # per-beat SCG amplitude
    Rc = np.array([r for r in R if r-a >= 0 and r+int(0.60*FS) < len(scg_c)])[:len(ramp)]
    resp_bp = bandpass(resp, 0.1, 0.5)
    resp_at_beat = resp_bp[Rc]
    ok = np.isfinite(ramp) & np.isfinite(resp_at_beat)
    resp_mod = float(np.corrcoef(ramp[ok], resp_at_beat[ok])[0, 1]) if ok.sum() > 10 else np.nan

    return dict(rec=rec, cond=COND[rec[0]], n_beats=int(len(M)), hr_bpm=float(hr),
                reproducibility=repro, template_snr=snr_template,
                scg_peak_hz=fpk, frac_power_0p5_4hz=frac_low,
                ring=ring, resp_mod_r=resp_mod, ensemble=ens.tolist())

if __name__ == "__main__":
    import sys
    SAMPTO = int(180*FS)          # first 180 s of each record (enough beats; keeps music tractable)
    subs = [f"{i:03d}" for i in range(1, 21)]
    out = {}
    for c in ["b", "m", "p"]:
        out[c] = []
        for s in subs:
            rec = c + s
            if not is_complete(rec):
                continue          # LOCAL + COMPLETE only (never stream, never read a partial download)
            try:
                r = analyze(rec, SAMPTO)
                if r:
                    out[c].append(r)
                    rg = r["ring"]
                    print(f"{rec} {r['cond']:10s} beats={r['n_beats']:3d} hr={r['hr_bpm']:5.1f} "
                          f"repro={r['reproducibility']:.3f} tSNR={r['template_snr']:5.1f} "
                          f"pk={r['scg_peak_hz']:5.2f}Hz low%={r['frac_power_0p5_4hz']*100:4.1f} "
                          f"ring={'Q=%.1f@%.0fHz r2=%.2f'%(rg['Q'],rg['ring_freq_hz'],rg['fit_r2']) if rg else 'none'} "
                          f"respMod={r['resp_mod_r']:+.2f}", flush=True)
            except Exception as e:
                print(f"{rec} FAILED: {e}", flush=True)
    # strip ensembles before saving summary (keep a compact stats file)
    slim = {c: [{k: v for k, v in r.items() if k != "ensemble"} for r in out[c]] for c in out}
    json.dump(slim, open(os.path.join(HERE, "cebs_heartwave_results.json"), "w"), indent=2)
    # also stash one representative ensemble per condition for plotting later
    reps = {c: (out[c][0]["ensemble"] if out[c] else None) for c in out}
    json.dump(reps, open(os.path.join(HERE, "cebs_ensembles.json"), "w"))
    print("\nwrote cebs_heartwave_results.json + cebs_ensembles.json")
