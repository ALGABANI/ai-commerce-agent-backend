# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings, get_cors_origins
from app.routers import health, auth, users, products, contact

app = FastAPI(title=settings.APP_NAME)

# CORS
origins = get_cors_origins()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if "*" in origins else origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(contact.router)

# Root
@app.get("/", tags=["root"])
def root():
    return {"ok": True, "service": settings.APP_NAME}
