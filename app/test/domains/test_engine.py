"""test Engine module
"""
from unittest import TestCase, mock

from app.domains.game.engine import Engine


class TestEngine(TestCase):
    """TestEngine Module

    Args:
        TestCase
    """

    def setUp(self):
        """initialize engine"""
        self.engine = Engine

    @mock.patch("random.choice", return_value="python")
    def test_encrypt(self, __):
        """test encrypt a str with success

        Args:
            __ (str): default str value
        """
        engine = self.engine()

        self.assertEqual(engine.encrypt("python", 5), "udymts")

    @mock.patch("random.choice", return_value="python")
    def test_decrypt(self, __):
        """test decrypt a str with success

        Args:
            __ (str): default str value
        """
        engine = self.engine()

        self.assertEqual(engine.decrypt("udymts", 5), "python")

    @mock.patch("random.choice", return_value="python")
    def test_start_game(self, __):
        """test if a game is started with success

        Args:
            __ (str): default str value
        """
        engine = Engine()
        response = engine.game()
        print(response)
        self.assertIn("session_id", response)
        self.assertIn("message", response)
        self.assertIn(response["message"], "_ _ _ _ _ _")

    @mock.patch("random.choice", return_value="python")
    def test_run_success_input_word(self, __):
        """test if a round game have a success requesting a letter

        Args:
            __ (str): default str value
        """
        session_id = "eyJwYnpvYnEiOiAiYmtmdGF6IiwgImhidiI6IDE1LCAicWZqYnBxeGptIjogMTY3NTE5NzExMy4yNDQzMzksICJxcm9rcCI6IDEsICJqeHBoYmFfdGxvYSI6ICJfIF8gXyBfIF8gXyJ9"
        engine = Engine()
        response = engine.get_game_session(letter="p", session=session_id)

        self.assertIn(response["message"], "p _ _ _ _ _")

    @mock.patch("random.choice", return_value="python")
    def test_run_success_win_a_game(self, __):
        """test if the game ends with a winner

        Args:
            __ (str): default str value
        """
        session_id = "eyJwYnpvYnEiOiAiYmtmdGF6IiwgImhidiI6IDE1LCAicWZqYnBxeGptIjogMTY3NTE5NzExMy4yNDQzMzksICJxcm9rcCI6IDYsICJqeHBoYmFfdGxvYSI6ICJfIF8gXyBfIF8gXyJ9"  # no-qa
        engine = Engine()
        response = engine.get_game_session(letter="p", session=session_id)
        # response = engine.get_game_session(letter="a", session=session_id)
        response = engine.get_game_session(letter="y", session=response["session_id"])
        response = engine.get_game_session(letter="t", session=response["session_id"])
        response = engine.get_game_session(letter="h", session=response["session_id"])
        response = engine.get_game_session(letter="o", session=response["session_id"])
        response = engine.get_game_session(letter="n", session=response["session_id"])

        self.assertEqual(
            response["message"], "Congratulations! You have disarmed the bomb."
        )

    @mock.patch("random.choice", return_value="python")
    def test_run_success_decrease_turn(self, __):
        """test if the the rounds are managed right

        Args:
            __ (str): default str value
        """
        session_id = "eyJwYnpvYnEiOiAiYmtmdGF6IiwgImhidiI6IDE1LCAicWZqYnBxeGptIjogMTY3NTE5NzExMy4yNDQzMzksICJxcm9rcCI6IDYsICJqeHBoYmFfdGxvYSI6ICJfIF8gXyBfIF8gXyJ9"  # no-qa
        engine = Engine()
        response = engine.get_game_session(letter="a", session=session_id)
        response = engine.get_game_session(letter="y", session=response["session_id"])

        print(response)
        self.assertEqual(response["message"], "_ y _ _ _ _")

    @mock.patch("random.choice", return_value="python")
    def test_run_lose_a_game(self, __):
        """test if the game ends with a loser

        Args:
            __ (str): default str value
        """
        session_id = "eyJwYnpvYnEiOiAiYmtmdGF6IiwgImhidiI6IDE1LCAicWZqYnBxeGptIjogMTY3NTE5NzExMy4yNDQzMzksICJxcm9rcCI6IDAsICJqeHBoYmFfdGxvYSI6ICJfIF8gXyBfIF8gXyJ9"  # no-qa
        engine = Engine()
        response = engine.get_game_session(letter="w", session=session_id)

        self.assertIn(response["message"], "Sorry, the bomb has exploded.")
