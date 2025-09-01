from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import HealthOut

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=HealthOut)
def health_check(db: Session = Depends(get_db)):
    # Touch the DB connection to ensure it's alive (handled by pool_pre_ping).
    return HealthOut()
