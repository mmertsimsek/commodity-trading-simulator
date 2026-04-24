from optimizer import find_best_strategy
from config import (
    DEFAULT_RUNS,
    DEFAULT_RISK_PENALTY,
    DEFAULT_STORAGE_PENALTY_WEIGHT
)


def print_results(results, best_level, best_score):
    for result in results:
        print(
            "level:", result["level"],
            "avg_profit:", round(result["avg_profit"], 2),
            "variance:", round(result["variance"], 2),
            "score:", round(result["score"], 2),
            "risk:", result["risk_label"],
            "decision:", result["decision_label"]      
        )

    print("BEST STRATEGY:", best_level, "score:", round(best_score, 2))


def main():
    best_level, best_score, results = find_best_strategy(
        risk_penalty=DEFAULT_RISK_PENALTY,
        storage_penalty_weight=DEFAULT_STORAGE_PENALTY_WEIGHT,
        runs=DEFAULT_RUNS
    )

    print_results(results, best_level, best_score)


if __name__ == "__main__":
    main()
