from fastapi import FastAPI

app = FastAPI(
    title="Resolver API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "success": True,
        "message": "Resolver API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
