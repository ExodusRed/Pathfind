import tkinter as tk

from utils.center_window import center_window

from controller.view_manger import ViewManager


class Nodes(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.withdraw()
        # self.geometry("800x600")
        # self.center_window()
        # center_window(self)

        # self.deiconify()
        # self.update()

        # self.update_idletasks()

        self.bind("<Escape>", lambda event: self.quit())

        self.view_manager = ViewManager(self)
        self.update_idletasks()

        center_window(self)

        # self.after(500, lambda: center_window(self))

        self.update_idletasks()
        # self.update()

        # self.after(1000, lambda: self.deiconify())

        # center_window(self)

        # self.after(200, lambda: center_window(self))

        # self.center_window()
        # center_window(self)
        # self.update()
        # self.update_idletasks()
        
        # self.deiconify()
        # self.after(250, lambda: self.deiconify())

        # center_window(self)

if __name__ == "__main__":
    nodes = Nodes()
    nodes.mainloop()


        