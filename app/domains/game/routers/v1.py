"""
game module having all routes from v1
"""

from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get("/")
async def index(res: Response):
    """fetch v1 index game endpoint

    Args:
        res (Response): a empty json object {}

    Returns:
        dict: {}
    """
    res.status_code = status.HTTP_200_OK

    return {}
