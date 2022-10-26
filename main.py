from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

from apps.groupmagt.routers import router as groupmagt_router

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(
        "mongodb+srv://andy:acdwsx321@groupmagt.cgjzv3a.mongodb.net/?retryWrites=true&w=majority")
    app.mongodb = app.mongodb_client["groupMagt"]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(groupmagt_router, tags=["group_id"], prefix="/group_id")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
