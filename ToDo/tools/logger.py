from datetime import datetime
from enum import Enum

class Logger:
    def __init__(self, logPath: str) -> None:
        self.logPath = logPath

    class LoggerMode(Enum):
        """ This class will be in charge of the logging states such as information, warning, errors """
        SYSTEM = "SYS"
        INFORMATION = "INFO"
        WARNING = "WARN"
        ERROR = "ERR"
    
    def __write_log(self, logMode: str, logMsg: str) -> bool:
        """ This private method is in charge of formatting the line that is going to be writen to the logs """
        formatted_date = datetime.now().strftime("%d-%m-%YT%H:%M:%S,%f")[:-3]
        logLine = f"[{logMode}]{formatted_date} - {logMsg}"

        write_to_log = open(self.logPath, "+a").write(logLine)

        return True if write_to_log else False

    def info(self, msg: str) -> None:
        """ Logs an information message """
        self.__write_log(self.LoggerMode["INFORMATION"].value, f"{msg}\n")
    
    def sys(self, msg: str) -> None:
        """ Logs a system message """
        self.__write_log(self.LoggerMode["SYSTEM"].value, f"{msg}\n")
    
    def warn(self, msg: str) -> None:
        """ Logs a warning message """
        self.__write_log(self.LoggerMode["WARNING"].value, f"{msg}\n")
    
    def err(self, msg: str) -> None:
        """ Logs an error message. """
        self.__write_log(self.LoggerMode["ERROR"].value, f"{msg}\n")
