from fastapi import FastAPI
from .config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return{
        "message": "Hello DeNA!",
        "status": "System is running",
        "database_url": settings.DATABASE_URL
    }

@app.post("/")
async def heals_check():
    return {'status': "ok"}