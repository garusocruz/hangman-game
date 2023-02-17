import random


def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


def is_valid(grid, row, col, num):
    # Check row constraints
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column constraints
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 subgrid constraints
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == num:
                return False

    return True


def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


def generate_grid():
    grid = [[0 for x in range(9)] for y in range(9)]
    solve(grid)
    return grid


def remove_elements(grid, n):
    count = 0
    while count < n:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count += 1
    return grid


easy_grid = generate_grid()
medium_grid = generate_grid()
hard_grid = generate_grid()

print("Easy Sudoku:")
print_grid(easy_grid)
print("\nMedium Sudoku:")
print_grid(medium_grid)
print("\nHard Sudoku:")
print_grid(hard_grid)
