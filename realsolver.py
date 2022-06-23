# Program that Generates and Solves Sudokus
import random
import copy

Grid = [[0 for x in range(9)] for j in range(9)]
def solve(gr, rows = -1, cols = -1 ,nums = -1):
    '''

    :param gr:
    :param rows:
    :param cols:
    :param nums:
    :return:
    '''

    find = empty(gr)
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    '''

    :return:
    '''
    lst = list(range(0, 81))
    random.shuffle(lst)
    Grid = [[0 for x in range(9)] for y in range(9)]
    solve(Grid)
    count = 0
    for i in lst:
        row = i // 9
        col = i % 9
        new_grid = copy.deepcopy(Grid)
        num = new_grid[row][col]
        new_grid[row][col] = 0
        solved_grid = solve(new_grid, row, col, num)
        if solved_grid == False:
            Grid[row][col] = 0
            count += 1
            if count == 25:
                break
    return Grid


def disp_grid(gr): #display grid
    '''

    :param gr:
    :return:
    '''
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            print(gr[i][j], end=' ')
        print()
# Check to see if the board is valid (grid, number, position)
def valid(gr, num, loc):
    '''

    :param gr:
    :param num:
    :param loc:
    :return:
    '''
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
    '''

    :param gr:
    :return:
    '''
    for i, row in enumerate(gr):
        for j, dig in enumerate(row):
            if dig == 0:
                return (i,j)  # row, col
    return None


def menu():
    ans = True
    while ans:
        make_puzzle = int(input('To generate a sudoku enter 1: \n'
                                'To exit the program enter 3:'))
        if make_puzzle == 1:
            puzzle = generate_puzzle()
            disp_grid(puzzle)
            sol = int(input('\n To see the solved sudoku enter 2: \n'
                            'To exit the program enter 3: '))
            if sol == 2:
                solve(puzzle,-1,-1,-1)
                disp_grid(puzzle)
            elif sol == 3:
                print('Goodbye')
                ans = False
        elif make_puzzle == 3:
            print('Goodbye')
            ans = False

menu()


