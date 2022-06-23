import random
import copy

grid = [
    [0, 0, 0, 3, 0, 0, 0, 0, 7],
    [2, 3, 8, 5, 4, 7, 6, 9, 1],
    [0, 0, 0, 0, 0, 9, 3, 8, 0],
    [0, 0, 0, 4, 0, 3, 7, 6, 2],
    [0, 0, 0, 9, 1, 0, 5, 4, 0],
    [4, 0, 0, 7, 0, 2, 0, 0, 9],
    [0, 0, 0, 8, 9, 0, 0, 0, 3],
    [8, 0, 3, 0, 0, 0, 9, 1, 4],
    [0, 0, 0, 0, 0, 0, 0, 5, 0]
]
grid2 = [
    [1, 1, 1, 1, 0, 0, 0, 0, 7],
    [2, 3, 8, 5, 4, 7, 6, 9, 1],
    [0, 0, 0, 0, 0, 9, 3, 8, 0],
    [0, 0, 0, 4, 0, 3, 7, 6, 2],
    [0, 0, 0, 9, 1, 0, 5, 4, 0],
    [4, 0, 0, 7, 0, 2, 0, 0, 9],
    [0, 0, 0, 8, 9, 0, 0, 0, 3],
    [8, 0, 3, 0, 0, 0, 9, 1, 4],
    [0, 0, 0, 0, 0, 0, 0, 5, 0]
]
grid3 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 1, 2, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
Grid = [[0 for x in range(9)] for j in range(9)]
def solve(gr,rows = -1,cols = -1,nums = -1):

    find = empty(gr)
    lst = [1,2,3,4,5,6,7,8,9]
    random.shuffle(lst)
    if not find:
        return True
    else:
        row, col = find

    for i in lst:
        if valid(gr, i, (row, col)) and not (row == rows and col == cols and nums == i):
            gr[row][col] = i

            if solve(gr, rows, cols, nums):
                return True

            gr[row][col] = 0

    return False

def generate_puzzle():
    lst = list(range(0, 81))
    random.shuffle(lst)
    Grid = [[0 for x in range(9)] for y in range(9)]
    solve(Grid)
    count = 0
    for i in lst:
        row = i//9
        col = i%9
        new_grid = copy.deepcopy(Grid)
        num = new_grid[row][col]
        new_grid[row][col] = 0
        solved_grid = solve(new_grid, row, col, num)
        if solved_grid == False:
            Grid[row][col] = 0
            count +=1
            if count == 25:
                break
    return Grid




def disp_grid(gr): #display grid
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            print(gr[i][j], end=' ')
        print()
# Check to see if the board is valid (grid, number, position)
def valid(gr, num, loc):
    # Check row
    for i in range(9):
        if gr[loc[0]][i] == num:
            return False
    # Check column
    for i in range(9):
        if gr[i][loc[1]] == num:
            return False

    # Check 3 x 3 box
    cube_x = loc[1] // 3
    cube_y = loc[0] // 3

    for i in range(cube_y*3,cube_y*3+3):
        for j in range(cube_x*3,cube_x*3+3):
            if gr[i][j] == num and (i,j) != loc:
                return False
    return True



def empty(gr): #find empty parts of grid
    for i, row in enumerate(gr):
        for j, dig in enumerate(row):
            if dig == 0:
                return (i,j)  # row, col
    return None


# Generate a sudoku puzzle

disp_grid(generate_puzzle())



