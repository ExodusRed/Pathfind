# import tkinter as tk

# import view.main_menu_view

from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController

from model.settings_model import SettingsModel
from view.settings_view import SettingsView
from controller.settings_controller import SettingsController


class ViewManager:
    def __init__(self, root):
        self.root = root
        self.initialize_menu()    

    # def create_ui(self):
    #     self.main_frame = tk.Frame(self.root)
    #     self.main_frame.pack()

    # def start():

    def initialize_menu(self):
        model = MainModel()
        controller = MainController(self, model)
        view = MainView(self.root, controller)

        # view.pack(fill="both")
        view.grid()


    def initialize_settings(self):
        model = SettingsModel()
        controller = SettingsController(self, model)
        view = SettingsView(self.root, controller)

        view.pack(fill="both")
        