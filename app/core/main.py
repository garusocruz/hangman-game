"""
main module all configurations from fast api application
"""
from fastapi import FastAPI

from app.domains.game.routers import v1 as game_v1
from app.domains.sudoku.routers import v1 as sudoku_v1

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(game_v1.router, tags=["Hangman Game"])
app.include_router(sudoku_v1.router, tags=["Sudoku Game"])
