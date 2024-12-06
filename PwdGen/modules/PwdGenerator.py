""" This file contains the functional part for the password generator functionality """

# Import random and alphabet libraries, needed modules only.
from random import choice, randint
from string import ascii_letters, ascii_lowercase, ascii_uppercase

# Class to generate the password.
class PwdGenerator:
    __special_characters = ("_", "-", "!", "#", "$")

    def __init__(self, lenght, security_level) -> None:
        self.lenght = lenght
        self.security_level = security_level

    def analyze_password_structure(self, password) -> dict:
        structure_analysis = {
            "last_four_chars": password[-4:] if len(password) >= 4 else "",
            "length": len(password),
        }

        return structure_analysis

    def password_backtracking(self, password) -> dict:
        upper_chars = lower_chars = special_chars = 0

        total_count = {
            "upper_chars": 0,
            "lower_chars": 0,
            "special_chars": 0,
        }

        for char in password:
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

    def should_add_special_char(self, special_chars, special_chars_needed, structure_analysis, current_pwd_lenght) -> bool:
        has_special_chars_left = special_chars < special_chars_needed
        random_choice = randint(0, 2) % 2 == 0
        no_special_in_last_four = structure_analysis['last_four_chars'] not in self.__special_characters
        has_space_for_more = current_pwd_lenght < self.lenght

        return has_special_chars_left and random_choice and no_special_in_last_four and has_space_for_more
    
    def generator(self) -> str:
        generated_password = ""
        special_chars = 0
        
        while ( len(generated_password) < self.lenght ):
            current_pwd_lenght = len(generated_password)
            chosen_char = choice(ascii_letters)
            special_chars_needed = max(1, int(self.lenght * 0.15)) # Percentage of amount of special characters in generated password have to vary based on security level.

            if current_pwd_lenght > 0 and generated_password[-1] == chosen_char:
                generated_password += chosen_char
                continue

            if current_pwd_lenght == 0 or current_pwd_lenght > 3:
                structure_analysis = self.analyze_password_structure(generated_password)

            generated_password += chosen_char
            
            if ( self.should_add_special_char(special_chars, special_chars_needed, structure_analysis, current_pwd_lenght) ):
                generated_password += choice(self.__special_characters)
                special_chars += 1

            if ( current_pwd_lenght > self.lenght ):
                generated_password = generated_password[:self.lenght]

        return generated_password
