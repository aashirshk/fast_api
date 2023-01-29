from fastapi.responses import Response
import json
from fastapi import APIRouter
from utils.decorators import return_check
from typing import Any

router = APIRouter(prefix="/users")


@router.get("/{name}")
@return_check
def test_api(name: str):
    """
    The test api.

    Args:
        name (str): Test name

    Returns:
        Response: Json repsponse
    """
    return Response(content=json.dumps({"msg": f"{name}"}))
