from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(
    title="Football AI",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "project": "Football AI",
        "status": "running"
    }