import tkinter as tk
from Sudoku import SudokuSolver


class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")

        self.sudoku_solver = SudokuSolver()
        self.difficulty = "easy"  # Default difficulty

        self.create_widgets()

    def create_widgets(self):
        # Create a Sudoku grid (entry widgets for the user input)
        self.entries = [[tk.Entry(self.master, width=2, font=("Arial", 16))
                         for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)
                self.entries[i][j].bind('<Key>', lambda event, row=i, col=j: self.validate_input(event, row, col))

                tk.Button(self.master, text="New Puzzle", command=self.generate_puzzle).grid(row=10, column=0)
                tk.Button(self.master, text="Check Solution", command=self.check_solution).grid(row=10, column=1)
                tk.Button(self.master, text="Easy", command=lambda: self.set_difficulty("easy")).grid(row=10, column=2)
                tk.Button(self.master, text="Medium", command=lambda: self.set_difficulty("medium")).grid(row=10,
                                                                                                          column=3)
                tk.Button(self.master, text="Hard", command=lambda: self.set_difficulty("hard")).grid(row=10, column=4)

    def generate_puzzle(self):
        self.sudoku_solver.generate_puzzle(difficulty=self.difficulty)
        self.update_gui()

    def check_solution(self):
        # Implement logic to check if the user's solution is correct
        pass

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def update_gui(self):
        # Update the GUI based on the current state of the Sudoku grid
        pass

    def validate_input(self, event, row, col):
        # Implement validation logic for user input
        pass

