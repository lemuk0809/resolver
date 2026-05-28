from fastapi import FastAPI
from app.database import engine

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

@app.get("/db-check")
def db_check():
    try:
        connection = engine.connect()
        connection.close()

        return {
            "database": "connected"
        }

    except Exception as e:
        return {
            "database": "error",
            "details": str(e)
        }
