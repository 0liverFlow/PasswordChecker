from rich.console import Console
from rich.table import Table
import sys
from password_generator import *
console =  Console()
printc = console.print

def check_character_occurences_in_password(password_characters_occurences: int, password_characters_type: str, password_length: int) -> str:
    if password_characters_occurences == 0:
        return f"{password_characters_type.capitalize()}: [red3 b]No occurence found![/red3 b]"
    else:
        return f"{password_characters_type.capitalize()}:  [red3 b]{password_characters_occurences}/{password_length}[/red3 b]"

def check_password_characters_mixture(password_characters_occurences_dict: dict, alphanumerical_characters_list: list) -> None:
    """
    |────────────────────────────────────────────────────────────────────────────────────────|
    |In this module, we have 2 functions namely :                                            |
    |                                                                                        |
    ==> check_character_occurences_in_password                                               |
    |   This function takes 2 parameters and returns nothing :                               |
    |                                                                                        |
    |-- password_characters_occurences represents a set of                                   |
    |   character's occurence percentage in the password                                     |
    |   Here, a group or set of characters can be alphabetical                               |
    |   (upper and lower characters), numerical or a set of special characters               |
    |                                                                                        |
    |-- password_characters_type represents a group of characters's name                     |
    |   For instance password_characters_type can be                                         | 
    |   'numbers', 'upper characters', 'lower characters' or 'special characters'            |
    |________________________________________________________________________________________|
    |                                                                                        |
    ==> check_character_occurences_mixture                                                   |
    |-- It checks the mixture of password characters and display a                           |
    |   summary table of password's characters                                               |
    |                                                                                        |
    |-- This function takes 2 parameters and returns nothing :                               |
    |                                                                                        |
    |-- password_characters_occurences_dict represents a dictionary whose :                  |
    |   Keys represent the type of each group of characters(str value) and                   |
    |   Values represent the number of occurences of each group of characters (int value)    |
    |   For instance, it could be :                                                          |
    |   {'special character' : 5, 'upper character' : 8, 'number': 10, 'lower character' : 0}|
    |                                                                                        |
    |-- alphanumerical_characters_list represents a matrice(list inside a list) whose:       |
    |   Lines represent a list containing alphabetical, numerical and special characters     |
    |   used by the user when specifying their password.                                     |
    |   Columns represent a character of a particular set of characters of the same type.    |
    |   Example :                                                                            |
    |   alphanumerical_characters_list = [['a','b','c'],['1','2','5','2'],[':', '~', '!']]   |
    |________________________________________________________________________________________|
    """
    password_length = sum(password_characters_occurences_dict.values())
    found_excessive_occurences = False
    character_found_list = list()
    character_occurence_percentage = list()
    password_characters_type_percentage = 0
    #Test if the password length is correct(Which means at least 12 characters)
    printc("\n[cyan3 bold underline][+] Check the password length[/cyan3 bold underline]\n")
    if password_length < 10:
        printc("Oh nooo :/, your password length is [red3 b]'extremely short'[/red3 b]")
        printc("Password characteristics cannot be checked, because it is too short(must be at least [red3 u]12 characters long![/red3 u])")
        print("Nevertheless, let's generate a stronger password :)")
        user_choice = input("Do you wanna generate a stronger one[Yay/nay]?")
        if user_choice.lower() in ['', 'yay', 'y', 'yes']:
            password_length = int(input("Enter the password length(minimum length is 20): "))
            while password_length < 20:
                password_length = int(input("Enter the password length(minimum length is 20): "))
            sys.exit(f"Generated password: {password_generator(password_length)}")
        sys.exit('You must mind your digital life.\nOne word is enough for a wise man!')

    elif password_length < 14:
        printc(f"Password length ([red3 bold]{password_length}[/red3 bold] chars) does not meet ANSSI's password policy requirements (must be at least [green bold]14 characters[/green bold])")
        printc@("Don't forget this golden rule: [yellow b]The longer the better![/yellow b]")
        printc("[red3 u]Note:[/red3 u] Passwords like 123457890 or iloveyou123 or adminpassword will be cracked in no time")
        printc("[yellow b][!] You're better safe than sorry :-)[/yellow b]\n")
    else:
        printc(f"[green b][+][/green b] Good password length : {password_length}")
    #Test the frequence of each group of characters(alphabetical, numerical characters, symbols)
    for password_characters_type, password_characters_occurences in password_characters_occurences_dict.items():
        if password_characters_occurences < password_length // 4:
            printc(f"[red3 b][-][/red3 b] {check_character_occurences_in_password(password_characters_occurences, password_characters_type, password_length)} (must represent at least 1/4 of your password length)")
        else:
            printc(f"[green b][+][/green b] {password_characters_type.capitalize()}: {password_characters_occurences}/{password_length}")
            password_characters_type_percentage += 25
        character_occurence_percentage.append(f"{password_characters_occurences/password_length*100:.2f}%")
    #char type occurence instead of char type percentage in password
    printc("\n[cyan3 bold underline][+] Global view of password characteristics[/cyan3 bold underline]\n")
    table = Table(title="S U M M A R Y ─ T A B L E", style="bold") 
    table.add_column("Character Type", justify="center", style="green bold")
    table.add_column("Char_Type_Percentage_In_Password", justify="center", style="green bold")     
    table.add_row("Digits characters", character_occurence_percentage[1])
    table.add_row("Special characters", character_occurence_percentage[0])
    table.add_row("Lowercase characters", character_occurence_percentage[2])
    table.add_row("Uppercase Characters", character_occurence_percentage[-1])
    printc(table)
    if password_characters_type_percentage >= 75:
        printc(f"[green b][+][/green b] Password's characters mixture percentage: [green b]{password_characters_type_percentage}%[/green b]") 
    elif password_characters_type_percentage >= 50:
        printc(f"[orange_red1 b][±][/orange_red1 b] Password's characters mixture percentage: [yellow b]{password_characters_type_percentage}%[/yellow b]") 
    else:
        printc(f"[red3 b][-][/red3 b] Password's characters mixture percentage: [red3 b]{password_characters_type_percentage}%[/red3 b]") 
    printc("\n[cyan3 bold underline][+] Looking for excessive occurences\n[/cyan3 bold underline]")
    for charset_type in alphanumerical_characters_list:
        #Knowing that alphanumerical_characters_list is a matrice, charset_type will be a list
        if len(charset_type) >= 4 : #Use list's method
            for char in charset_type:
                if charset_type.count(char) > len(charset_type) // 2 and char not in character_found_list: 
                    character_occurences = charset_type.count(char)
                    found_excessive_occurences = True
                    if char.isspace():
                        printc(f"[red bold][-][/red bold] {character_occurences} occurences of space character")
                        character_found_list.append(char)
                    else:
                        printc(f"[red bold][-][/red bold] {character_occurences} occurences of {char} character")
                        character_found_list.append(char)
    if not found_excessive_occurences:
        printc("[green bold][+][/green bold] No excessive occurences of characters found!\n")
    
