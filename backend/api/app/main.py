from fastapi import FastAPI
from routers import health
from routers import family
from routers import shopping
from routers import bills



app = FastAPI(title="KutumbOS API")

app.include_router(health.router)

app.include_router(family.router)
app.include_router(shopping.router)
app.include_router(bills.router)

@app.get("/")
def root():
    return {"message": "Welcome to KutumbOS"}