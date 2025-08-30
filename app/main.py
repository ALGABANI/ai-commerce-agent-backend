from fastapi import FastAPI
from .routers import health, products

app = FastAPI(title="AI Commerce Agent")

# Root (اختياري)
@app.get("/")
def root():
    return {"ok": True, "service": "ai-commerce-backend"}

# Routers
app.include_router(health.router)
app.include_router(products.router)
