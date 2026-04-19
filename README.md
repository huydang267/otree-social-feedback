# Social Feedback & Risk-taking Experiment (oTree)

## Project Overview
This experimental economics project investigates how social feedback mechanisms (stickers and taglines) influence individual risk preferences. The study utilizes a digital profile creation phase followed by a Peer Voting stage and a Bomb Risk Elicitation Task (BRET).

## Experimental Design
- **Social Identity Construction**: Participants select from 36 unique stickers and 24 taglines to build a profile.
- **Peer Feedback**: Real-time interaction allowing participants to "like" others' profiles.
- **Risk Elicitation**: A 100-box BRET module with dynamic incentive tracking.
- **Incentive Structure**: Random Lottery Incentive (RLI) where one participant is selected for a cash payout based on their BRET performance ($0.20 per box).

## Technical Specifications
- **Framework**: oTree 5.0.0+
- **Primary Language**: Python 3.x / JavaScript (Frontend Grid Logic)
- **Database**: 
  - Local: SQLite3 (excluded via `.gitignore`)
  - Production: PostgreSQL (via `psycopg2-binary`)
- **Server Configuration**: Multi-process Production Server (via `Procfile`)

## Application Sequence
As defined in `settings.py`, the session consists of:
1. `social_feedback`: The core application managing the entire experiment flow.

## Deployment Instructions
This repository is pre-configured for **Heroku**:
1. Connect this GitHub repository to your Heroku app.
2. Ensure the following environment variables are set in Heroku:
   - `OTREE_ADMIN_PASSWORD`: For admin dashboard access.
   - `DATABASE_URL`: Automatically provided by Heroku Postgres.
3. The `Procfile` uses a split web/worker configuration to optimize performance for concurrent voting.

## Local Development
To run this project locally:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the server: `otree devserver`
