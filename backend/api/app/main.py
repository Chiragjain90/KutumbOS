from fastapi import FastAPI
from routers import health
from routers import family



app = FastAPI(title="KutumbOS API")

app.include_router(health.router)

app.include_router(family.router)

@app.get("/")
def root():
    return {"message": "Welcome to KutumbOS"}