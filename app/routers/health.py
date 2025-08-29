from fastapi import APIRouter
from ..schemas import HealthOut

router = APIRouter(prefix="", tags=["health"])

@router.get("/", response_model=HealthOut)
def root_health():
    return {"ok": True, "service": "ai-commerce-backend"}
