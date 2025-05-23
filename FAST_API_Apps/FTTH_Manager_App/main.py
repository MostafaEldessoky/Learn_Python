from fastapi import FastAPI
from contextlib import asynccontextmanager
from Controllers import functionalty, user
from Services import db


@asynccontextmanager
async def start_end_fun(app: FastAPI):
    await db.start_db()
    yield   


app = FastAPI(lifespan=start_end_fun)

app.include_router(user.router,prefix="/user",tags=["user"])
app.include_router(functionalty.router,prefix="/functionalty",tags=["functionalty"])
