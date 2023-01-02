from getpass import getpass
from password_characteristics import check_character_occurences_in_password, check_password_characters_mixture
from password_characters_occurences import get_password_characters_occurences
from password_generator import password_generator
from test_password import determine_elapsed_time, format_time, crack_password
from menu import password_checker_menu
from password_entropy import get_entropy, password_level_sensibility
import time
from rich.console import Console
console = Console()
printc = console.print

if __name__ == '__main__':
    password_checker_menu()
    user_password = getpass('\nEnter your passw0rd: ')
    printc("\n[yellow b][!][/yellow b] Note: The rockyou dictionary will be used by default if no passwords dictionary is specified!\n")
    user_response = input('Would you like to specify your own dictionary path[yay/Nay]? : ')
    if user_response.lower() in ['yay', 'yes', 'y']:
        user_response = True
        passwords_dictionary_file_path = input('Thanks to specify your password dictionary file path (absolute path): ')  
    else:
        user_response = False

    #Check user's password characters occurences and mixture
    password_characters_occurences_dict, alphanumerical_characters_list = get_password_characters_occurences(user_password)
    check_password_characters_mixture(password_characters_occurences_dict, alphanumerical_characters_list)
        
    #Get the password entropy
    printc("[cyan3 bold underline][+] Password entropie[/cyan3 bold underline]\n")
    password_entropy = get_entropy(len(user_password), password_characters_occurences_dict)
    printc(password_level_sensibility(password_entropy))

    #Try to crack user password using custom password dictionary or rockyou by default
    printc("[cyan3 bold underline][+] Brute force attempt[/cyan3 bold underline]\n")
    crack_password(user_password, passwords_dictionary_file_path) if user_response else crack_password(user_password)
    
    #Ask the user if they wanna generate a password
    printc("\n[cyan3 bold underline][+] Password Generator[/cyan3 bold underline]\n")
    user_response = input('Do you wanna generate a password using the password generator[yay/Nay] : ')
    if user_response.lower() in ['yay', 'yes', 'y']:
        while True:
            password_length = int(input('Enter the password length: '))
            if password_length >= 20:
                break
            print('The password should have 20 characters minimum!')
        print(f"Generated password : {password_generator(password_length)}")
    print("────────────────────────────────────────────────────────────────\n")
    print('Feel free to hit me up for any suggestions(^_-)')
    time.sleep(2)
    print("Hmmm last thing: if your password was considered as weak, do not forget to CHANGE it ASAP(^.^)")
