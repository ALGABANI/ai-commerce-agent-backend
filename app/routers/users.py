# app/routers/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Keep these imports matching your project structure
from app.database import get_db
from app import schemas, models

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/ping")
def ping_users():
    return {"ok": True, "scope": "users"}


@router.post("", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Minimal create user endpoint.
    Adjust hashing/uniqueness rules to match your project.
    """
    # Check if email exists
    existing = db.query(models.User).filter(models.User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # If you have password hashing util, replace with your helper.
    # For now, store as-is or adapt to your hashing module.
    user = models.User(
        email=payload.email,
        full_name=getattr(payload, "full_name", None),
        is_active=True,
        hashed_password=getattr(payload, "password", None),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
