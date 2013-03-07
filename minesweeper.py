# can only print out a minesweeper board currently

import random

def put_bombs(board, n_bombs):
    height, width = len(board), len(board[0])
    coords = [(x, y) for x in xrange(width) for y in xrange(height)]
    random.shuffle(coords)
    for i in xrange(n_bombs):
        x, y = coords[i]
        board[y][x] = '*'

# if n = number of bombs around coordinate i, j, then board[i][j] = n
# do nothing if current coordinate contains a bomb
def put_number(board, i, j):
    if board[i][j] != '*':
        height, width = len(board), len(board[0])
        board[i][j] = sum(1 for y in xrange(i-1, i+2) for x in xrange(j-1, j+2)
                            if 0 <= y < height and 0 <= x < width
                            if (y, x) != (i, j) and board[y][x] == '*')

# generate minesweeper board of given height, width, and number of bombs
def generate(height, width, n_bombs):
    board = []
    for _ in xrange(height):
        board.append(list([] for i in xrange(width)))
    put_bombs(board, n_bombs)

    for i in xrange(height):
        for j in xrange(width):
            put_number(board, i, j)
    return board

def print_board(board):
    for row in board:
        print ' '.join(map(str, row))    

if __name__ == "__main__":
    print_board(generate(15, 20, 100))
