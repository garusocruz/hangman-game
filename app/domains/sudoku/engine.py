import random

import numpy as np


class Engine:
    def search_none_cells(self, masked_board):
        """
        This function searches for the first cell with a value of 0 (empty cell) in the masked sudoku board.
        :param self: Object of the class that this function belongs to.
        :param masked_board: 2D numpy array representing the masked sudoku board.
        :type masked_board: numpy.ndarray
        :return: A numpy array with three elements: [row, col, Fill_Chk], where row and col represent the coordinates
        of the empty cell, and Fill_Chk is set to 1 if an empty cell is found and 0 if not.
        :rtype: numpy.ndarray
        """
        for i in range(9):
            for j in range(9):
                if masked_board[i, j] == 0:
                    row = i
                    col = j
                    Fill_Chk = 1
                    res = np.array([row, col, Fill_Chk], dtype="int8")
                    return res
        res = np.array([-1, -1, 0])
        return res

    def validate_game(self, masked_board, row, col, num):
        """
        This function validates if a given number can be placed in a specific cell in the sudoku board.
        :param self: Object of the class that this function belongs to.
        :param masked_board: 2D numpy array representing the masked sudoku board.
        :type masked_board: numpy.ndarray
        :param row: Row coordinate of the cell to be validated.
        :type row: int
        :param col: Column coordinate of the cell to be validated.
        :type col: int
        :param num: Number to be validated.
        :type num: int
        :return: A boolean indicating if the number can be placed in the cell (True) or not (False).
        :rtype: bool
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        if num in masked_board[:, col] or num in masked_board[row, :]:
            return False
        if num in masked_board[row_start : row_start + 3, col_start : col_start + 3]:
            return False
        return True

    def get_masked_game(self, masked_board, difficulty):
        """
        This function generates a masked sudoku board based on the selected difficulty level.
        :param self: Object of the class that this function belongs to.
        :param masked_board: 2D numpy array representing the sudoku board.
        :type masked_board: numpy.ndarray
        :param difficulty: Difficulty level of the sudoku game. The options are: "Easy", "Medium", "Hard".
        :type difficulty: str
        :return: A masked sudoku board with values filled according to the selected difficulty level.
        :rtype: numpy.ndarray
        """
        count, done = 0, False
        if difficulty is "Easy":
            print("Easy Difficulty Puzzle Generating...\n\n")
            upper_limit = 35
        elif difficulty is "Medium":
            print("Medium Difficulty Puzzle Generating...\n\n")
            upper_limit = 41
        else:
            print("Hard Difficulty Puzzle Generating...\n\n")
            upper_limit = 47
        while True:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if count <= upper_limit:
                if masked_board[i, j] != 0:
                    not_check = masked_board[i, j]
                    masked_board[i, j] = 0
                    masked_board_copy = masked_board
                    if self.win_game(masked_board_copy, not_check):
                        masked_board[i, j] = not_check
                        continue
                    row_start = (i // 3) * 3
                    col_start = (j // 3) * 3
                    if difficulty is "Easy":
                        if (
                            np.count_nonzero(
                                masked_board[
                                    row_start : row_start + 3, col_start : col_start + 3
                                ]
                            )
                            < 5
                        ):
                            masked_board[i, j] = not_check
                            continue
                    elif difficulty is "Medium":
                        if (
                            np.count_nonzero(
                                masked_board[
                                    row_start : row_start + 3, col_start : col_start + 3
                                ]
                            )
                            < 4
                        ):
                            masked_board[i, j] = not_check
                            continue
                    else:
                        if (
                            np.count_nonzero(
                                masked_board[
                                    row_start : row_start + 3, col_start : col_start + 3
                                ]
                            )
                            < 3
                        ):
                            masked_board[i, j] = not_check
                            continue
                    count += 1
            else:
                break

    def win_game(self, masked_board, not_check):
        """
        This function is used to solve the sudoku game by filling in the empty cells with numbers that are not
        in the same row, column, or 3x3 square as the number being checked. The function uses a backtracking
        algorithm.
        :param self: Object of the class that this function belongs to.
        :param masked_board: 2D numpy array representing the masked sudoku board.
        :param not_check: The number that is being checked for validity.
        :type masked_board: numpy.ndarray
        :type not_check: int
        :return: Boolean value indicating if the game can be solved or not.
        :rtype: bool
        """
        x = self.search_none_cells(masked_board)
        if x[2] == 0:
            return True
        else:
            row = x[0]
            col = x[1]
            for i in np.random.permutation(10):
                if i != 0 and i != not_check:
                    if self.validate_game(masked_board, row, col, i):
                        masked_board[row, col] = i
                        if self.win_game(masked_board, not_check):
                            return True
                        masked_board[row, col] = 0
        return False

    def create_sudoku(self, ch=random.randint(1, 3)):
        """
        This function creates a sudoku game with a specified level of difficulty.
        :param self: Object of the class that this function belongs to.
        :param ch: Level of difficulty of the game (1: Easy, 2: Medium, 3: Hard).
        :type ch: int
        :return: A list of dictionaries, where each dictionary represents a row in the sudoku board,
        containing information about each cell, such as its value, placeholder, editability, and selection status.
        :rtype: list
        """

        if ch == 1:
            difficulty = "Easy"
        elif ch == 2:
            difficulty = "Medium"
        else:
            difficulty = "Hard"
        masked_board = np.zeros((9, 9), dtype="int8")

        if self.win_game(masked_board, -1):
            result = []
            masked_board = masked_board

            board = masked_board.copy()
            board = board.tolist()

            self.get_masked_game(masked_board, difficulty)
            masked_board = masked_board.tolist()

            for i in range(len(board)):
                row = {"id": i + 1, "cels": []}
                for j in range(len(board[i])):
                    placeholder = None if not masked_board[i][j] else board[i][j]
                    isEditable = True if not masked_board[i][j] else False
                    isSelected = False
                    row["cels"].append(
                        {
                            "id": j + 1,
                            "value": board[i][j],
                            "placeholder": placeholder,
                            "isEditable": isEditable,
                            "isSelected": isSelected,
                        }
                    )
                result.append(row)
            return result
        return
