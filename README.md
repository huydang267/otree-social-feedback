# Social Feedback and Risk-Taking — A Behavioural Experiment in oTree

A fully implemented online economic experiment testing whether **peer social feedback changes
individual risk-taking**. Participants build a social profile, receive peer validation, are
randomly assigned to a feedback treatment, and then complete an incentivised risk-elicitation
task.

> **Status: research instrument, not a results repository.** This is the experimental software.
> **No hypothesis is tested here and no results are reported**, because the experiment has not
> been run at a sample size that would support inference. No participant data is included. See
> [Current status](#current-status).

---

## Research question

Does receiving positive or negative social feedback on a self-constructed identity change how
much financial risk a person subsequently takes?

The design connects two literatures: social identity and validation on one side, incentivised
risk elicitation on the other. The mechanism under test is whether peer feedback on a
*self-presented identity* shifts risk preference — not whether people conform to observed risk
behaviour, which is what most peer-effects designs measure.

## Design

Twelve-page sequence, single round.

| Stage | Page | What happens |
|---|---|---|
| 1 | `Instructions_Part1` / `Part2` | Task and incentive explanation |
| 2 | `ComprehensionQuiz` | Two questions, **enforced** — wrong answers block progress with a corrective message |
| 3 | `ProfileCreation` | Participant picks 3 of 36 stickers and 1 of 24 taglines |
| 4 | `PeerVoting` | Participants view others' profiles and "like" them |
| 5 | `CalculationWaitPage` | Likes tallied, percentile rank computed, **50% randomly assigned to treatment** |
| 6 | `TreatmentFeedback` | Social feedback delivered |
| 7 | `BRET_Task` | Bomb Risk Elicitation Task |
| 8 | `PostSurvey` | Demographics, self-reported risk tolerance, social media use |
| 9 | `FinalWaitPage` / `Results` | Random Lottery Incentive payout resolution |

### Identity construction

Stickers and taglines are grouped into three latent categories, and the participant's choices
are tallied to derive an **archetype**:

| Category | Archetype | Example tagline |
|---|---|---|
| A | The Calculated Strategist | "I have a spreadsheet for this." |
| B | The Bold Adventurer | "Doing it for the plot." |
| C | The Social Harmonizer | "Just happy to be included." |

Ties resolve to the tagline's category, since a single deliberate tagline choice is a stronger
identity signal than one of three sticker picks. The participant is never shown the category
structure — they choose on aesthetic appeal, so the archetype is elicited rather than declared.

### Risk elicitation — BRET

The [Bomb Risk Elicitation Task](https://doi.org/10.1287/mnsc.2013.1819) (Crosetto & Filippin)
presents 100 boxes, one containing a bomb. Each box collected pays $0.20; collecting the bomb
zeroes the payoff. Boxes collected is a continuous, intuitive measure of risk preference.

Chosen over Holt–Laury lottery lists because it needs no probability comprehension, produces a
continuous rather than ordinal measure, and yields far fewer inconsistent responses from
non-specialist participants.

**The bomb location is drawn *after* the participant stops** (`before_next_page`), which
guarantees the outcome cannot influence the decision and makes the draw verifiable.

### Incentives

Random Lottery Incentive: one participant is drawn at random for actual payment at $0.20 per
box. RLI keeps incentives real while bounding total cost — standard practice in experimental
economics, and appropriate for a student-budget study.

### Measurement

| Field | Purpose |
|---|---|
| `boxes_collected` | Primary dependent variable — revealed risk preference |
| `is_treatment` | Random 50% assignment |
| `likes_received`, `percentile_rank` | Social feedback received |
| `calculated_archetype` | Derived identity type |
| `general_risk_tolerance` | Self-reported risk (0–10), for comparison against revealed |
| `gender`, `is_econ_major`, `social_media_freq` | Controls |

Collecting both revealed (`boxes_collected`) and stated (`general_risk_tolerance`) risk measures
is deliberate: the gap between them is itself analysable.

## Current status

**The experiment is implemented and runnable. It has not been run as a study.**

The only sessions executed were local pilot runs to test the page flow, during development.
Those records exist solely in a local SQLite database that is **excluded from this repository**
and has never been committed.

Concretely, this means:

- **No hypothesis test has been run.** No treatment effect is claimed, in either direction.
- **No sample size is reported**, because none would be meaningful. The pilot data exists to
  confirm the pages advance correctly, nothing more.
- **Any future analysis would need a power calculation first.** For a between-subjects design
  with 50/50 assignment, detecting a medium effect (d ≈ 0.5) at 80% power needs roughly 64
  participants per arm — around 128 total. The peer-voting stage also requires enough
  simultaneous participants for the social comparison to be credible, which constrains session
  size independently of statistical power.

This repository is the instrument. Treating pilot runs as findings would be the exact error the
design is built to avoid.

## Known design limitations

Stated because they would need addressing before the experiment is run for real.

- **No deception, but the feedback is real** — participants see genuine peer likes. This makes
  the treatment honest, but it also means treatment intensity is **not controlled**: a
  participant's feedback depends on whatever profile they happened to build. A synthetic-feedback
  arm would isolate the mechanism more cleanly at the cost of requiring deception and the ethics
  approval that follows.
- **Percentile rank is computed within-session**, so its meaning depends on session size. Small
  sessions produce coarse, potentially misleading ranks.
- **Single round.** No within-subject baseline risk measure is taken before treatment, so the
  design relies entirely on randomisation to establish the counterfactual. A pre-treatment BRET
  would allow a difference-in-differences estimate, at the cost of order effects.
- **Ties in the archetype tally** resolve deterministically to the tagline category. Defensible,
  but it is a researcher choice that shapes a derived variable.
- **Self-selected online samples** skew young, educated and student-heavy. `is_econ_major` is
  collected partly to detect this, since economics students are known to behave differently in
  incentivised games.
- **No attention or manipulation check** beyond the comprehension quiz. There is no measure
  confirming participants actually registered the feedback they received.

## Participant data and ethics

**No participant data is in this repository, and none will be added.** See
[`docs/data-protection.md`](docs/data-protection.md).

- The session database (`db.sqlite3`) is gitignored and has never been committed — verified
  against the full published file list.
- `*.csv` and `*.xlsx` are gitignored, so oTree's "Data" tab exports cannot be committed by
  accident.
- The `experiment_feedback` free-text field is excluded from any export that would be published.
  Free text is the field most likely to contain self-identifying information.
- `gender` and `is_econ_major` are collected as analysis controls and would only ever be
  reported in aggregate.

Running this with human participants requires ethics approval from the relevant institutional
review board first. The code does not constitute approval.

## Security

The oTree `SECRET_KEY` was previously hardcoded in `settings.py` and is present in this
repository's git history. It has been moved to an environment variable.

**Anyone deploying this must set a fresh `OTREE_SECRET_KEY`.** The historical value must be
treated as compromised — removing a secret in a later commit does not remove it from history.
Practical exposure is low, since the key only signed sessions for a local application that was
never deployed publicly, but it should not be reused.

Copy `.env.example` to `.env` and fill in real values. `.env` is gitignored.

## Running locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# generate a key:  python -c "import secrets; print(secrets.token_urlsafe(32))"
# then set OTREE_SECRET_KEY and OTREE_ADMIN_PASSWORD in .env

otree devserver
```

Open http://localhost:8000. The default session config runs 3 demo participants; the peer-voting
stage needs at least 2 to be meaningful.

Requires Python 3.8+ and oTree 5. `python-dotenv` is required by `settings.py` and is declared
in `requirements.txt` — it was previously imported without being declared, which broke clean
installs.

**Deployment is out of scope for this repository.** The `Procfile` and `psycopg2-binary`
dependency are retained from the original configuration, but nothing here is deployed and no
hosted instance exists.

## Repository structure

```
├── settings.py                  oTree configuration (secrets via environment)
├── requirements.txt             Pinned dependencies
├── .env.example                 Template for local secrets - copy to .env
├── Procfile                     Web/worker split (unused; no deployment)
├── social_feedback/
│   ├── __init__.py              Models, pages, archetype logic, BRET, payout
│   └── *.html                   Twelve page templates
├── _static/social_feedback/
│   └── stickers/                36 sticker images
└── docs/
    ├── experiment-design.md     Full protocol, variables, and analysis plan
    └── data-protection.md       What is collected, what is excluded, and why
```

## References

- Crosetto, P. & Filippin, A. (2013). The "bomb" risk elicitation task. *Journal of Risk and
  Uncertainty*, 47(1), 31–65.
- Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree — An open-source platform for
  laboratory, online, and field experiments. *Journal of Behavioral and Experimental Finance*,
  9, 88–97.
