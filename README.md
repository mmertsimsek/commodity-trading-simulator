# Stochastic Commodity Trading Simulator

A Python-based simulation project for evaluating commodity production strategies under uncertain demand.

The simulator compares different production aggressiveness levels and selects the best strategy based on expected profit, variance, and risk-adjusted scoring.

## Project Goal

The goal of this project is to model a simplified commodity trading decision problem:

- demand is uncertain
- production capacity is limited
- storage has a cost
- higher profit usually comes with higher risk
- the system chooses the best risk-adjusted strategy

## Core Idea

The model evaluates each strategy using:

```text
score = average_profit - risk_penalty * variance
