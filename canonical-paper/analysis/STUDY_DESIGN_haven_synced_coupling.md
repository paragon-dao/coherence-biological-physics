# Study design: Haven-node-synced multi-person cardiac-coupling study
Written 2026-07-21 from Phil's connection: the couple/group sleep study needs
synchronized multi-person data, and Haven Node infrastructure already does
exactly that. Plain ASCII. Design-first; honest about which CMH claim each
piece tests.

===================================================================
## WHAT HAVEN IS FOR (corrected 2026-07-21 by Phil -- read first)
===================================================================
Haven's value is NOT syncing a dyad and it is NOT using the internet as a
channel to send one person's signal to another. Its value is SCALE +
DISTRIBUTION: Haven nodes are already deployed on MANY people, in the wild,
across locations, continuously. That makes Haven a DISTRIBUTED OBSERVATORY for
COLLECTIVE coupling -- we can look at coherence across a whole population, not
just two people in a room.

How it works (the method, and it is the honest one): each node measures its OWN
person's biosignals INDEPENDENTLY and locally. No node sends its person's state
to another person. We detect coupling purely by ANALYZING correlations ACROSS
the population's independently-measured signals, aligned by GPS-synced
timestamps. The nodes are sensors in an array; the coupling, if it exists, is in
the people, not in the network.

Why this is the big unlock: no lab can put hundreds of people in sleep beds
across cities for a month. Haven already has the people and the distribution.
This directly targets CMH's MOST AMBITIOUS layer -- COLLECTIVE / population-scale
coherence and group-synchronization events (paper 8.3.3, 8.4) -- not just the
pairwise claim. It is Phil's own version of the global 104-person heart-rhythm
synchronization study, at potentially far larger scale, because the nodes are
already out there.

===================================================================
## THE INTEGRITY FLAG (still holds, now a one-line method rule)
===================================================================
One week ago (2026-07-14) Phil split CMH into v1.0 and v2.0
([[project_eci_cmh_connection]]). v2.0 WITHDREW the nonlocal / planetary-field
mechanism on a power-budget argument (a warm-body biofield cannot drive a
planetary cavity mode above the lightning background). The science that
SURVIVES in v2.0 = coupled oscillators coupling via INFORMATION CHANNELS
(near-field, bounded, NO nonlocal). The marrow/Schumann/nonlocal material moved
to the philosophical paper as honest metaphysics.

Why this matters HERE: the moment Haven syncs two partners' data over a network,
Haven IS an information channel. So we must keep two roles strictly separate, or
the study cannot distinguish its own hypotheses:

- ROLE 1 -- HAVEN AS INSTRUMENT (collect / timestamp / attest / store ONLY).
  Each partner's sensors write to THEIR OWN node; data is GPS-timestamped,
  Ed25519 + TPM signed (Patent 17 Claim 9), privacy-preserving. No partner's
  live state is shared to the other during recording. This measures whether
  their BODIES couple through natural channels, with tamper-evident data a
  reviewer trusts. THIS IS THE BIOLOGICAL STUDY.
- ROLE 2 -- HAVEN/ECI AS SUBSTRATE (nodes gossip compressed biosignal state).
  This is CMH-in-silicon, the v2.0 coupled-oscillator-via-channels twin. A
  DIFFERENT experiment: do node networks show the collective dynamics human
  groups do. Legitimate and exciting -- but NOT the biological measurement.

THE WALL (new location, same principle): for the biological study, Haven may
only instrument. If Haven shares partner state during recording, we have BUILT
the coupling we claim to detect. Instrument is not intervention. Never blur.

Consequence for the "coupling at distance" idea from the prior discussion: with
Haven as a live channel, distance coupling is trivially the app moving data --
NOT biology. The honest distance test requires NO information channel between
partners during recording (pure passive parallel measurement, clocks synced by
GPS not by exchanging data). v2.0 predicts that test is NULL at distance; v1.0
predicted a signal. Running it cleanly is how the two versions are decided.

===================================================================
## WHY HAVEN IS THE RIGHT INSTRUMENT (Role 1)
===================================================================
The study's hard problem is synchronized, trustworthy, private multi-person
biosignal capture over many nights, in homes, possibly across locations. Haven
already solves each piece:
- NODE-CANONICAL STORAGE: each person's raw biosignals stay on their own node/
  device; nothing sensitive persists on any relay (60s hard-delete-on-ACK).
  Sleep + cardiac + (later) bone-vibration data is intimate; this is the only
  ethically clean way to hold it at scale.
