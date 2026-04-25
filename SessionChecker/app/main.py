from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Session Checker API")

app.include_router(router)