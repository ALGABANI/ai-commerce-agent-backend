from fastapi import APIRouter
from sqlalchemy import text
from app.database import SessionLocal

# هنا ضفنا prefix = "/health"
router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")   # هتكون النتيجة: /health/
def health_check():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "db_error": str(e)}
    finally:
        db.close()
