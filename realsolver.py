# Program that Generates and Solves Sudokus
import random
import copy

Grid = [[0 for x in range(9)] for j in range(9)]
def solve(gr, rows = -1, cols = -1 ,nums = -1):
    '''
    Function that solves sudoku puzzles

    :param gr: list
    :param rows: integer: -1
    :param cols: integer: -1
    :param nums: integer: -1
    :return: False if none of the numbers are valid, return True if they are valid
    '''
    #Picks an empty point, tries all numbers that work until it's valid
    #Repeats until Grid is full
    find = empty(gr)
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(lst)
    if not find:
        return True
    else:
        row, col = find
    #If it's not empty then return True, indicating it's done

    for i in lst:
        if valid(gr, i, (row, col)) and not (row == rows and col == cols and nums == i):
            gr[row][col] = i

            if solve(gr, rows, cols, nums):
                return True
            #If solve doesn't work it changes the value to 0 and repeats the process recursively
            gr[row][col] = 0

    return False

def generate_puzzle():
    '''
    Function that creates a sudoku puzzle with random
    points marked as 0
    :return: list (Matrix)
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
        if solved_grid is False:
            Grid[row][col] = 0
            count += 1
            if count == 25:
                break
    return Grid


def disp_grid(gr): #display grid
    '''
    Function that displays sudoku puzzle as matrix
    :param gr: a list
    :return: a matrix
    '''
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            print(gr[i][j], end=' ')
        print()
# Check to see if the board is valid (grid, number, position)
def valid(gr, num, loc):
    '''
    Function that checks to see if a sudoku puzzle is valid
    :param gr: a list
    :param num: integer that's added to a row
    :param loc: integer that's used to represent the location of a number in the grid
    :return: True if it's a valid position, False if not a valid position
    '''
    # Check row
    for i in range(9):
        if gr[loc[0]][i] == num:
            return False
    # Check column
    for i in range(9):
        if gr[i][loc[1]] == num:
            return False

    # Check 3 x 3 square
    # Given a position it finds the square that the number is in
    square_x = loc[1] // 3
    square_y = loc[0] // 3
    # Makes sure that the number doesn't appear twice in box
    # Multiply by 3 to get the different indexes
    for i in range(square_y*3,square_y*3+3):
        for j in range(square_x*3,square_x*3+3):
            if gr[i][j] == num and (i, j) != loc:
                return False
    return True



def empty(gr): #find empty parts of grid
    '''
    Finds the empty spots on the grid which are represented by 0 and returns them as none
    :param gr: a list
    :return: returns 0's, if there is no blank squares it will return none
    '''
    for i, row in enumerate(gr):
        for j, digit in enumerate(row):
            if digit == 0:
                return (i,j)  # row, col
    return None


def menu():
    '''
    Creates a menu for solving and generating a sudoku
    :return:Returns an unsolved sudoku grid, solved Grid, and exits program
    '''
    ans = True
    while ans:
        make_puzzle = int(input('To generate a sudoku enter 1: \n'
                                'To exit the program enter 3:'))
        if make_puzzle == 1:
            puzzle = generate_puzzle()
            disp_grid(puzzle)
            sol = int(input('\n To see the solved sudoku enter 2: \n'
                            ' To exit the program enter 3: '))
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


