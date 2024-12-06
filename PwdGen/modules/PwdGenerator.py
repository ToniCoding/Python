""" This file contains the functional part for the password generator functionality """

# Import random and alphabet libraries, needed modules only.
from random import choice, randint
from string import ascii_letters, ascii_lowercase, ascii_uppercase, punctuation

# Class to generate the password.
class PwdGenerator:
    __special_characters = ("_", "-", "!", "#", "$")

    def __init__(self, lenght, security_level) -> None:
        self.lenght = lenght
        self.security_level = security_level

    def password_backtracking(self, password) -> dict:
        upper_chars = lower_chars = special_chars = 0

        total_count = {
            "upper_chars": 0,
            "lower_chars": 0,
            "special_chars": 0,
            "previous_four": ""
        }

        for backtrack_iteration, char in enumerate(password):
            if ( backtrack_iteration == 3 ):
                total_count["previous_four"] = password[-3]

            if ( char in ascii_lowercase ):
                lower_chars += 1
            elif ( char in ascii_uppercase ):
                upper_chars += 1
            else:
                special_chars += 1
        
        total_count["upper_chars"] = upper_chars
        total_count["lower_chars"] = lower_chars
        total_count["special_chars"] = special_chars

        return total_count


    def generator(self) -> str:
        previous_char = ""
        generated_password = ""

        upper_chars = lower_chars = special_chars = 0

        # Achieved:
        #   - Password length.
        #   - Flexibility in length for password security.
        #   - Generate a password with random letters.
        #   - Ensure the password contains special characters.
        #   - Avoid generating too many special characters but ensure they are distributed throughout the password.
        #   - Backtracking for uppercase, lowercase, and special characters.
        #   - Ensure that the same character of the same type does not repeat more than twice consecutively.
        # To achieve:
        #   - Password complexities based on difficulty level.
        
        while ( len(generated_password) < self.lenght ):
            current_pwd_lenght = len(generated_password)
            chosen_char = choice(ascii_letters)
            special_chars_needed = int((current_pwd_lenght / self.lenght) * len(generated_password))

            if ( current_pwd_lenght == 0 or current_pwd_lenght > 3):
                analysis = self.password_backtracking(generated_password)

            if ( current_pwd_lenght > 0 and generated_password[-1] == chosen_char ):
                generated_password += chosen_char
                continue

            generated_password += chosen_char
            
            if (
                randint(0, 2) % 2 == 0
                and analysis['previous_four'] not in self.__special_characters
                and special_chars < special_chars_needed
                and current_pwd_lenght > 3
            ):
                generated_password += choice(self.__special_characters)
                special_chars += 1

        return generated_password
