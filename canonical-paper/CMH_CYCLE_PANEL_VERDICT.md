# V1 (static) vs V2 (cycle) -- Comparative Panel Verdict
Recorded 2026-07-14. Plain ASCII. Five simulated expert lenses read both PDFs:
hyperscanning neuroscientist, collective-intelligence researcher, complex-systems physicist,
skeptical peer reviewer, senior journal editor. This is an anticipatory red-team, not real
peer review; the convergence across independent lenses is the signal.

Files judged:
  cmh-collective-intelligence.pdf        (V1, "static": CI(r)=r(1-r))
  cmh-collective-intelligence-cycle.pdf  (V2, "cycle": the breathing rhythm)

================================================================================
## THE BOTTOM LINE
================================================================================
Four of five reviewers say the cycle idea (V2) is the stronger contribution; the fifth
(skeptic) agrees the *kernel* is real but says the current packaging is riskier than V1.
Unanimous on structure: this is ONE paper, not two. V1's CI(r)=r(1-r) becomes the "static /
do-both-at-once bound" subsection; the breathing cycle is the payoff. Do NOT ship V1 as a
standalone flagship (by its own abstract it "formalizes rather than discovers" -- a referee
will say so), and do NOT ship V2 as-is (its central claim is posited, not proved).

The panel's real message is a fork, and it is precise:
  - As written, V2's core is INCREMENTAL: "complementary operations with opposite coupling
    optima favor time-multiplexing over a static compromise" is a known convex-dominance
    principle (Jensen / bang-bang / duty-cycling / Parrondo / exploration-exploitation), and
    the alternation is already Bernstein-Shore-Lazer (2018). A capable but not seminal paper.
  - There is ONE upgrade that flips it to SEMINAL, and it is concrete and doable: derive the
    breath as a SELF-ORGANIZED relaxation limit cycle from ADAPTIVE coupling, instead of
    imposing it as a schedule. That converts "an engineer can impose a duty cycle" (trivial)
    into "coupled minds spontaneously breathe, and that is optimal" (a real theorem).

So the value of the write-cycle proposal is HIGH but CONDITIONAL: it is seminal-capable, and
the physics upgrade below is what cashes the check.

================================================================================
## WHERE THE PANEL CONVERGED
================================================================================
1. MERGE. One paper: V1's r(1-r) = the static lower bound (a subsection); the cycle = the
   contribution. No two co-equal papers. (all five)
2. THE GENUINE NEW KERNEL is the TEMPO -- a finite optimal period with a scale -- and the
   claim that the TEMPORAL PATTERN of synchrony predicts performance beyond its mean. That is
   what Bernstein/Lazer cannot state. (all five)
3. THE CENTRAL FLAW: the dominance (breathing beats static) is ASSERTED, not proved. Eq. (4)
   Y = S(r_up)G(r_down) - C_switch is admitted "illustrative, not a theorem." (all five)
