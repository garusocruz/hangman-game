from pydantic import BaseModel


class Game(BaseModel):
    """This class has field email to create token of authentication"""

    session: str
    letter: str
