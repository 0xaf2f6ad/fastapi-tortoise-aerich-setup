from fastapi import FastAPI
import uvicorn

from logic.ensure_defaults_exist import ensure_defaults_exist
from core.config import settings
from core.db import init_db
from api import v1

app = FastAPI()
app.include_router(v1.router)


@app.on_event("startup")
async def startup():
    await init_db(app=app)
    print("[+] Ensuring defaults exist")
    await ensure_defaults_exist()
    addr = f"{settings.HOST}:{settings.PORT}"
    print(f"[+] {settings.APP_NAME} all good and listening on {addr} 👍")


@app.on_event("shutdown")
async def shutdown():
    """
    Tortoise automatically closes the connection on shutdown
    can add other shutdown handlers here
    """


@app.get("/")
async def test():
    return {"detail": "The application is running", "status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )
