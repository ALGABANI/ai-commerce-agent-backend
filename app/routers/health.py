from fastapi import APIRouter
from ..schemas import HealthOut

# خليه prefix واضح لتفادي خطأ "Prefix and path cannot be both empty"
router = APIRouter(prefix="/health", tags=["health"])

@router.get("", response_model=HealthOut)
def health_check():
    return {"ok": True, "service": "ai-commerce-backend"}
