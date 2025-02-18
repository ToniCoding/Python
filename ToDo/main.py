from modules.controller.TaskController import TaskController
from modules.controller.MenuController import MenuController

def main():
    menu_instance = MenuController()
    menu_instance.generate_step_menu("./tx/english/menu.txt")

    task_controller = TaskController()
    task_controller.register_task()

if (__name__ == "__main__"):
    main()
