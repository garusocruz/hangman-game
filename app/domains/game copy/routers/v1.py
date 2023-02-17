"""
game module having all routes from v1
"""

from fastapi import APIRouter, Response, status
from app.domains.game.engine import Engine
from app.domains.game.models import Game

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


@router.get("/game")
async def start_game(res: Response):
    res.status_code = status.HTTP_200_OK

    engine = Engine()

    return engine.game()


@router.post("/game")
async def start_game(game: Game, res: Response):
    res.status_code = status.HTTP_200_OK

    engine = Engine()

    return engine.get_game_session(letter=game.letter, session=game.session)


@router.get("/")
def game_status():
    # return the current game status from the BehaviorSubject
    return {"status": "playing"}


@router.post("/init")
def init_game():
    # initiate the game by calling the initGame() method
    return {"message": "game initiated"}


@router.post("/restart")
def restart_game():
    # restart the game by calling the restartGame() method
    return {"message": "game restarted"}


@router.post("/validate")
def validate_game():
    # validate the current game solution by calling the validateSolution() method
    return {"message": "solution validated"}
