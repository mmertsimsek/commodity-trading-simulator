from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class OptimizeRequest(BaseModel):
    runs: int = Field(default=100, ge=1, le=10000)
    risk_penalty: float = Field(default=0.1, ge=0)
    storage_penalty_weight: float = Field(default=10, ge=0)


class SimulateRequest(BaseModel):
    aggressive_level: int = Field(..., ge=1, le=6)
    storage_penalty_weight: float = Field(default=10, ge=0)
    runs: int = Field(default=100, ge=1, le=10000)
    risk_penalty: float = Field(default=0.1, ge=0)


class StrategyResult(BaseModel):
    level: int
    avg_profit: float
    variance: float
    score: float
    risk_label: str
    decision_label: str


class OptimizeResponse(BaseModel):
    best_level: int
    best_score: float
    results: List[StrategyResult]


class SimulateResponse(BaseModel):
    aggressive_level: int
    avg_profit: float
    variance: float
    score: float
    risk_label: str
    decision_label: str
class SavedSimulationResult(BaseModel):
    id: int
    run_type: str | None = None
    aggressive_level: int
    avg_profit: float
    variance: float
    score: float
    risk_label: str
    decision_label: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True