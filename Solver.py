#Pick empty square
#Try all numbers
#Find one that works
#Backtrack at point where solution cannot be completed
import random
import itertools
grid = [
    [0, 0, 6, 0, 0, 7, 0, 0, 1],
    [0, 7, 0, 0, 6, 0, 0, 5, 0],
    [8, 0, 0, 1, 0, 0, 2, 0, 0],
    [0, 0, 5, 0, 4, 0, 8, 0, 0],
    [0, 4, 0, 7, 0, 2, 0, 9, 0],
    [9, 0, 8, 0, 1, 0, 7, 0, 0],
    [0, 0, 1, 2, 0, 5, 0, 0, 3],
    [0, 6, 0, 0, 7, 0, 0, 8, 0],
    [2, 0, 0, 0, 0, 0, 4, 0, 0]
]

def solve(gr, row, col):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if gr[row][col] > 0:
        return solve(gr, row, col + 1)

    for num in range(1, 10):
        if valid(gr, row, col, num):
            gr[row][col] = num
            if solve(gr, row, col + 1):
                return True
        gr[row][col] = 0

    return False


def disp_grid(gr): #display grid
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            print(gr[i][j], end=' ')
        print()
# Check to see if the board is valid (grid, number, position)
def valid(gr, row, col, num):
    # Check row
    for i in range(9):
        if gr[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if gr[i][col] == num:
            return False

    # Check 3 x 3 box
    cube_x = row // 3
    cube_y = col // 3

    for i in range(cube_y*3,cube_y*3+3):
        for j in range(cube_x*3,cube_x*3+3):
            if gr[i][j] == num and (i,j) != row and col:
                return False
    return True



def empty(gr): #find empty parts of grid
    for i, row in enumerate(gr):
        for j, dig in enumerate(row):
            if dig == 0:
                return (i,j)  # row, col
    return None

#Generating Sudoku puzzles
def createsudoku():
    Grid = [[0 for x in range(0,9)] for y in range(0,9)]
    for i,j in itertools.product(range(9), repeat=2):
        Grid[i][j] = 0
    # The range is the amount of numbers in the grid
    for i in range(25):
        num = random.randrange(1,10)
        row = random.randrange(9)
        col = random.randrange(9)
        while(not valid(Grid, row, col, num) or Grid[row][col] != 0):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        Grid[row][col] = num

    return Grid

if solve(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
        print()

disp_grid(createsudoku())