4. THE MULTIPLICATIVE ASSUMPTION *IS* THE THEOREM. If per-cycle value ADDED instead of
   multiplied, breathing buys nothing (S+G is flat; the optimum is a constant r). The whole
   dominance lives in the multiplicative / complementary-input (Liebig / Cobb-Douglas) form.
   State this plainly as the boundary of the claim -- it is not a caveat, it is the load.
   (physicist explicit; CI agrees; NOTE the skeptic wrongly thought it robust to additivity --
   the physicist's Jensen argument settles it: additive => no breathing benefit.)
5. CUT (or heavily demote) THE DMN / MEDITATION / "WRITE-IN-THE-TROUGH" MATERIAL. It is the
   weakest, riskiest element: EEG cannot measure the DMN (an fMRI network); it conflates group-
   decoupling with an individual cognitive mode; it picks one side of a live dispute
   (incubation research ties creativity to DMN UP-regulation, not down); and given the withdrawn-
   Schumann footnote it "primes a referee to suspect a relapse into over-reach." The tempo law
   needs no neuro story. (skeptic: cut; hyperscanning: demote/re-modality; physicist: unneeded)
6. LEAD WITH THE TEMPO LAW, NOT "TEMPORAL PATTERN BEATS MEAN." The latter (Prediction 1) is a
   near-tautology -- r(t) always has more information than its mean, so a rich model wins by
   overfitting unless you pre-commit to WHICH feature and its SIGN. The tempo law (Prediction 3:
   finite optimal period, inverted-U in period, tied to an independently measured timescale) is
   the a-priori, unfakeable test. (skeptic; endorsed by others)
7. ONE REAL RE-ANALYSIS. Put a single panel of real data in (Bernstein 2018 / Dikker 2017 open
   data) showing alternation predicts performance beyond mean r. "First blood" moves it from
   beautiful hypothesis to result. (editor; skeptic's cheap-test; hyperscanning's re-analysis)
8. SCHUMANN FOOTNOTE IN EXACTLY ONE PAPER. Repeated across the set it "looks haunted." Keep it
   once, as clean provenance. (editor)

================================================================================
## THE SINGLE HIGHEST-LEVERAGE MOVE (what makes it seminal, from the physicist + editor)
================================================================================
Two levels; do at least the first, do the second to be seminal.

LEVEL 1 -- Name the theorem and prove the easy version (cheap, ~a page).
  State the convex-dominance proposition explicitly: with S increasing in r, G decreasing in r,
  and MULTIPLICATIVE per-cycle yield, the objective is non-concave in the time allocation, so
  under a time-average constraint it is maximized bang-bang -- the extreme points (corners) beat
  any interior fixed r. A two-point (r_down, r_up) proof that S(r_up)G(r_down) > max_r S(r)G(r)
  suffices. Cite the convex-dominance backbone (Jensen; Pontryagin bang-bang / chattering
  controls; flashing ratchet / Parrondo; March 1991 exploration-exploitation). This converts the
  headline from rhetoric to a stated (if elementary) result and names additivity as the boundary.

LEVEL 2 -- Derive the breath as a SELF-ORGANIZED limit cycle (the seminal upgrade).
  As written, K(t) is an externally imposed open-loop schedule, and "the optimum is a limit
  cycle" conflates an optimal control TRAJECTORY that happens to be periodic with a stable
  limit-cycle ATTRACTOR of an autonomous flow. The title promises the second; the math delivers
  the first. Fix by making coupling ADAPTIVE: add a slow variable so K senses coherence and
  modulates itself -- e.g. a consensus-fatigue / resource that depletes with alignment and
  recovers with separation, or Hebbian/anti-Hebbian plasticity:
        K_dot = -epsilon (K - K0) + (feedback on r).
  In the slow-fast (r, K) system, show the fixed point r* is destabilized via a Hopf bifurcation
  and a stable RELAXATION OSCILLATION -- a genuine breathing limit cycle -- emerges. Then the
  group "breathes on its own," which is a theorem, not a schedule. The adaptive-Kuramoto
  literature already exhibits exactly such breathing/multicluster relaxation dynamics, and this
  is what makes the Tognoli-Kelso metastability tie load-bearing rather than decorative
  (biological metastability is intrinsic, not scheduled).

CRITICAL PHYSICS CORRECTION (either level): the tempo bound in the paper (T* >~ tau_int, a
within-PERSON cognitive time) is NOT the right physical bound. The order parameter has its OWN
relaxation dynamics; the Ott-Antonsen / Stuart-Landau normal form gives
        dr/dt = (K(t)/2 - gamma) r - (K(t)/2) r^3,
whose relaxation rate |gamma - K/2| = |K - Kc|/2 VANISHES at the transition (critical slowing
down). The breathing scheme must cross Kc every half-cycle -- exactly where the relaxation time
diverges -- so if K(t) is driven faster than tau_r, r never reaches the quoted extremes
(amplitude-attenuated, hysteretic). The binding constraint is T >> tau_r(K), a COLLECTIVE
timescale, not tau_int. USE the OA one-liner (it is cited in both papers but never used) to
compute the achievable r(t) for a given tempo and derive the RIGHT bound. This is the difference
between an asserted tempo and a derived one.

================================================================================
## ADDITIONAL FIXES (consensus)
================================================================================
- CITE MARCH 1991 (Exploration and Exploitation in Organizational Learning) -- MANDATORY and
  currently absent. "Sharing wants convergence, generating wants divergence, no single setting
  serves both" IS March's tradeoff; a CI referee catches its absence in seconds. (CI, physicist)
- ADD the dynamics canon: chimera (Abrams-Strogatz 2004; Panaggio-Abrams 2015); ADAPTIVE/PLASTIC
  Kuramoto (Aoki-Aoyagi 2009; Seliger-Young-Tsimring 2002; Berner et al.; Maistrenko) -- the
  emergent-cycle engine; slow-fast / relaxation & bursting (Rinzel; Izhikevich; Ermentrout-
  Kopell); Kuramoto-Sakaguchi phase lag; Almaatouq 2020-21 (adaptive networks; task-contingency);
  Shirado-Christakis 2017 (noise breaks gridlock); Bahrami 2010. Promote Ott-Antonsen 2008 from
  footnote to the actual dr/dt derivation. (physicist, CI)
- COIN A DIMENSIONLESS NUMBER. Seminal papers leave a measurable behind (Reynolds number,
  small-world sigma, the c-factor). Name the group that decides whether breathing wins -- a
  "respiration number" / duty ratio: switching-cost-to-generative-gain, or period-to-tau_r. Give
  the field a quantity to estimate and they use your paper as its definition. (editor)
- MAKE FIGURE 1 THE ARGUMENT. Replace the sine-wave figure with three curves in one frame:
  S(r) rising, G(r) falling, and the shaded area showing the corners' product exceeds the
  interior product. "That figure IS the paper." (editor)
- MODEL THE CARRIED STOCK. Sharing at high r presupposes material the generate phase produced;
  generating at low r presupposes shared context -- an implicit inventory carried across phases
  that is never modeled. (physicist)

================================================================================
## THE TITLE (a genuine split, resolved)
================================================================================
Split: the EDITOR defends a metaphor-forward title (fields carry metaphors: "wisdom of crowds,"
"small worlds") IF anchored by mechanism; the SKEPTIC says "breathing" HURTS this author (a
poetic title is a loan against credibility only a proven result repays, and this author carries a
withdrawn grandiose prior); the PHYSICIST warns "breathing" pre-commits to a limit-cycle ATTRACTOR
the paper does not yet derive; hyperscanning and CI want mechanism-forward with a memorable handle.

Reconciliation (depends on whether Level 2 physics gets done):
  - Publishing the CURRENT (time-multiplexing) content -> lead with mechanism, keep a handle:
    RECOMMENDED NOW: "The Optimum Is a Rhythm: Time-Multiplexed Coupling in Collective
    Intelligence." ("The optimum is a rhythm" is the sayable, slide-ready handle multiple
    reviewers converged on; it does not over-promise a derived attractor.)
  - After the adaptive-coupling derivation (Level 2), the metaphor is EARNED:
    "Groups Must Breathe: Why the Optimum for Collective Intelligence Is a Rhythm, Not a
    Set-Point." (Editor's pick; the "X, not Y" subtitle names the incumbent it overturns.)
  Do NOT use "The Breathing of Groups" as the primary title as-is -- four of five flagged it as
  metaphor-first over an un-derived claim. Keep "breathe" as the verb in the body regardless.

