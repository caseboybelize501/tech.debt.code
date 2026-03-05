# Tech.Debt.Code

Autonomous Code Review & Technical Debt Navigator

## Overview

A self-learning system that continuously monitors pull requests, scores technical debt accumulation across the codebase, generates targeted refactor plans ranked by ROI, auto-patches low-risk debt items, and builds a model of what debt patterns slow this specific team's velocity.

## Features

- ✅ Continuous PR monitoring
- ✅ Technical debt scoring
- ✅ Refactor plan generation
- ✅ Auto-patching for safe debt items
- ✅ Velocity tracking
- ✅ Team-specific learning
- ✅ Stripe billing integration

## Architecture


GitHub Watcher → PRMonitorAgent → DebtScanAgent → ImpactScoreAgent →
RefactorPlanAgent → AutoPatchAgent → VelocityTrackAgent → LearnAgent
→ Tools (static analyzers: pylint/eslint/golangci-lint/rubocop, AST diff,
git blame, coverage parsers, GitHub PR API, Stripe) + Memory
(debt pattern RAG + team velocity graph + refactor outcome library +
meta-learning index per repo)


## System Requirements

- Python 3.11+
- Docker & docker-compose
- Git
- Node.js (for frontend)

## Setup

bash
# Clone the repository
$ git clone https://github.com/caseboybelize501/tech.debt.code.git
$ cd tech.debt.code

# Install dependencies
$ pip install -r requirements.txt

# Run with Docker
$ docker-compose up

# Or run directly
$ python src/main.py


## API Endpoints

- `GET /health` - Health check
- `GET /api/system/profile` - System profile
- `POST /api/debt/scan` - Scan repository for debt
- `GET /api/debt/{id}/score` - Get debt score
- `GET /api/debt/{id}/refactors` - Get refactor plan
- `GET /api/memory/patterns` - Get debt patterns
- `POST /api/payments/subscribe` - Subscribe to payment tier

## License

MIT