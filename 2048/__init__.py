import random
import tkinter as tk

from . import colors


class Game(tk.Frame):
    def __init__(self):
        super().__init__()

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
        pass
