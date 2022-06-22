import random


def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0

    # The range here is the amount
    # of numbers in the grid
    for i in range(27):
        # choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while (not CheckValid(Grid, row, col, num) or Grid[row][col] != 0):  # if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        Grid[row][col] = num

    disp_grid(Grid)

def disp_grid(gr): #display grid
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            print(gr[i][j], end=' ')
        print()

def CheckValid(Grid, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if (Grid[rowsection * 3 + x][colsection * 3 + y] == num):
                valid = False
    return valid


Grid = MakeSudoku()
print(Grid)