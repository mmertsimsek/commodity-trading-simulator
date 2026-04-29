from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from app.db.database import Base


class SimulationResult(Base):
    __tablename__ = "simulation_results"

    id = Column(Integer, primary_key=True, index=True)

    run_type = Column(String)

    aggressive_level = Column(Integer)
    avg_profit = Column(Float)
    variance = Column(Float)
    score = Column(Float)

    risk_label = Column(String)
    decision_label = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)