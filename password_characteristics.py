from rich import print as printc
from rich.table import Table


def check_character_occurences_in_password(password_characters_occurences: int, password_characters_type: str, password_length: int) -> str:
    if password_characters_occurences == 0:
        return f"{password_characters_type.capitalize()}: [red3 b] No occurence found![/red3 b]"
    else:
        return f"{password_characters_type.capitalize()}: [red3 b]{password_characters_occurences}/{password_length}[/red3 b]"

def check_password_characters_mixture(password_characters_occurences_dict: dict, alphanumerical_characters_list: list) -> None:
    """
    This function takes 2 parameters and checks the type of characters that compose a password,
    then displays a summary table of a given password's characters percentage.
    
    :param password_characters_occurences_dict: This is a dictionary whose keys represent 
    the type of each group of characters (special characters, numbers, ect...) and whose values represent the number of occurences
    of each group of characters (int value).
    Ex: {'special character' : 5, 'upper character' : 8, 'number': 10, 'lower character' : 0}

    :param alphanumerical_characters_list: This is a matrice whose lines represent a list of character type
    and columns represent a character of a particular type of character.
    Ex: alphanumerical_characters_list = [['a','b','c'],['1','2','5','2'],[':', '~', '!']]
    """
    password_length = sum(password_characters_occurences_dict.values())
    found_excessive_occurences = False
    character_found_list = list()
    character_occurence_percentage = list()
    password_characters_type_percentage = 0
    
    # Test the password length
    printc("\n[cyan3 bold underline][*] Checking password length and characters occurences[/cyan3 bold underline]")
    if password_length < 12:
        printc(f"[red3 b][-][/red3 b] Short password length: [red3 b]{password_length}[/red3 b]")
        printc("[yellow1 b][!][/yellow1 b] Please, consider changing your password [red3 b]ASAP[/red3 b]!!")
    elif password_length < 14:
        printc(f"[orange_red1 b][±][/orange_red1 b] Password length: [orange_red1 b]{password_length}[/orange_red1 b] characters")
    else:
        printc(f"[green b][+][/green b] Password lenght acceptable: {password_length}")
    
    # Test the frequence of each group of characters(alphabetical, numerical characters, symbols)
    for password_characters_type, password_characters_occurences in password_characters_occurences_dict.items():
        if password_characters_occurences < password_length // 4:
            printc(f"[red3 b][-][/red3 b] {check_character_occurences_in_password(password_characters_occurences, password_characters_type, password_length)}")
        else:
            printc(f"[green b][+][/green b] {password_characters_type.capitalize()}: {password_characters_occurences}/{password_length}")
            password_characters_type_percentage += 25
        character_occurence_percentage.append(f"{password_characters_occurences/password_length*100:.2f}%")
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
        printc(f"[green b][+][/green b] Percentage of mixed character types in password: [green b]{password_characters_type_percentage}%[/green b]") 
    elif password_characters_type_percentage >= 50:
        printc(f"[orange_red1 b][±][/orange_red1 b] Percentage of mixed character types in password: [yellow b]{password_characters_type_percentage}%[/yellow b]") 
    else:
        printc(f"[red3 b][-][/red3 b] Percentage of mixed character types in password: [red3 b]{password_characters_type_percentage}%[/red3 b]") 
    printc("\n[cyan3 b u][+] Looking for excessive occurences[/cyan3 b u]")
    for charset_type in alphanumerical_characters_list:
        
        # Knowing that alphanumerical_characters_list is a matrice, charset_type will be a list
        if len(charset_type) >= 4 : #Use list's method
            for char in charset_type:
                if charset_type.count(char) > len(charset_type) // 2 and char not in character_found_list: 
                    character_occurences = charset_type.count(char)
                    found_excessive_occurences = True
                    if char.isspace():
                        printc(f"[red1 bold][-][/red1 bold] {character_occurences} occurences of space character\n")
                        character_found_list.append(char)
                    else:
                        printc(f"[red1 bold][-][/red1 bold] {character_occurences} occurences of {char} character\n")
                        character_found_list.append(char)
    if not found_excessive_occurences:
        printc("[green bold][+][/green bold] No excessive occurences of characters found!\n")