- CRYPTOGRAPHIC ATTESTATION (Ed25519 + TPM-bound hardware identity, Patent 17
  Claim 9): every record is signed to a hardware identity + timestamp. For a
  preprint, this is gold -- the data is tamper-evident and provenance-locked, a
  reviewer can trust it was not edited. This is the same signed-claim discipline
  we use for Reflex DD, applied to science.
- SYNC + TIMESTAMP: envelope metadata carries timestamps; GPS-disciplined clocks
  (per the CMH roadmap) give sub-ms cross-node alignment for coupling analysis.
- BUFFER + RETRY: 7-day offline buffer, retry/backoff -- home recordings survive
  network gaps; data reaches the analysis store without loss.
So: build a thin "Haven Sense" app profile = the fleet's existing node stack,
carrying accelerometer/ECG/temp streams instead of mail, same attestation and
node-canonical rules. Little new infrastructure; mostly a new payload type.

===================================================================
## THE STUDY (three layers, mapped to who/what/where)
===================================================================
L1 -- SINGLE BODY (heart wave + resonance). n = 1-2 (Phil + Anh). Home nights.
   Multi-site bone accelerometers + ECG + core temp on ONE person; test the
   reproducible wave, the ring-down/Q, temperature dependence, sleep
   amplification. Haven = instrument. Answers "is there a marrow-resonator
   signature at all" (the discriminating test chest-SCG can't do).
L2 -- POPULATION, DISTRIBUTED (the Haven layer -- collective coupling at scale).
   Many Haven-instrumented people, in the wild, across locations, measured
   independently and continuously. Detect coupling by correlations across the
   population (synced clocks). Structure the analysis by RELATIONSHIP GRADIENT
   (the design IS the prediction, paper 8.3.1): within-household > friends >
   strangers > random-surrogate null. Test the COLLECTIVE claims (paper 8.3.3/
   8.4): do many people's rhythms show above-chance group synchrony; do
   population-level coherence shifts track shared events or lunar/geophysical
   windows? This is what no lab can do and what Haven uniquely unlocks. A single
   co-sleeping dyad (Phil + Anh) is just the smallest instance of this, useful
   for piloting the pipeline.
L3 -- THE DISTANCE DECIDER (v1.0 vs v2.0). Because Haven measures people
   independently across locations by design, it ALREADY separates co-located
   from distant pairs. Ask: does any coupling survive between people who are far
   apart with NO shared information channel (nodes never exchange personal
   state)? Persists at distance -> extraordinary (v1.0). Vanishes with distance,
   present only near-field -> v2.0 confirmed. Either result is publishable and
   honest -- and the population design gives many distance pairs for free.

RECRUITMENT (the "how do you get people to sleep in groups" answer): you don't
gather strangers -- you instrument people who ALREADY co-sleep, at home, so the
group sleep is natural, retention is high, and multi-week lunar-cycle coverage
is feasible (nobody lives in a lab for a month; everyone sleeps at home for a
month). Contemplative communities (retreat centers, meditators) = the willing
high-coherence population the theory flags. Twin registries for the strongest-
coupling arm.

===================================================================
## THE ECI PARALLEL TRACK (Role 2 -- complementary, not the same paper)
===================================================================
Run the SAME coupling math on the Haven/ECI node network itself: nodes gossiping
compressed biosignal state (HAR 60-byte channel + text channel) are coupled
oscillators via channels -- the v2.0 model in silicon
([[project_eci_full_vision]]). Question: does a node network reproduce the
collective dynamics (inverted-U integration-vs-independence, coupling ~ bandwidth
x fidelity) that v2.0 predicts for human groups? This is CMH-in-silicon as its
own study, and it strengthens the v2.0 paper -- but it is a SEPARATE result from
the biological measurement. Do not merge the two in one paper (claims hygiene).

===================================================================
## PUBLICATION MAPPING
===================================================================
- L1 + open-SCG replication (CEBS/FOSTER/SCG-RHC) -> the modest first bioRxiv
  methods/precursor preprint (NOT "CMH validated").
- L2 (relationship-gradient cardiac coupling in sleep) -> the real empirical
  CMH v2.0 paper once n and replication are met.
- L3 (separated-nights decider) -> the high-stakes test; result either way.
- ECI node-network track -> feeds the v2.0 collective-intelligence paper.
Every number through the 4-agent claims panel before any external word.

## Next build (cheap, when hardware resourced)
1. "Haven Sense" payload profile on the existing node stack (accel/ECG/temp
   instead of mail; same attestation + node-canonical + 60s-delete rules).
2. The L1 multi-site bone rig (~$400, Phil + Anh) -- first CMH-designed capture.
3. IRB for dyad sleep + temperature modulation (couples-sleep is trodden IRB
   ground; temp needs medical monitoring per the roadmap).
