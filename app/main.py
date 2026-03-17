from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(title="Market Analysis API")

app.include_router(analyze_router)

@app.get("/")
async def root():
    return {"message": "API is running"}