================================================================================
## PER-REVIEWER VERDICTS
================================================================================
- Hyperscanning: advance V2 (flagship), V1 as cited static companion; the contribution is "the
  clock" (T*~tau_int); DMN link over-commits the neuroscience the EEG design can deliver -- demote;
  the experiment is unusually confound-safe; lead mechanism ("The Optimum Is a Rhythm").
- Collective intelligence: V2 stronger "and it's not close"; fold V1 in as Section 2; MANDATORY
  March 1991; the new step = tempo + write-in-trough + temporal-pattern-beyond-mean; bound Eq. 4;
  don't publish V1 alone.
- Physicist: V1 the stronger PAPER, V2 the stronger IDEA; dominance is a known convex-dominance
  result and the multiplicative form IS the theorem; the K(t)->r(t) tracking is un-derived and
  tau_int is the wrong bound (use OA dr/dt, critical slowing); SEMINAL only after adaptive-coupling
  self-organized limit cycle (Hopf); merge, staged.
- Skeptic: V1 survives review better (lower desk-reject); the kernel (time-multiplexing + tempo)
  is real (~30% advance, ~70% risk-ornament); CUT Section 3 (DMN) + Prediction 2; lead with the
  tempo law not the near-tautological Prediction 1; "breathing" hurts; merge, V1 as spine.
- Editor: V2 has seminal SHAPE, "one honest move away"; demote V1 to a subsection (not co-equal);
  four upgrades -- prove the corner-beats-interior, one real re-analysis, coin the number, killer
  figure; keep an anchored metaphor title; Schumann footnote once.

================================================================================
## ONE-LINE TAKEAWAY
================================================================================
The write-cycle proposal is real and seminal-CAPABLE, but as written it is an elegant
restatement of a known principle (time-multiplexing beats a static compromise) plus Bernstein's
alternation. It becomes seminal with one concrete, doable move: let the coupling adapt so the
group's breath SELF-ORGANIZES into a relaxation limit cycle (Hopf), derive the true tempo from
the order-parameter relaxation (Ott-Antonsen), name the multiplicative assumption as the theorem,
cut the DMN bridge, lead with the tempo law, and merge V1 in as the static bound. Do that, and
"Groups Must Breathe" is a title the field remembers by name rather than a slogan.
