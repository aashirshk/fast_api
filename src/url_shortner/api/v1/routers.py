from fastapi.routing import APIRouter
from fastapi.responses import Response
from fastapi_restful.cbv import cbv

router = APIRouter(prefix="/urlshort")


@cbv(router)
class UrlShortner:
    @router.get("/tt")
    def get_root(self):
        return Response("Ok")
