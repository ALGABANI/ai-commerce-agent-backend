from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db, Base, engine
from .. import models, schemas

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/vendors", tags=["vendors"])

@router.get("", response_model=list[schemas.VendorOut])
def list_vendors(db: Session = Depends(get_db)):
    return db.query(models.Vendor).all()

@router.post("", response_model=schemas.VendorOut)
def create_vendor(payload: schemas.VendorCreate, db: Session = Depends(get_db)):
    v = models.Vendor(
        name=payload.name,
        source_url=payload.source_url,
        verified_score=payload.verified_score,
        contact_email=payload.contact_email,
        contact_phone=payload.contact_phone,
        country=payload.country
    )
    db.add(v)
    db.commit()
    db.refresh(v)
    return v
