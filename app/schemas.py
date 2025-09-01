from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


# ---------- User ----------
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=6)


class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- Auth ----------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None  # user id as string
    exp: int | None = None


# ---------- Product ----------
class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float = 0.0


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None


class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- Contact ----------
class ContactIn(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactOut(ContactIn):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- Health ----------
class HealthOut(BaseModel):
    status: str = "ok"
    db: str = "connected"
