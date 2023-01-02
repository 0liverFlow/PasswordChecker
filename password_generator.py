import random
import string

def password_generator(password_length):
    """
    |───────────────────────────────────────────────────────────────────────────────────|
    | This module is composed of 1 function namely :                                    |
    |                                                                                   |
    ==> password_generator()                                                            |
    |   This function has no parameter and return nothing apart displaying the          |
    |   generated password on the screen.                                               |
    |   It will generate a password based on the lower, upper,                          |
    |   special characters and numbers.                                                 |
    |   Also, one thing which is important, it is gonna generate a                      |
    |   password of 12 characters at least.                                             |
    |   When a user enters a length less than 12 characters,                            |
    |   the function will let them know about the minimum length authorized.            |
    |___________________________________________________________________________________|
    """
    string.punctuation = "!\#$%&'()*+,-./:;<= >?@[\]^_`{|}~"
    characters_combination = string.ascii_lowercase + string.punctuation + string.ascii_uppercase + string.digits
    combination_length = len(characters_combination)
    combo = 0
    while combo < 2000:
        characters_combination = ''.join(random.sample(characters_combination, combination_length))
        combo += 1
    password =  characters_combination[:password_length]
    return password
