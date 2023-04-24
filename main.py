from getpass import getpass
import sys

from rich import print as printc

from password_characteristics import check_character_occurences_in_password, check_password_characters_mixture
from password_characters_occurences import get_password_characters_occurences
from password_generator import password_generator
from test_password import determine_elapsed_time, format_time, crack_password
from menu import password_checker_menu
from password_entropy import get_entropy, password_level_sensibility
from have_i_been_pwned_check import check_haveibeenpwned_db


if __name__ == '__main__':
    password_checker_menu()
    user_password = getpass('Enter your passw0rd: ')
    # Checking Have I Been Pwned Database
    printc("\n[cyan3 bold underline][*] Checking HaveIBeenPwned database[/cyan3 bold underline]\n")
    printc(check_haveibeenpwned_db(user_password))

    # Checking user's password characters occurences and mixture
    password_characters_occurences_dict, alphanumerical_characters_list = get_password_characters_occurences(user_password)
    check_password_characters_mixture(password_characters_occurences_dict, alphanumerical_characters_list)
        
    # Getting the password entropy
    printc("[cyan3 bold underline][*] Password entropy[/cyan3 bold underline]\n")
    password_entropie = get_entropy(len(user_password), password_characters_occurences_dict)
    printc(password_level_sensibility(password_entropie))
    
    
    # Asking the user if they want to generate a password
    printc("\n[cyan3 bold underline][*] Password Generator[/cyan3 bold underline]\n")
    try:
        user_response = input('Do you wanna generate a password using our password generator[Yay/nay]: ')
        if user_response.lower() in ['','yay', 'yes', 'y', 'yeah', 'yep']:
            while True:
                password_length = int(input('Enter the password length: '))
                if password_length >= 20:
                    break
                printc('The password should have [red b]20[/red b] characters minimum!')
            printc(f"Generated password: [magenta2 b]{password_generator(password_length)}[/magenta2 b]\n")
    except KeyboardInterrupt:
        sys.exit(print("\nGood Bye!"))
    print("────────────────────────────────────────────────────────────────────────────")
    printc("[yellow1 b][!][/yellow1 b] Don't forget to CHANGE your password [red b]ASAP[/red b] if it was considered unsecure.")
