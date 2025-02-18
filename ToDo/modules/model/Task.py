from tools.strTools import complyWithLen, replace_special_chars_with_underscore
from tools.datetimeParser import isDateFormattedCorrectly
from tools.logger import Logger
from enum import Enum

log = Logger("log/program.log")

class Task:
    class TaskStatus(Enum):
        NOT_STARTED = 1
        IN_PROGRESS = 2
        FINISHED = 3
        BLOCKED = 4

    def __init__(self, task_name: str = "None", task_description: str = "None", task_due: str = "None", task_status: bool = False) -> None:
        self.task_name = task_name
        self.task_description = task_description
        self.task_due = task_due
        self.task_status = task_status

    def get_task_name(self) -> str:
        return self.task_name
    
    def set_task_name(self, new_task_name: str) -> bool | None:
        if (not complyWithLen(new_task_name, 30)):
            log.info("[TASK] Task name cannot be longer than 30 characters.")
            return False
        
        log.info("[TASK] Correctly applied task name.")
        self.task_name = new_task_name

    def get_task_description(self) -> str:
        return self.task_description

    def set_task_description(self, new_task_description: str) -> bool | None:
        if (not complyWithLen(new_task_description, 500)):
            log.info("[TASK] Task description cannot be longer than 500 characters.")
            return False
        
        log.info("[TASK] Correctly applied task description.")
        self.task_description = new_task_description
    
    def get_task_due(self) -> str:
        return self.task_due
    
    def set_task_due(self, new_task_due: str) -> None:
        new_task_due = replace_special_chars_with_underscore(new_task_due.replace(" ", ""))
        
        if (isDateFormattedCorrectly(new_task_due)):
            log.info("[TASK] Applied date to task due.")
            self.task_due = new_task_due
        else:
            raise TypeError("Date format is incorrect.")

    def get_task_status(self) -> str:
        return self.task_status
    
    def set_task_status(self, new_task_status: TaskStatus) -> None:
        if not isinstance(new_task_status, self.TaskStatus):
            raise ValueError("new_task_status must be an instance of TaskStatus Enum")
        
        log.info(f"[TASK] Applied task status {new_task_status.name}.")

        self.task_status = new_task_status.name
    
    def get_task_details(self) -> str:
        task_details = f"{self.get_task_name()}, {self.get_task_description()}, {self.get_task_due()}, {self.get_task_status()}"

        return task_details

    def register_details(self, details: list) -> bool:
        if len(details) > 3:
            return False

        for i, detail in enumerate(details):
            match i:
                case 0:
                    self.set_task_name(detail)
                case 1:
                    self.set_task_description(detail)
                case 2:
                    self.set_task_due(detail)
                case _:
                    raise ValueError("Index of details is out of bounds.")
        
        self.set_task_status(self.TaskStatus.NOT_STARTED)

        return True
