from simulator import evaluate_strategy
from config import MIN_STRATEGY_LEVEL, MAX_STRATEGY_LEVEL


def calculate_score(avg_profit, variance, risk_penalty):
    return avg_profit - risk_penalty * variance


def classify_strategy(avg_profit, variance, score):
    if variance > 1000:
        risk_label = "high risk"
    elif variance > 300:
        risk_label = "medium risk"
    else:
        risk_label = "low risk"

    if score > 60:
        decision_label = "strong strategy"
    elif score > 30:
        decision_label = "acceptable strategy"
    else:
        decision_label = "weak strategy"

    return risk_label, decision_label


def find_best_strategy(
    risk_penalty,
    storage_penalty_weight,
    runs,
    min_level=MIN_STRATEGY_LEVEL,
    max_level=MAX_STRATEGY_LEVEL
):
    best_level = None
    best_score = float("-inf")
    results = []

    for level in range(min_level, max_level + 1):
        avg_profit, variance = evaluate_strategy(
            aggressive_level=level,
            storage_penalty_weight=storage_penalty_weight,
            runs=runs
        )

        score = calculate_score(
            avg_profit=avg_profit,
            variance=variance,
            risk_penalty=risk_penalty
        )

        risk_label, decision_label = classify_strategy(
            avg_profit=avg_profit,
            variance=variance,
            score=score
        )

        result = {
            "level": level,
            "avg_profit": avg_profit,
            "variance": variance,
            "score": score,
            "risk_label": risk_label,
            "decision_label": decision_label
        }

        results.append(result)

        if score > best_score:
            best_score = score
            best_level = level

    return best_level, best_score, results
