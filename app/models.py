from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    source_url = Column(Text, nullable=True)   # Alibaba / supplier URL
    verified_score = Column(Float, default=0)  # simple trust score 0..1
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    products = relationship("Product", back_populates="vendor")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    sku = Column(String(128), index=True, nullable=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    base_price = Column(Float, default=0.0)
    currency = Column(String(16), default="USD")
    link = Column(Text, nullable=True)  # product URL

    vendor = relationship("Vendor", back_populates="products")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    qty = Column(Integer, default=1)
    est_shipping = Column(Float, default=0.0)
    est_customs = Column(Float, default=0.0)
    est_margin = Column(Float, default=0.0)
    total_est = Column(Float, default=0.0)
    status = Column(String(32), default="draft")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")
