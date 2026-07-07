from fastapi import FastAPI
from routers import health

app = FastAPI(title="KutumbOS API")

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to KutumbOS"}