from tools.FileHandler import FileHandler
from modules.controller.MenuController import MenuController

file_handler = FileHandler("READ_FILE")
menu_controller = MenuController()

class MenuView:
    LINE_DECORATOR_1 = "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
    LINE_DECORATOR_2 = "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    LINE_DECORATOR_3 = "/////////////////////////////////////////////////////////////"
    LINE_DECORATOR_4 = "#############################################################"

    def __init__(self):
        pass

    def print_menu(self) -> str:
        visual_menu = f"{self.LINE_DECORATOR_2}\nToDo Agenda --- Created by ToniCoding --- Python scripting\n{menu_controller.generate_step_menu("")}{self.LINE_DECORATOR_2}"
        return visual_menu
