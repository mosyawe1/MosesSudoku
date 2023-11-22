import random
import copy

class SudokuSolver:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def empty(self):
        for i, row in enumerate(self.grid):
            for j, digit in enumerate(row):
                if digit == 0:
                    return (i, j)
        return None

    def display_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], end=' ')
            print()

    def valid(self, num, loc):
        for i in range(9):
            if self.grid[loc[0]][i] == num or self.grid[i][loc[1]] == num:
                return False

        square_x = loc[1] // 3
        square_y = loc[0] // 3

        for i in range(square_y * 3, square_y * 3 + 3):
            for j in range(square_x * 3, square_x * 3 + 3):
                if self.grid[i][j] == num and (i, j) != loc:
                    return False
        return True

    def solve(self, rows=-1, cols=-1, nums=-1):
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

                self.grid[row][col] = 0

        return False

    def generate_puzzle(self):
        self.solve()

        puzzle_grid = copy.deepcopy(self.grid)

        for _ in range(40):
            row, col = random.randint(0, 8), random.randint(0, 8)
            puzzle_grid[row][col] = 0

        self.grid = puzzle_grid

    def menu(self):
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
