from fastapi import FastAPI

app = FastAPI(title="KutumbOS API")

@app.get("/")
def root():
    return {"message": "Welcome to KutumbOS"}

@app.get("/health")
def health():
    return {"status": "healthy"}