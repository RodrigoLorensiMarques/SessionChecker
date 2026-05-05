from fastapi import FastAPI
from app.api.routes import router
from app.db.init_db import init_db


app = FastAPI(title="Session Checker API")

app.include_router(router)


@app.on_event("startup")
def startup():
    init_db()