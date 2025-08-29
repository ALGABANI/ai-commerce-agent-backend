from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db, Base, engine
from .. import models, schemas

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post("", response_model=schemas.UserOut)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    u = models.User(
        email=payload.email,
        name=payload.name,
        country=payload.country,
        is_active=payload.is_active
    )
    db.add(u)
    db.commit()
    db.refresh(u)
    return u
