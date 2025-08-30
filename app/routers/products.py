from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db, Base, engine
from .. import models, schemas

# إنشاء الجداول عند الإقلاع
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/products", tags=["products"])

@router.get("", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.post("", response_model=schemas.ProductOut)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    # تأكيد البائع (إن توفر vendor_id)
    if payload.vendor_id:
        vendor = db.get(models.Vendor, payload.vendor_id)  # SQLAlchemy 2.0 way
        if not vendor:
            raise HTTPException(status_code=400, detail="Vendor not found")

    p = models.Product(
        title=payload.title,
        sku=payload.sku,
        vendor_id=payload.vendor_id,
        base_price=payload.base_price,
        currency=payload.currency,
        link=payload.link
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
