import random
import tkinter as tk

from . import colors


class Game(tk.Frame):
    def __init__(self):
        super().__init__()

        # Variables
        self.score = 0

        self.grid()

        self.master.title("2048 Python")

        self.main_grid = tk.Frame(self, bg=colors.GRID_COLOR, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(80, 0))

        self.generate_gui()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    def generate_gui(self):
        # -- Generate the cells --
        self.cells = []

        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    width=100,
                    height=100,
                    bg=colors.EMPTY_CELL_COLOR
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)

                cell_number = tk.Label(self.main_grid, bg=colors.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)

                cell_data = {"frame": cell_frame, "number": cell_number}

                row.append(cell_data)

            self.cells.append(row)

        # -- Score section --
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=40, anchor="center")

        tk.Label(
            score_frame,
            text="Score",
            font=colors.SCORE_LABEL_FONT
        ).grid(row=0)

        self.score_label = tk.Label(score_frame, text="0", font=colors.SCORE_FONT)
        self.score_label.grid(row=1)

    def start_game(self):
        # Generate empty matrix
        self.matrix = [[0] * 4 for i in range(4)]

        # Fill random cells with 2s
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        self.matrix[row][col] = 2

        self.cells[row][col]["frame"].configure(bg=colors.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            text="2",
            bg=colors.CELL_COLORS[2],
            fg=colors.CELL_NUMBER_COLORS[2],
            font=colors.CELL_NUMBER_FONTS[2]
        )

        while self.matrix[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        self.matrix[row][col] = 2

        self.cells[row][col]["frame"].configure(bg=colors.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            text="2",
            bg=colors.CELL_COLORS[2],
            fg=colors.CELL_NUMBER_COLORS[2],
            font=colors.CELL_NUMBER_FONTS[2],
        )

    def add_new_tile(self):
        """Add a new tile of 2 or 4 randomly."""
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    # -- Matrix operations --
    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]

        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]

        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix
