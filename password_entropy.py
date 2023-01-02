import math
import string

def get_entropie(user_password_length: int, password_characters_occurences_dict: dict) -> float:
    password_characters_length = 0
    for key, value in password_characters_occurences_dict.items():
        if value:
            if 'lower' in key:
                password_characters_length += len(string.ascii_lowercase)
            elif 'upper' in key:
                password_characters_length += len(string.ascii_uppercase)
            elif 'numbers' in key:
                password_characters_length += len(string.digits)
            else:
                password_characters_length += len(string.punctuation) + 1
    password_space = password_characters_length ** user_password_length
    return math.log2(password_space)

def password_level_sensibility(entropie: float) -> str:
    if entropie < 66:
        return "[red3 b][-][/red3 b] Password strength: [red3 b]very weak[/red3 b]"
    elif entropie < 85:
        return "[red b][-][/red b] Password strength: [red3 b]weak[/red3 b]"
    elif entropie < 100:
        return "[orange_red1 b][±][orange_red1 b] Password strength: [orange_red1 b]moderately good[/orange_red1 b]"
    else:
        return "[green b][+][/green b] Password strength:  [green b]good[/green b]"
