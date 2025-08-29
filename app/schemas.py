from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ---------- Health ----------
class HealthOut(BaseModel):
    ok: bool
    service: str

# ---------- Users ----------
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    country: Optional[str] = None
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    class Config:
        from_attributes = True

# ---------- Vendors ----------
class VendorBase(BaseModel):
    name: str
    source_url: Optional[str] = None
    verified_score: float = 0.0
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    country: Optional[str] = None

class VendorCreate(VendorBase):
    pass

class VendorOut(VendorBase):
    id: int
    class Config:
        from_attributes = True

# ---------- Products ----------
class ProductBase(BaseModel):
    title: str
    sku: Optional[str] = None
    vendor_id: Optional[int] = None
    base_price: float = 0.0
    currency: str = "USD"
    link: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        from_attributes = True

# ---------- Orders ----------
class OrderBase(BaseModel):
    user_id: int
    product_id: int
    qty: int = 1
    est_shipping: float = 0.0
    est_customs: float = 0.0
    est_margin: float = 0.0
    total_est: float = 0.0
    status: str = "draft"

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    class Config:
        from_attributes = True
