from fastapi import FastAPI
import time
import requests
import uvicorn
from users.api.v1.crud import router as user_router
from config import get_settings

env = get_settings()

app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":

    uvicorn.run(app, host=env.host, port=env.port)
