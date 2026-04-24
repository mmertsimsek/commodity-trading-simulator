import random
from config import PRICES, MAX_STORAGE, RANDOM_SEED, DEFAULT_FUTURE_WEIGHT

AVG_PRICE = sum(PRICES) / len(PRICES)

def decide_production(
    price,
    storage,
    demand,
    aggressive_level,
    storage_penalty_weight,
    avg_price,
    future_weight,
):
    best_score = float("-inf")
    best_production = 0

    max_possible_production = min(
        aggressive_level,
        MAX_STORAGE - storage
    )

    for production in range(0, max_possible_production + 1):
        available = storage + production

        sell_today = min(available, demand)
        profit_today = price * sell_today

        next_storage = available - sell_today

        storage_ratio = next_storage / MAX_STORAGE
        storage_penalty = storage_ratio * storage_penalty_weight

        expected_future_price = avg_price

        future_value = expected_future_price * next_storage

        score = (
               profit_today
               + future_weight * future_value
               - storage_penalty
        )

        if score > best_score:
            best_score = score
            best_production = production

    return best_production


def run_simulation(aggressive_level, storage_penalty_weight):
    storage = 0
    total_profit = 0

    for price in PRICES:
        demand = random.randint(0, 5)

        production = decide_production(
            price=price,
            storage=storage,
            demand=demand,
            aggressive_level=aggressive_level,
            storage_penalty_weight=storage_penalty_weight,
            avg_price=AVG_PRICE,
            future_weight=DEFAULT_FUTURE_WEIGHT,

            )

        available = storage + production
        sell = min(available, demand)
        profit = price * sell

        storage = available - sell
        total_profit += profit

    return total_profit


def evaluate_strategy(aggressive_level, storage_penalty_weight, runs):
    profits = []

    for _ in range(runs):
        profit = run_simulation(
            aggressive_level=aggressive_level,
            storage_penalty_weight=storage_penalty_weight
        )
        profits.append(profit)

    avg_profit = sum(profits) / len(profits)

    variance = sum(
        (profit - avg_profit) ** 2 for profit in profits
    ) / len(profits)

    return avg_profit, variance
