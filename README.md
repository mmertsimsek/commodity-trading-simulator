# Commodity Trading Strategy Simulator

A full-stack ready stochastic commodity trading simulator built with Python, FastAPI, and PostgreSQL.

This project models a simplified commodity trading environment under uncertainty and evaluates production strategies using Monte Carlo simulation and risk-adjusted scoring.

---

## Project Overview

This system simulates a commodity producer that must decide how aggressively to produce under uncertain demand and storage constraints.

The model incorporates:

* stochastic demand (randomized)
* limited storage capacity
* production constraints
* inventory carryover across periods
* future value of stored inventory

The system evaluates multiple strategies and selects the optimal one based on a risk-return tradeoff.

---

## Core Concept

Each strategy is evaluated using a risk-adjusted score:

```
score = average_profit - risk_penalty * variance
```

Where:

* `average_profit` = expected return
* `variance` = risk
* `risk_penalty` = risk aversion parameter

This mimics real-world decision-making in commodity trading and quantitative finance.

---

## Features

* Monte Carlo simulation engine
* Strategy optimization across multiple production levels
* Risk classification (low / medium / high)
* Strategy evaluation (weak / acceptable / strong)
* Inventory tracking over time
* Future value approximation for stored goods
* REST API with FastAPI
* PostgreSQL database integration
* Persistent storage of simulation results

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic

---

## Architecture

```
Core Simulation Layer
├── simulator.py
├── optimizer.py
├── evaluate_strategy.py

Backend API Layer
├── FastAPI (app/)
├── Routes
├── Services
├── Schemas

Database Layer
├── PostgreSQL
├── SQLAlchemy ORM
```

---

## API Endpoints

### POST /simulate

Runs a simulation for a single strategy.

Request:

```json
{
  "aggressive_level": 3,
  "storage_penalty_weight": 10,
  "runs": 100,
  "risk_penalty": 0.1
}
```

Response:

```json
{
  "aggressive_level": 3,
  "avg_profit": 129.96,
  "variance": 899.8,
  "score": 39.98,
  "risk_label": "medium risk",
  "decision_label": "acceptable strategy"
}
```

---

### POST /optimize

Finds the best strategy across all levels.

---

### GET /results

Returns stored simulation results from PostgreSQL.

---

## Database Model

Table: `simulation_results`

Fields:

* id
* run_type (simulate / optimize)
* aggressive_level
* avg_profit
* variance
* score
* risk_label
* decision_label
* created_at

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start PostgreSQL

3. Run the API:

```bash
uvicorn app.main:app --reload
```

4. Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Example Workflow

1. Run `/simulate` to test a strategy
2. Run `/optimize` to find the best strategy
3. View results via `/results`

---

## Future Improvements

* stochastic price modeling
* dynamic programming / reinforcement learning
* better demand distributions
* front-end dashboard (Angular)
* Docker deployment
* cloud hosting (AWS/GCP)

---

## Why This Project Matters

This project demonstrates:

* quantitative thinking (risk vs return)
* backend engineering (FastAPI + DB)
* simulation modeling
* clean architecture design

It is directly relevant for:

* commodity trading roles
* quantitative analyst positions
* backend / full-stack engineering roles

## Live Demo

Backend API:

https://commodity-trading-simulator.onrender.com/docs

The frontend connects to the live FastAPI backend and stores simulation results in PostgreSQL.

## Screenshots

### Frontend
![Frontend](frontend.png)

### API Docs
![API](api.png)
