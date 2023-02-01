"""
main module all configurations from fast api application
"""
from fastapi import FastAPI

from app.domains.game.routers import v1 as game_v1

app = FastAPI()
app.include_router(game_v1.router, tags=["Hangman Game"])
