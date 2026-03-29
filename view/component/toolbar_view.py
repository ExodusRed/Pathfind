import tkinter as tk

# from algorithm.bfs import BFS


class ToolbarView(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print("Toolbar initializing...")

        button_frame = tk.Frame(self)

        # AlgoSelector
        algo_options = ["BFS"]
        algo_selection = None

        algo_selector = tk.OptionMenu(master=self, variable=algo_selection, value=algo_options[0])
        algo_selection = tk.StringVar(algo_selector)
        algo_selection.set(algo_options[0])
        self.config(width=100, height=100, bg="grey12")

        start_button = tk.Button(button_frame, text="Start", fg="green")
        end_button = tk.Button(button_frame, text="End", fg="red")

        # algo_selector.pack()
        # start_button.pack(fill="both")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        start_button.grid()
        end_button.grid()

        algo_selector.grid()
        

    class AlgoSelector(tk.Frame):
        def __init__(self, master):
            super().__init__()
        

    
