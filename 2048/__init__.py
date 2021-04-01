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

    def generate_gui(self):
        pass

    def start_game(self):
        pass
