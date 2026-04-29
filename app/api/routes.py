from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal

from app.schemas.simulation import (
    OptimizeRequest,
    SimulateRequest,
    OptimizeResponse,
    SimulateResponse,
    SavedSimulationResult,
)

from app.services.trading_service import (
    optimize_strategy,
    simulate_single_strategy,
    get_simulation_results,
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/optimize", response_model=OptimizeResponse)
def optimize(request: OptimizeRequest, db: Session = Depends(get_db)):
    return optimize_strategy(request, db)


@router.post("/simulate", response_model=SimulateResponse)
def simulate(request: SimulateRequest, db: Session = Depends(get_db)):
    return simulate_single_strategy(request, db)


@router.get("/results", response_model=List[SavedSimulationResult])
def get_results(db: Session = Depends(get_db)):
    return get_simulation_results(db)