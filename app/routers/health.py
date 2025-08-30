from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.database import SessionLocal

router = APIRouter()

@router.get("", tags=["health"])
def health_check():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "db_error": str(e)}
    finally:
        db.close()
