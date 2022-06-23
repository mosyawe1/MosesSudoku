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
        return solve(grid, row, col + 1)
    for num in range(1,10):
        if valid(gr, row, col, num):
            gr[row][col] = num
            if solve(gr, row, col + 1):
                return True
        gr[row][col] = 0
    print(grid[row][col], end=' ')
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
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if gr[corner_row+ x][corner_col + y] == num:
                return False
    return True



def empty(gr): #find empty parts of grid
    for i, row in enumerate(gr):
        for j, digit in enumerate(row):
            if digit == 0:
                return (i,j)  # row, col
    return None

#Generating Sudoku puzzles

disp_grid(grid)

