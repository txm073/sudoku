import random
import numpy as np

def solve(board, rlevel=0):
    if rlevel == 0:
        assert np.array(board).shape == (9, 9), "Invalid board input!"
        global solved
        solved = False

    if solved:
        return

    empty = find_empty(board)
    if empty is None:
        solved = True
        return

    row, col = empty

    for i in range(1, 10):
        if validate(board, i, row, col):
            board[row][col] = i
            solve(board, rlevel+1)

    if rlevel != 0 and not solved:
        board[row][col] = 0

    if rlevel == 0 and solved:
        return np.array(board).reshape(9, 9)

def validate(board, num, row, col):
    params = list(locals().values())
    if check_row(*params) and check_column(*params) and check_box(*params):
        return True
    return False

def check_row(board, num, row, col):
    if num in board[row]:
        return False
    return True

def check_column(board, num, row, col):
    column = [board[i][col] for i in range(9)]
    if num in column:
        return False
    return True

def check_box(board, num, row, col):
    rowbox = row // 3
    colbox = col // 3
    box = []
    for _row in board[rowbox*3: rowbox*3+3]:
        box.extend(_row[colbox*3: colbox*3+3])
    if num in box:
        return False
    return True

def find_empty(board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 0:
                return i, j

def generate(level=1):
    assert type(level) is int and 0 < level < 4, \
            f"Level must be between 1 and 3, not '{level}'"

    board = []
    for i in range(9):
        row = [1] + [0] * 8
        random.shuffle(row)
        board.append(row)

    for i, row in enumerate(board):
        pass

    print(np.array(board).reshape(9, 9))


board = [
        [5, 0, 7, 2, 0, 0, 0, 9, 0],
        [0, 0, 6, 0, 3, 0, 7, 0, 1],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [1, 0, 0, 4, 9, 0, 0, 0, 7],
        [0, 0, 0, 5, 0, 8, 0, 0, 0],
        [8, 0, 0, 0, 2, 7, 0, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 0, 9],
        [2, 0, 9, 0, 8, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 9, 3, 0, 8]
        ]

board2 = [
        [0, 7, 0, 0, 2, 0, 0, 4, 6],
        [0, 6, 0, 0, 0, 0, 8, 9, 0],
        [2, 0, 0, 8, 0, 0, 7, 1, 5],
        [0, 8, 4, 0, 9, 7, 0, 0, 0],
        [7, 1, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 1, 3, 0, 4, 8, 0],
        [6, 9, 7, 0, 0, 2, 0, 0, 8],
        [0, 5, 8, 0, 0, 0, 0, 6, 0],
        [4, 3, 0, 0, 8, 0, 0, 7, 0]
         ]

print(solve(board2))
