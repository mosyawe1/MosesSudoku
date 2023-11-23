import tkinter as tk
from Sudoku_Game import SudokuGame


if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()