import tkinter as tk

class DiagramView(tk.Canvas):
    def __init__(self, unit=100, **kwargs):
        super().__init__(**kwargs)
        # self.create_grid(unit)
        self.unit = unit
        self.starting_tile = None
        self.after(100, lambda unit=unit: self.initialize())
        # self.after(100, lambda unit=unit: self.create_grid(unit))

    def initialize(self):
        self.create_grid()
        self.create_starting_tile(1, 1)
    
    def create_starting_tile(self, column, row):
        if self.starting_tile != None: self.delete(self.starting_tile)
        self.starting_tile = self.create_rectangle(
            column * self.unit,
            row * self.unit,
            column * self.unit + self.unit,
            row * self.unit + self.unit,
            fill="red"
        )


    def create_grid(self):
        print("Creating grid...")
        self.update_idletasks()
        self.update()

        width, height = self.winfo_width(), self.winfo_height()
        # print(f"width: {width}, height: {height}")

        max_column, max_row = width // self.unit, height // self.unit

        print(f"width: {width}, height: {height}")

        self.update_idletasks()
        self.update()

        # self.create_line(0, 100, 300, 100, fill="white")

        for row in range(max_row + 1):
            print(f"row: {row}")
            self.create_line(
                0,
                row * self.unit,
                width,
                row * self.unit,
                fill="white"
            )
            print(f"x: , y: {row}")

        for column in range(max_column):
            self.create_line(
                self.unit * column,
                0,
                self.unit * column,
                height,
                fill="white"
            )

        self.update_idletasks()