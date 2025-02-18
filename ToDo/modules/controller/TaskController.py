from tools.FileHandler import FileHandler
from tools.datetimeParser import monthTranslator, getDateDetails
from modules.model.Task import Task
from os.path import exists
from os import makedirs

file_hanlder = FileHandler("WRITE_FILE")

class TaskController:
    def __init__(self) -> None:
        pass
    
    def register_task(self) -> bool:
        task = Task()
        task_details = input("Details of your new task (name, description, date)\n").split(",")

        try:
            task.register_details(task_details)
            task_content = f"{task.get_task_details()}\n"

            date_details = getDateDetails("ym")
            form_path = f"tasks/{date_details[0]}/{monthTranslator((date_details[1]) - 1)}"

            makedirs(form_path, exist_ok=True)

            with open(f"{form_path}/tasks.txt", "w") as task_file:
                pass
        
            return True if file_hanlder.write_file(f"{form_path}/tasks.txt", task_content) else False
        
        except Exception as e:
            print(f"An exception ocurred: {e}")