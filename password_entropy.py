import math
import string

def get_entropy(user_password_length: int, password_characters_occurences_dict: dict) -> float:
    """"
    This function takes 2 parameters and return the password entropy.
    The entropy is calculated based on ANSSI's recommendations.
    https://www.ssi.gouv.fr/administration/precautions-elementaires/calculer-la-force-dun-mot-de-passe/

    :param user_password_length: As the name implies, this is the user's password length
    :param password_characters_occurences_dict: This is a dictionary representing every type of character (upper case, lower case, number, special characters) type with their respective number of occurences.
    """
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

def password_level_sensibility(entropy: float) -> str:
    if entropy < 64:
        return "[red3 b][-][/red3 b] Password entropy: [red3 b]Very weak[/red3 b]"
    elif entropy < 80:
        return "[red b][-][/red b] Password entropy: [red3 b]Weak[/red3 b]"
    elif entropy < 100:
        return "[orange_red1 b][±][orange_red1 b] Password entropy: [orange_red1 b]Moderately good[/orange_red1 b]"
    elif entropy < 130:
        return "[green b][+][/green b] Password entropy:  [green b]Good[/green b]"
    else:
        return "[green b][+][/green b] Password entropy:  [green b]Excellent[/green b]"
