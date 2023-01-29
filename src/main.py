from fastapi import FastAPI
import time
import requests
import uvicorn
from users.api.v1.crud import router as user_router
from config import get_settings
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from url_shortner.api.v1.routers import router as url_router
from utils.decorators import return_check
from fastapi_restful.inferring_router import InferringRouter


env = get_settings()

app = FastAPI()

router = InferringRouter()

app.add_middleware(TrustedHostMiddleware, allowed_hosts=env.allowed_hosts)

app.include_router(user_router)
app.include_router(url_router)


@app.get("/default")
def get_resource(resource_id: int) -> str:
    # the response will be serialized as a JSON number, *not* a string
    return resource_id


if __name__ == "__main__":

    uvicorn.run("main:app", host=env.host, port=env.port, reload=True)
