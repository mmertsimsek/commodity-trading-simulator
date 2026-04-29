from optimizer import find_best_strategy, calculate_score, classify_strategy
from simulator import evaluate_strategy
from app.db.models import SimulationResult


def optimize_strategy(request, db):
    best_level, best_score, results = find_best_strategy(
        risk_penalty=request.risk_penalty,
        storage_penalty_weight=request.storage_penalty_weight,
        runs=request.runs
    )

    rounded_results = []

    for result in results:
        rounded_results.append({
            "level": result["level"],
            "avg_profit": round(result["avg_profit"], 2),
            "variance": round(result["variance"], 2),
            "score": round(result["score"], 2),
            "risk_label": result["risk_label"],
            "decision_label": result["decision_label"]
        })
    best_result = next(
            result for result in results if result["level"] == best_level
    )

    db_result = SimulationResult(
            run_type="optimize",
            aggressive_level=best_level,
            avg_profit=best_result["avg_profit"],
            variance=best_result["variance"],
            score=best_result["score"],
            risk_label=best_result["risk_label"],
            decision_label=best_result["decision_label"]
)

    db.add(db_result)
    db.commit()
    db.refresh(db_result)

    return {
        "best_level": best_level,
        "best_score": round(best_score, 2),
        "results": rounded_results
    }


def simulate_single_strategy(request, db):
    avg_profit, variance = evaluate_strategy(
        aggressive_level=request.aggressive_level,
        storage_penalty_weight=request.storage_penalty_weight,
        runs=request.runs
    )

    score = calculate_score(
        avg_profit=avg_profit,
        variance=variance,
        risk_penalty=request.risk_penalty
    )

    risk_label, decision_label = classify_strategy(
        avg_profit=avg_profit,
        variance=variance,
        score=score
    )

    db_result = SimulationResult(
        run_type="simulate",
        aggressive_level=request.aggressive_level,
        avg_profit=avg_profit,
        variance=variance,
        score=score,
        risk_label=risk_label,
        decision_label=decision_label
    )    

    db.add(db_result)
    db.commit()
    db.refresh(db_result)
  
    return {
        "aggressive_level": request.aggressive_level,
        "avg_profit": round(avg_profit, 2),
        "variance": round(variance, 2),
        "score": round(score, 2),
        "risk_label": risk_label,
        "decision_label": decision_label
    }
def get_simulation_results(db):
    results = (
        db.query(SimulationResult)
        .order_by(SimulationResult.id.desc())
        .limit(20)
        .all()
    )

    return [
        {
            "id": result.id,
            "run_type": result.run_type,
            "aggressive_level": result.aggressive_level,
            "avg_profit": round(result.avg_profit, 2),
            "variance": round(result.variance, 2),
            "score": round(result.score, 2),
            "risk_label": result.risk_label,
            "decision_label": result.decision_label,
            "created_at": result.created_at,
        }
        for result in results
    ]