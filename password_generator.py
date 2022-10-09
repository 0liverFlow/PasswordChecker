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
import random
def password_generator():
    lower_characters = "abcdefghijklmnopqrstuvwxz"
    upper_characters = lower_characters.upper()
    numbers = "0123456789"
    special_characters = "'\" #^~@<>-#*:$\\/+£"
    characters_combination = lower_characters + numbers + upper_characters + special_characters
    combination_length = len(characters_combination)
    combo = 0
    while combo < 1000:
        characters_combination = ''.join(random.sample(characters_combination, combination_length))
        combo += 1
    password_length = 0
    password_length = int(input('Enter the password length : '))
    while password_length < 12 :
        print('The password should have 12 characters length minimum!')
        password_length = int(input('Enter the password length : '))
    password =  characters_combination[:password_length]
    print(password)