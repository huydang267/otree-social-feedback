# Experiment design

Full protocol, variable definitions, and the analysis plan that *would* apply if the study were
run. **No results are reported here** — the experiment has not been conducted at scale.

## Hypotheses

Pre-specified, untested.

| | Hypothesis |
|---|---|
| **H1** | Participants receiving positive social feedback take **more** risk in the BRET than those who do not. |
| **H2** | The effect of feedback is moderated by the participant's constructed **archetype** — feedback confirming a Bold Adventurer identity amplifies risk-taking more than feedback confirming a Calculated Strategist identity. |
| **H3** | Revealed risk (`boxes_collected`) diverges from stated risk (`general_risk_tolerance`), and social feedback moves the revealed measure more than the stated one. |

H3 is the most robust of the three, because it does not depend on the treatment working — the
revealed-versus-stated gap is analysable either way.

## Procedure

### 1–2. Instructions and comprehension

Two instruction pages, then a two-question quiz. The quiz is **enforced**: an incorrect answer
returns a corrective explanation and blocks progress.

| Question | Correct | Tests |
|---|---|---|
| Stop at 20 boxes, bomb in box 75 → earnings? | $4.00 | Payment accrues per box when the bomb is avoided |
| Stop at 50 boxes, bomb in box 12 → earnings? | $0.00 | Collecting the bomb zeroes the payoff |

Both failure modes are covered deliberately. A participant who misunderstands the downside will
over-collect, contaminating the dependent variable with comprehension error rather than risk
preference.

### 3. Profile creation

3 stickers from 36, 1 tagline from 24. **Both lists are shuffled per participant**, so position
effects do not systematically bias which items are chosen.

Archetype derivation: tally category membership across the 3 stickers and 1 tagline; the
modal category wins; ties resolve to the tagline's category.

The category structure is never shown. Participants choose on appeal, so the archetype is
**elicited rather than self-declared** — avoiding the self-presentation bias that a direct
"which type are you?" question would introduce.

### 4. Peer voting

Participants view other profiles in the session and like any number of them. Likes are stored as
a comma-separated list of recipient IDs.

### 5. Calculation

Executed once all participants arrive:

1. Tally likes received per participant.
2. Compute percentile rank from the sorted like distribution.
3. **Randomly assign exactly 50%** to treatment via `random.sample`.

Note that treatment assignment is random and therefore **independent of likes received**. This
is the correct design: it separates *receiving feedback* from *being popular*. Without it,
treatment would be confounded with whatever makes a profile appealing.

With an odd number of participants, integer division floors the treatment group, so assignment
is 50% or marginally below.

### 6. Treatment feedback

The treatment group receives social feedback on their profile. The control group does not.

### 7. BRET

100 boxes, one bomb, $0.20 per box collected, bomb zeroes the payoff. The participant chooses
how many to collect. `bomb_location` is drawn **after** submission, in `before_next_page`,
so it cannot influence the decision.

### 8. Post-survey

`gender`, `is_econ_major`, `general_risk_tolerance` (0–10), `social_media_freq` (4 bands),
`experiment_feedback` (free text, optional, never published).

### 9. Payout

One participant drawn at random across the session. If drawn, payoff = `boxes_collected × $0.20`,
or $0 if the bomb was collected.

## Variables

### Dependent

| Variable | Type | Range |
|---|---|---|
| `boxes_collected` | integer | 0–100 |

### Treatment

| Variable | Type | Notes |
|---|---|---|
| `is_treatment` | boolean | Random 50% |

### Moderators and controls

| Variable | Type | Role |
|---|---|---|
| `calculated_archetype` | 3-level factor | Moderator (H2) |
| `likes_received` | integer | Feedback intensity |
| `percentile_rank` | integer 1–100 | Relative standing |
| `general_risk_tolerance` | 0–10 | Stated risk (H3) |
| `gender` | 3-level | Control |
| `is_econ_major` | boolean | Control — known to affect behaviour in incentivised games |
| `social_media_freq` | 4-level ordinal | Control — validation sensitivity proxy |

## Analysis plan

Pre-specified. **Not executed.**

1. **Randomisation check** — compare archetype, gender, econ-major and stated risk tolerance
   across arms. Imbalance on a small sample is likely and must be reported, not silently
   controlled away.
2. **H1** — two-sample test on `boxes_collected` by `is_treatment`. Inspect the distribution
   first: BRET responses commonly pile up at focal values (50, and the risk-neutral optimum),
   so a t-test's normality assumption should be checked rather than assumed. Mann–Whitney as
   the fallback.
3. **H2** — `boxes_collected ~ is_treatment × calculated_archetype`, with the interaction as the
   term of interest. This needs substantially more power than H1; a three-level interaction on
   a modest sample will be underpowered, and that should be stated up front rather than
   discovered afterwards.
4. **H3** — correlate revealed against stated risk; compare treatment effects on each.
5. **Controls** — add `gender`, `is_econ_major`, `social_media_freq`. Report both adjusted and
   unadjusted estimates.

### Power

For a between-subjects comparison at 80% power, α = 0.05:

| Effect size | n per arm | Total |
|---|---|---|
| d = 0.8 (large) | 26 | 52 |
| d = 0.5 (medium) | 64 | 128 |
| d = 0.2 (small) | 394 | 788 |

A realistic target is d ≈ 0.5, so roughly **128 participants**. H2's interaction needs
considerably more.

There is also a design-side constraint independent of statistics: the peer-voting stage needs
enough simultaneous participants for social comparison to feel real. Sessions of 3–5 produce
percentile ranks too coarse to carry meaning.

## Why these instruments

**BRET over Holt–Laury.** Holt–Laury requires comprehending ten paired lotteries with varying
probabilities, and produces an ordinal switching point with well-documented inconsistent
switching. BRET needs no probability reasoning, yields a continuous measure, and is far more
robust with non-specialist participants.

**RLI over paying everyone.** Random Lottery Incentive preserves real monetary stakes — the
standard requirement for valid preference elicitation — at bounded cost. The trade-off is that
most participants earn nothing, which must be disclosed before consent.

**Real peer feedback over scripted feedback.** Real likes avoid deception and the heavier ethics
burden that follows. The cost is that **treatment intensity is uncontrolled**: a participant's
feedback depends on the profile they happened to build. This is the design's principal
weakness, and a synthetic-feedback arm would be the natural extension.
