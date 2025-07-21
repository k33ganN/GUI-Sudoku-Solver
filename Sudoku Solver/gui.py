import tkinter as tk
from tkinter import messagebox, filedialog
from solver import solve_sudoku


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.entries = [[tk.Entry(root, width=2, font=('Arial', 18), justify='center') for _ in range(9)] for _
                        in range(9)]
        self.original_values = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                e = self.entries[i][j]
                e.grid(row=i, column=j, padx=2, pady=2)
                if (i // 3 + j // 3) % 2 == 0:
                    e.configure(bg="#e6e6e6")

        solve_button = tk.Button(root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9, pady=5)

        load_button = tk.Button(root, text="Load Puzzle from File", command=self.load_puzzle_from_file)
        load_button.grid(row=10, column=0, columnspan=9, pady=5)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val == "":
                    row.append(0)
                    self.original_values[i][j] = 0
                else:
                    try:
                        num = int(val)
                        if num < 1 or num > 9:
                            raise ValueError
                        row.append(num)
                        self.original_values[i][j] = num
                    except ValueError:
                        messagebox.showerror("Invalid Input", f"Cell ({i+1}, {j+1}) must be a number between 1-9")
                        return None
            board.append(row)
        return board

    def fill_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(board[i][j]))
                if self.original_values[i][j] == 0:
                    self.entries[i][j].config(fg='green')
                else:
                    self.entries[i][j].config(fg='black')

    def solve_puzzle(self):
        board = self.get_board()
        if board:
            if solve_sudoku(board):
                self.fill_board(board)
                messagebox.showinfo("Success", "Puzzle solved!!")
            else:
                messagebox.showerror("Unsolvable", "No solution exists for the given puzzle.")

    def load_puzzle_from_file(self):
        file_path = filedialog.askopenfilename(
            title="Open Sudoku Puzzle File",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if not file_path:
            return

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            board = []
            for line in lines:
                line = line.strip()
                if ' ' in line:
                    row = [int(num) for num in line.split()]
                else:
                    row = [int(num) for num in line]
                if len(row) != 9:
                    raise ValueError("Each row must contain 9 digits.")
                board.append(row)

            if len(board) != 9:
                raise ValueError("Puzzle must have 9 rows")

            self.load_puzzle(board)

        except Exception as e:
            messagebox.showerror("File Error", f"Failed to load puzzle:\n{e}")

    def load_puzzle(self, board):
        self.original_values = board
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(0, str(board[i][j]))
                    self.entries[i][j].config(fg='black')
                else:
                    self.entries[i][j].config(fg='black')
