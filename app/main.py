from fastapi import FastAPI
from .routers import health, products

app = FastAPI(title="AI Commerce Agent")

# Routers
app.include_router(health.router)
app.include_router(products.router)
