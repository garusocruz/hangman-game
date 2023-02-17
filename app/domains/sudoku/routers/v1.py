import random

from fastapi import APIRouter, Response, status

from app.domains.sudoku.engine import Engine

router = APIRouter()

from fastapi import FastAPI

app = FastAPI()


@router.get("/sudoku-game")
async def game(res: Response):
    """
    This endpoint returns a sudoku game with a random level of difficulty.
    The levels of difficulty are represented by numbers from 1 to 9.
    engine = Engine()
    :param res: Response object from FastAPI
    :type res: Response
    :return: A sudoku game with a random level of difficulty represented by a 2D list of integers.
    """
    engine = Engine()

    res.status_code = status.HTTP_200_OK

    return engine.create_sudoku(random.randint(1, 9))
