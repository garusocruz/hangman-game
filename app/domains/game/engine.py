"""
engine module is provided with ChatGPT help
"""

import base64
import json
import random
from datetime import datetime, timedelta


class Engine:
    """Engine Class Object

    Returns:
        _type_
    """

    ASCII_LOWERCASE_START = 97
    ALPHABET_LENGTH = 26

    def __init__(self) -> None:
        """Initialize class object

        Args:
            session (str, optional): Defaults to None.
        """
        self.words = [
            "python",
            "algorithm",
            "debugging",
            "performance",
            "optimization",
            "software",
            "development",
            "coding",
            "architecture",
            "design",
        ]

        self.key: int
        self.masked_word: str
        self.turns: str

        # Select a random word from the words list
        self.secret_word = random.choice(self.words)

        # Create a variable called word to store the word that is being guessed
        self.word = ["_"] * len(self.secret_word)

        # Create a variable called turns and set it to a value.
        self.max_turns = 6

    def run(self, letter: str = ""):
        """Create a loop that runs until the turns variable is equal
        to 0 or the secret_word has been guessed correctly

        Args:
            letter (str, optional): Defaults to "".

        Returns:
            str: containing a encrypted word
        """
        turns = self.turns

        if turns == 0:
            return "Sorry, the bomb has exploded."

        if self.max_turns == turns:
            self.turns -= 1

        self.masked_word = (
            self.masked_word
            if hasattr(self, "masked_word")
            else ("".join(self.word) if " " in self.word else " ".join(self.word))
        )

        letter = letter.lower()

        if letter in self.secret_word:
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    self.word[i] = letter
                    self.masked_word = self.masked_word.split(" ")
                    self.masked_word[i] = self.word[i]
                    self.masked_word = " ".join(self.masked_word)

        else:
            self.turns -= 1

        if "_" not in self.masked_word:
            self.turns -= 1
            return "Congratulations! You have disarmed the bomb."

        return self.masked_word

    def encrypt(self, text, key: int = None):
        """Caesar Cipher encryption function

        Args:
            text (str): str to encrypt
            key (int, optional): _description_. Defaults to None.

        Returns:
            str: str encripted
        """
        if not key and hasattr(self, "key"):
            key = self.key

        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted_char = chr(
                    (ord(char) + key - self.ASCII_LOWERCASE_START)
                    % self.ALPHABET_LENGTH
                    + self.ASCII_LOWERCASE_START
                )
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text, key: int = None):
        """Caesar Cipher decryption function

        Args:
            text (str): str to decrypt
            key (int, optional): Defaults to None.

        Returns:
            str: str decripted
        """
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted_char = chr(
                    (ord(char) - key - self.ASCII_LOWERCASE_START)
                    % self.ALPHABET_LENGTH
                    + self.ASCII_LOWERCASE_START
                )
                decrypted_text += shifted_char
            else:
                decrypted_text += char
        return decrypted_text

    def game(self, letter: str = "", key: int = random.randint(1, 25)):
        """Execute round game

        Args:
            letter (str, optional): Defaults to "".
            key (int, optional): Defaults to random.randint(1, 25).

        Returns:
            dict: {
            "session_id": str,
            "message": str,
        }
        """
        # Create an instance of the Caesar Cipher algorithm and set the key
        self.key = key

        # Create an instance of the Caesar Cipher algorithm and set the key
        self.turns = self.max_turns if not hasattr(self, "turns") else self.turns

        response = self.run(letter)

        secret = self.encrypt(self.secret_word)

        json_encoded = json.dumps(
            {
                "secret": secret,
                "key": key,
                "timestamp": (datetime.now() + timedelta(seconds=600)).timestamp(),
                "turns": self.turns,
                "masked_word": self.masked_word,
            }
        )

        session_id = base64.b64encode(
            self.encrypt(json_encoded, key=23).encode("utf-8")
        ).decode("utf-8")

        return {
            "session_id": session_id,
            "message": response,
        }

    def get_game_session(self, session: str, letter: str = ""):
        """Load game session and execute a new round game

        Args:
            session (str): base b4 with historic of game
            letter (str, optional): Defaults to "".

        Returns:
            dict: {
            "session_id": session_id,
            "message": response,
        }
        """
        session: dict = json.loads(
            self.decrypt(base64.b64decode(session).decode("utf-8"), key=23)
        )
        # Load an instance of the Caesar Cipher algorithm and set the key
        self.key = session["key"]

        # Load a variable called turns and set it to a value.
        self.turns = session["turns"]

        # Load a variable called secred_word and set it to a value.
        self.secret_word = self.decrypt(session["secret"], key=self.key)

        # update a variable called word and set it to a value.
        self.word = ["_"] * len(self.secret_word)

        # Load a variable called secred_word and set it to a value.
        self.masked_word = session["masked_word"]

        return self.game(key=self.key, letter=letter)
