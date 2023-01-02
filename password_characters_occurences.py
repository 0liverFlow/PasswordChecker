import string

def get_password_characters_occurences(password: str) -> tuple:
    """
    |───────────────────────────────────────────────────────────────────────────────────|
    | This module is composed of 1 function namely :                                    |
    |                                                                                   |
    ==> get_password_characters_occurences(password)                                    |
    |   This function only takes one parameter which is the user password and           |
    |   return a dictionary and a list.                                                 |
    |-- password represents the user password.                                          |
    |   Indeed, the function will try to determine how many numbers, alphabetical       |
    |   and special characters the password contains and                                |
    |   it will store them in a dictionary : password_characters_occurences_dict.       |
    |                                                                                   |
    |   alphanumerical_characters_list is just a matrice which contains lists that      |
    |   contain values of each set of characters of the same type.                      |
    |   password_characters_occurences_dict, alphanumerical_characters_list will be     |
    |   returned by the function and these 2 values.                                    |                                    
    |   will be useful for getting the password characteristics module.                 |
    |___________________________________________________________________________________|
    """
    alphabetical_characters = list()
    numerical_characters = list()
    special_characters_list = list()
    lower_characters_occurences = upper_characters_occurences = numbers_occurences = special_characters_occurences = 0
    for character in password:
        if character in string.ascii_lowercase:
            lower_characters_occurences  += 1
            alphabetical_characters.append(character)
        elif character in string.ascii_uppercase:
            upper_characters_occurences += 1
            alphabetical_characters.append(character)
        elif character in string.digits :
            numbers_occurences += 1
            numerical_characters.append(character)
        elif character in string.punctuation:
            special_characters_occurences += 1
            special_characters_list.append(character)
    password_characters_occurences_dict = {
        'special characters' : special_characters_occurences,
        'numbers' : numbers_occurences,
        'lower characters' : lower_characters_occurences,
        'upper characters' : upper_characters_occurences
    }
    alphanumerical_characters_list = [alphabetical_characters, numerical_characters, special_characters_list]
    return password_characters_occurences_dict, alphanumerical_characters_list
