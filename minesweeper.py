# can only print out a minesweeper board currently
#
# Sample output:
# print_board(generate(15, 20, 100))
"""
* 2 * * 4 * * * * 3 * * 3 1 2 * 3 3 2 1
1 2 3 * 4 * 5 5 3 4 * * 4 * 4 5 * * * 1
0 1 2 2 2 2 * 3 * 3 5 * 6 4 * * * * 3 1
0 1 * 1 1 2 3 * 2 2 * * * * 4 6 * 5 2 1
0 1 1 1 2 * 4 3 2 3 3 5 * 4 3 * * 4 * 3
2 2 1 0 3 * * 3 * 3 * 3 3 * 4 4 3 3 * *
* * 2 0 2 * 3 3 * 3 1 3 * 4 * * 3 3 4 3
* * 3 1 3 2 3 2 2 1 0 2 * 3 3 * 4 * * 2
* 4 4 * 3 * 2 * 1 1 1 2 2 2 2 1 4 * * 2
2 * 4 * 5 4 4 3 2 3 * 2 1 * 1 0 2 * 4 2
2 3 * 5 * * * 5 * 4 * 2 1 1 1 1 2 4 * 3
1 * 3 * * 6 * * * 4 2 3 2 1 0 1 * 4 * *
2 2 3 3 4 * 5 6 * 2 1 * * 1 1 2 2 3 * 4
* 1 1 * 2 3 * * 2 2 2 3 3 2 2 * 2 3 4 *
1 1 1 1 1 2 * 3 1 1 * 1 1 * 2 1 2 * * 2
"""

import random

def put_bombs(board, n_bombs):
    height, width = len(board), len(board[0])
    coords = [(x, y) for x in range(width) for y in range(height)]
    random.shuffle(coords)
    for i in range(n_bombs):
        x, y = coords[i]
        board[y][x] = '*'

# if n = number of bombs around coordinate i, j, then board[i][j] = n
# do nothing if current coordinate contains a bomb
def put_number(board, i, j):
    if board[i][j] != '*':
        height, width = len(board), len(board[0])
        board[i][j] = sum(1 for y in range(i-1, i+2) for x in range(j-1, j+2)
                            if 0 <= y < height and 0 <= x < width
                            if (y, x) != (i, j) and board[y][x] == '*')

# generate minesweeper board of given height, width, and number of bombs
def generate(height, width, n_bombs):
    board = []
    for _ in range(height):
        board.append(list([] for i in range(width)))
    put_bombs(board, n_bombs)

    for i in range(height):
        for j in range(width):
            put_number(board, i, j)
    return board

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    print_board(generate(15, 20, 100))
