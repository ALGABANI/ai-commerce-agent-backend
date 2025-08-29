from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db, Base, engine
from .. import models, schemas

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=list[schemas.OrderOut])
def list_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router.post("", response_model=schemas.OrderOut)
def create_order(payload: schemas.OrderCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).get(payload.user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    product = db.query(models.Product).get(payload.product_id)
    if not product:
        raise HTTPException(status_code=400, detail="Product not found")

    o = models.Order(
        user_id=payload.user_id,
        product_id=payload.product_id,
        qty=payload.qty,
        est_shipping=payload.est_shipping,
        est_customs=payload.est_customs,
        est_margin=payload.est_margin,
        total_est=payload.total_est,
        status=payload.status
    )
    db.add(o)
    db.commit()
    db.refresh(o)
    return o
