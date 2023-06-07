from getpass import getpass
import sys

from rich import print as printc

from password_characteristics import check_character_occurences_in_password, check_password_characters_mixture
from password_characters_occurences import get_password_characters_occurences
from password_generator import password_generator
from password_entropy import get_entropy, password_level_sensibility
from have_i_been_pwned_check import check_haveibeenpwned_db


if __name__ == '__main__':
    # Display banner
    print("""
                 .--------.
                / .------. \\
               / /        \ \\
               | |        | |
              _| |________| |_
            .' |_|P4SSW0RD|_| '.
            '._____ ____ _____.'
            |     .'_____'.    |
            '.__.'.'     '.'.__'
            '.__  | CHECK |  __'
            |   '.'.____.'.'   |
            '.____'.____.'____.'
            '.________________.'Author: 0LIVERFLOW | Version: 1.0
            \n""")    
    user_password = getpass('Enter your passw0rd: ')
    # Checking Have I Been Pwned Database
    printc("\n[cyan3 bold underline][*] Checking HaveIBeenPwned database[/cyan3 bold underline]")
    printc(check_haveibeenpwned_db(user_password))

    # Checking user's password characters occurences and mixture
    password_characters_occurences_dict, alphanumerical_characters_list = get_password_characters_occurences(user_password)
    check_password_characters_mixture(password_characters_occurences_dict, alphanumerical_characters_list)
        
    # Getting the password entropy
    printc("[cyan3 bold underline][*] Password entropy[/cyan3 bold underline]")
    password_entropie = get_entropy(len(user_password), password_characters_occurences_dict)
    printc(password_level_sensibility(password_entropie))
    
    # Asking the user if they want to generate a password
    printc("\n[cyan3 bold underline][*] Password Generator[/cyan3 bold underline]")
    try:
        user_response = input('Do you wanna generate a password using our password generator [Yay/nay]: ')
        if user_response.lower() in ['','yay', 'yes', 'y', 'yeah', 'yep']:
            while True:
                password_length = input('Enter the password length: ')
                if password_length.isdigit() and int(password_length) >= 20:
                    break
                printc('The password should have [red b]20[/red b] characters minimum!')
            password_generator(int(password_length))
            printc(f"[green1 b][+][/green1 b] The generated password was securely copied in your clipboard!")
    except KeyboardInterrupt:
        sys.exit(print("\nGood Bye!"))
    print("────────────────────────────────────────────────────────────────────────────")
    printc("[yellow1 b][!][/yellow1 b] Don't forget to [red1 b]CHANGE[/red1 b] your password [red1 b]ASAP[/red1 b] if it was considered unsecure.")
