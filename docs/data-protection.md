# Data protection

What this experiment collects, what is excluded from the repository, and why.

## Nothing participant-related is published

**No participant data is in this repository.** Verified against the full published file list:
no database, no exports, no response data.

| Excluded | How |
|---|---|
| `db.sqlite3` — session database | Gitignored (`*.sqlite3`); never committed |
| oTree "Data" tab exports | Gitignored (`*.csv`, `*.xlsx`, `exports/`) |
| Free-text responses | Never exported; see below |
| Secrets | `.env` gitignored; `.env.example` holds placeholders only |

The only sessions ever run were local pilots during development, to confirm the page flow. Those
records live in a local SQLite file that has never left the development machine.

## What the instrument collects

Collected during a session and stored in the local database.

### Behavioural measures

| Field | Type | Sensitivity |
|---|---|---|
| `boxes_collected` | integer 0–100 | Low — the primary dependent variable |
| `bomb_location` | integer 1–100 | Low — randomly drawn after the decision |
| `sticker_1/2/3`, `tagline` | identifiers | Low — choices from a fixed set |
| `calculated_archetype` | derived | Low |
| `liked_ids`, `likes_received`, `percentile_rank` | integers | Low |
| `is_treatment` | boolean | Low — random assignment |
| `selected_for_payout`, `payoff` | — | Low |

### Survey measures

| Field | Type | Sensitivity |
|---|---|---|
| `gender` | Male / Female / Other | **Demographic** — aggregate reporting only |
| `is_econ_major` | boolean | Low |
| `general_risk_tolerance` | 0–10 | Low |
| `social_media_freq` | 4-level band | Low |
| `experiment_feedback` | **free text** | **High — see below** |

## Free-text responses

`experiment_feedback` is an open-ended field:

> *"Do you have any thoughts, feelings, or feedback regarding this experiment?"*

**This field is excluded from any published export, without exception.**

Open-ended responses are the single most likely place for self-identifying information to
appear. Participants routinely volunteer their course, campus, the friend who referred them, or
their reaction to a specific other participant — none of it requested, none of it removable by a
schema-level rule. It cannot be safely anonymised by dropping columns, because the identifying
content is inside the text.

It is retained locally because participant feedback genuinely improves instrument design between
pilots. It is never published.

## Identifiers oTree generates

oTree assigns each participant a `code` (a random string) and a `label` where one is supplied,
and records timestamps per page.

- **Participant codes are pseudonymous**, not anonymous. They link every response by one person
  across the session. They are not re-identifying on their own, but they are not a substitute
  for anonymisation.
- **`label` can carry real identity** — it is commonly populated with a student ID or email when
  recruiting through a university pool or a panel service. Any published dataset must drop
  `participant.label` explicitly. Assuming it is empty is not safe.
- **Page timestamps** are fine-grained. Combined with a known session time they are, in
  principle, re-identifying within a small cohort.

## If data were ever published

Not applicable today, since the study has not been run. If it were, the minimum would be:

1. Drop `participant.label`, `participant.code`, all IP addresses and all page timestamps.
2. Drop `experiment_feedback` entirely.
3. Replace `liked_ids` with counts only — the raw field records *who liked whom*, which is a
   social graph within the session and is re-identifying in a small cohort even without names.
4. Aggregate or suppress `gender` where cell sizes are small; "Other" will often be a cell of
   one.
5. Re-index participants with fresh sequential IDs unlinked to session order.
6. Publish only after ethics approval covering data sharing, with participant consent that
   explicitly includes it.

Point 3 is the one most easily missed. `liked_ids` looks like an innocuous integer list, but it
is relational data about identifiable people within the session.

## Secrets

- `ADMIN_PASSWORD` reads from `OTREE_ADMIN_PASSWORD`. No default.
- `SECRET_KEY` reads from `OTREE_SECRET_KEY`, with an obviously-insecure development fallback.
- `DATABASE_URL` is never committed; it is supplied by the environment.
- `.env` is gitignored; `.env.example` contains placeholders only.

**Historical exposure.** `SECRET_KEY` was hardcoded in earlier commits and remains in this
repository's git history. It has been moved to an environment variable, but history was not
rewritten — so that value must be treated as compromised and never reused. Anyone deploying
this must generate a fresh key. Real-world impact is minimal, since the key only signed sessions
for a locally-run application that was never publicly deployed.

## Ethics

Running this with human participants requires institutional review board approval before
recruitment. The design has features that an IRB would specifically examine:

- **Peer feedback can be negative.** A participant may learn they ranked poorly among peers.
  That is a real, if mild, psychological risk and needs a debrief.
- **Payment is probabilistic.** Random Lottery Incentive means most participants are paid
  nothing for the task. This must be stated clearly *before* consent, not discovered at the end.
- **Social profiles are visible to other participants**, which is a within-session disclosure
  that participants must agree to in advance.

Publishing this code is not a substitute for approval, and none is claimed.
