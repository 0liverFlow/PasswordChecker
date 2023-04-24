import string
import secrets
import pyperclip

def password_generator(password_length: str) -> str:
    """
    This function takes the password length and returns a generated secured password in the clipboard.
    The minimum lenght of a generated password is 20 characters.

    :param password_length: This is the password length
    """
    string.punctuation = "!\#$%&'()*+,-./:;<= >?@[\]^_`{|}~"
    characters_combination = string.ascii_lowercase + string.punctuation + string.ascii_uppercase + string.digits
    password = ''.join(secrets.choice(characters_combination) for combo in range(password_length))
    pyperclip.copy(password)
