import random
import copy

class SudokuSolver:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def empty(self):
        '''
        Finds the empty spots on the grid which are represented by 0 and returns them as none
        :return: (int, int) or None
        '''
        for i, row in enumerate(self.grid):
            for j, digit in enumerate(row):
                if digit == 0:
                    return (i, j)
        return None

    def display_grid(self):
        '''
        Function that displays sudoku puzzle as matrix
        '''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], end=' ')
            print()

    def valid(self, num, loc):
        '''
        Function that checks to see if a sudoku puzzle is valid
        :param num: integer that's added to a row
        :param loc: integer that's used to represent the location of a number in the grid
        :return: True if it's a valid position, False if not a valid position
        '''
        # Check row
        for i in range(9):
            if self.grid[loc[0]][i] == num:
                return False
        # Check column
        for i in range(9):
            if self.grid[i][loc[1]] == num:
                return False

        # Check 3 x 3 square
        # Given a position it finds the square that the number is in
        square_x = loc[1] // 3
        square_y = loc[0] // 3
        # Makes sure that the number doesn't appear twice in the box
        # Multiply by 3 to get the different indexes
        for i in range(square_y * 3, square_y * 3 + 3):
            for j in range(square_x * 3, square_x * 3 + 3):
                if self.grid[i][j] == num and (i, j) != loc:
                    return False
        return True

    def solve(self, rows=-1, cols=-1, nums=-1):
        '''
        Function that solves sudoku puzzles
        :param rows: integer: -1
        :param cols: integer: -1
        :param nums: integer: -1
        :return: False if none of the numbers are valid, return True if they are valid
        '''
        # Picks an empty point, tries all numbers that work until it's valid
        # Repeats until the Grid is full
        find = self.empty()
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(lst)
        if not find:
            return True
        else:
            row, col = find

        for i in lst:
            if self.valid(i, (row, col)) and not (row == rows and col == cols and nums == i):
                self.grid[row][col] = i

                if self.solve(rows, cols, nums):
                    return True
                # If solve doesn't work, it changes the value to 0 and repeats the process recursively
                self.grid[row][col] = 0

        return False

    def generate_puzzle(self):
        '''
        Function that creates a sudoku puzzle with random points marked as 0
        '''
        lst = list(range(0, 81))
        random.shuffle(lst)
        self.solve()

        count = 0
        for i in lst:
            row = i // 9
            col = i % 9
            new_grid = copy.deepcopy(self.grid)
            num = new_grid[row][col]
            new_grid[row][col] = 0
            solved_grid = self.solve(new_grid, row, col, num)
            if solved_grid is False:
                self.grid[row][col] = 0
                count += 1
                if count == 25:
                    break

    def menu(self):
        '''
        Creates a menu for solving and generating a sudoku
        '''
        ans = True
        while ans:
            make_puzzle = int(input('Enter 1 to generate a sudoku:\n'
                                    'Enter 3 to exit the program: '))
            if make_puzzle == 1:
                self.generate_puzzle()
                self.display_grid()

                sol = int(input('\n'
                                'Enter 2 to see the solved sudoku:\n'
                                'Enter 3 to exit the program: '))
                if sol == 2:
                    self.solve()
                    self.display_grid()
                elif sol == 3:
                    print('Goodbye')
                    ans = False

            elif make_puzzle == 3:
                print('Goodbye')
                ans = False
            else:
                print('Invalid Input!')


if __name__ == "__main__":
    sudoku_solver = SudokuSolver()
    sudoku_solver.menu()
