from tools.FileHandler import FileHandler

file_handler = FileHandler("READ_FILE")

class MenuController:
    def get_info_from_file(self, path: str, lang: str) -> list:
        file_content = file_handler.read_file(path)

    def generate_step_menu(self, steps_txt: str) -> str:
        steps_txt = file_handler.read_file(steps_txt)
        steps_txt_processed = steps_txt.split(",", maxsplit=15)
        final_menu = ""
        step_iteration = 0

        if len(steps_txt_processed) == 1:
            raise Exception("Menu components is empty.")

        for step in steps_txt_processed:
            step_iteration += 1

            final_menu += f"{step_iteration}. {step.capitalize()}.\n"
        
        print(final_menu)

        return True if len(final_menu) > 1 else False
