"""
game module having all routes from v1
"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.domains.game.engine import Engine
from app.domains.game.models import Game

router = APIRouter()


@router.get("/")
async def index():
    """fetch v1 index game endpoint

    Args:
        res (Response): a empty json object {}

    Returns:
        dict: {}
    """

    return JSONResponse(status_code=status.HTTP_200_OK, content={})


@router.get("/game", responses={status.HTTP_200_OK: {"model": Game}})
async def start_game():
    """start a new game session endpoint

    Args:
        game (Game): Game Model

        Returns:
            response: Game Model
    """
    engine = Engine()

    return JSONResponse(status_code=status.HTTP_200_OK, content=engine.game())


@router.post("/game", responses={status.HTTP_200_OK: {"model": Game}})
async def gaming(game: Game):
    """load game session and proccess new round endpoint

    Args:
        game (Game): Game Model

        Returns:
            _type_: Game Model
    """
    engine = Engine()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=engine.get_game_session(letter=game.letter, session=game.session),
    )
