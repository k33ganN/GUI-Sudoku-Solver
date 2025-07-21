# 🧩 Sudoku Game & Solver

A fully functional Sudoku game built with **Python and Tkinter**, featuring:

- ✅ Manual puzzle input
- ✅ File upload support for puzzle loading
- ✅ Sudoku solving logic with backtracking
- ✅ Solution cells shown in red for clarity
- ✅ Extendable architecture (supports puzzle generation, difficulty settings, timer, and more)

---

##  Features

###  Core Features
- Enter Sudoku puzzles manually
- Upload `.txt` files containing Sudoku puzzles
- Solve puzzles using a recursive backtracking algorithm
- Visual feedback for solution cells (red highlights)

###  Architecture
- **Modular design**: GUI, solving logic, and file handling are split into separate files
- Easy to extend for future features like:
  - Random puzzle generation
  - Timed gameplay
  - Input validation with green/red feedback
  - Reset & reveal buttons

---

##  Requirements

- Python 3.10+
- Tkinter (comes pre-installed with most Python distributions)

## Format
  - Each line = one Sudoku row
  - Use 0 for blank cells

  ```
  530070000
  600195000
  098000060
  800060003
  400803001
  700020006
  060000280
  000419005
  000080079

    
