# adapted and modified from a reddit post

import random

# generate maze using depth-first search
def makemaze(height, width):
    maze = []
    for j in range(height*2+1):
        temp = ['*' for i in range(width*2+1)]
        maze.append(temp)
    maze[1][0] = maze[-2][-1] = '>'
    generate(maze, height, width)
    return maze


def generate(maze, height, width):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # in (dy, dx) coordinate
    y, x = random.randrange(1, height*2, 2), random.randrange(1, width*2, 2)
    needVisit, stack = height*width-1, [(y, x)]
    maze[y][x] = ' '
    while (needVisit > 0):
        unvisited = [(dy, dx) for dy, dx in dirs
                     if 0 <= y+2*dy < len(maze)  and 0 <= x+2*dx < len(maze[0])
                     and maze[y+2*dy][x+2*dx] == '*']
        if not unvisited:
            y, x = stack.pop(); continue
        dy, dx = random.choice(unvisited)
        maze[y+dy][x+dx] = ' '
        y, x = y + 2*dy, x + 2*dx
        maze[y][x] = ' '
        stack.append((y, x))
        needVisit -= 1


def printmaze(maze):
    for row in maze:
        print(' '.join(row))

if __name__ == '__main__':
    printmaze(makemaze(15, 20))

