from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ContactMessage
from app.schemas import ContactIn, ContactOut

router = APIRouter(prefix="/contact", tags=["contact"])


@router.post("/", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
def create_message(payload: ContactIn, db: Session = Depends(get_db)):
    msg = ContactMessage(name=payload.name, email=payload.email, message=payload.message)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg
