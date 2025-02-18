from enum import Enum
from contextlib import contextmanager
from typing import Generator, IO
from os.path import isfile
from tools.logger import Logger

log = Logger("log/program.log")

class FileHandler:

    class UnsupportedOperationError(Exception):
        """ Custom exception to annouce that the introduced operation is unsupported """
        def __init__(self, message = "Operation not supported"):
            self.message = message
            super().__init__(self.message)

    class FileOperatingMode(Enum):
        """ This class serves as tracker for the current operator mode of the file hanlder """
        NONE = 0
        READ_FILE = 1
        WRITE_FILE = 2
        DELETE_FILE = 3
    
    def __init__(self, operating_mode: str):
        self.operating_mode = self.FileOperatingMode[operating_mode]

    def set_operating_mode(self, new_operating_mode: str) -> None:
        self.operating_mode = self.FileOperatingMode[new_operating_mode]
    
    def get_operating_mode(self) -> FileOperatingMode:
        return self.operating_mode
    
    @contextmanager
    # Aqui hay un problema que genera una excepción acerca de 3 argumentos dados y 2 se esperan.
    def open_file(self, path: str, mode: str) -> Generator[IO, None, None]:
        """
        Opens a file securing a correct resource management in case of an exception.

        Parameters:
        path(str): The path to the file that will be read.
        mode(str): The mode in which the file will be opened.

        Yields:
        An IO object opened in the specified mode.

        File will be automatically close after exiting the 'with' statement in which the function will be used.
        """

        try:
            file = open(path, mode)
            yield file
        finally:
            file.close()

    def write_file(self, path: str, content: str) -> bool:
        """
        Appends content to a file in a specified path.

        Parameters:
        path (str): The path to the file in which the content will be appended.
        content(str): The content to append to the file.

        Returns:
        bool: True if the content was successfully written, False otherwise

        Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path to the file is a directory.
        PermissionError: If there is a lack of permission to access the file.
        OSError: For other I/O related errors.
        """

        try:
            with open(path, "a") as opened_file:
                opened_file.write(content)
                log.info("[F_HANDLER] Successfully added contents to file.")
                return True
        except FileNotFoundError:
            log.err(f"[F_HANDLER] File at path '{path}' not found.")
        except IsADirectoryError:
            log.err(f"[F_HANDLER] The specified path '{path}' is a directory.")
        except PermissionError:
            log.err(f"[F_HANDLER] You do not have permission to access the file.")
        except OSError as err:
            log.err(f"[F_HANDLER] An I/O error has occurred: {err}")
        
        return False
        
    def read_file(self, path: str) -> str | None:
        """
        Reads a file and returns the content.

        Parameters:
        path(str): Path to the file.

        Returns:
        file_contents(str): The contents of the file that was read.
        None: If there was an exception and the file was not read.

        Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path to the file is a directory.
        PermissionError: If there is a lack of permission to access the file.
        OSError: For other I/O related errors.
        """

        try:
            with self.open_file(path, "r") as opened_file:
                file_contents = opened_file.read()
                log.info("[F_HANDLER] Successfully read contents.")
                return file_contents
        except FileNotFoundError:
            log.err(f"[F_HANDLER] File at path '{path}' not found.")
        except IsADirectoryError:
            log.err(f"[F_HANDLER] The specified path '{path}' is a directory.")
        except PermissionError:
            log.err(f"[F_HANDLER] You do not have permission to access the file.")
        except OSError as err:
            log.err(f"[F_HANDLER] An I/O error has occurred: {err}")
        
        return None

    def operate_file(self, path: str, content: str = "") -> bool:
        """
        Unique function in charge of reading and writing contents of a file. Errors are logged by each independent function, this one logs the action execution and its final state.

        Parameters:
        path(str): The path to the file that will be read or written.
        content(str): Defaulted to an empty string because it makes no sense to make it a mandatory parameter in case of READ_FILE operation.

        Returns:
        bool: Returns true if the operation is successful, returns false if any error happened.

        Raises:
        UnsupportedOperationError: If the operation mode is not supported.
        """
        current_operating_mode = self.get_operating_mode().name

        match current_operating_mode:
            case "READ_FILE" if isfile(path):
                file_contents = self.read_file(path)
                
                if file_contents is not None:
                    return True
                
            case "WRITE_FILE":
                return self.write_file(path, content)
            
            case _:
                raise self.UnsupportedOperationError(f"Operation <{current_operating_mode}> not supported.")
