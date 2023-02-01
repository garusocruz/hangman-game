"""Game Object Model
"""
from pydantic import BaseModel


class Game(BaseModel):
    """This class has field session and letter to create Object to interact with game"""

    session: str
    letter: str
