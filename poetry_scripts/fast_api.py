"""
fast_api module have many scripts to run fast api commands
"""
import sys
from os import system as shcmd

PORT = "--port"


def server() -> None:
    """
    The function start a fast api server using a uvicorn with arguments like port
    following example:

    poetry run server --port=PORTNUMBER
    """
    args: list = sys.argv
    port: int = 8000

    for arg in args[1:]:
        argument: list = arg.split("=")
        if argument[0] == PORT:
            port = int(argument[1])

    shcmd(f"uvicorn app.core.main:app --reload --port {port}")
