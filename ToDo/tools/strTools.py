from re import sub

""" Toolbox for strings """

def complyWithLen(string: str, max_len: int = 4) -> bool:
    """ Check if a string is N characters long or shorter and return the corresponding boolean """
    return len(string) <= max_len

def replace_special_chars_with_underscore(input_string):
    """ Replaces special characters with underscore. This is mostly used for date processing. """
    pattern = r'[-/]'

    result = sub(pattern, '_', input_string)
    return result