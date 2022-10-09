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
def check_character_occurences_in_password(password_characters_occurences, password_characters_type):
    if password_characters_occurences == 0:
        return "Your password does not contain any occurence of " + password_characters_type
    else:
        return "Your password contains only (" + str(password_characters_occurences) + ") "\
                +  password_characters_type

def check_password_characters_mixture(password_characters_occurences_dict, alphanumerical_characters_list):
    password_length = sum(password_characters_occurences_dict.values())
    found_excessive_occurences = 0
    char_occurence_found = []
    character_occurence_percentage = list()
    mixture_percentage = 0
    #Test if the password length is correct(Which means at least 12 characters)
    if password_length < 12:
        print(f"\nYour password length must have at least 12 characters(rather than {password_length} characters)")
        print("Don't forget this little tip ('v')")
        print("In most cases, more your password length is long, more it will require lots of time to crack it")
        print("Note : passwords like 123457890 or iloveyou123 or adminpassword will be instantly cracked")
        print("──────────────────────────────────────────────────────────────────────────────────────")
    else:
        print("\nGood :)\n────────")
        print("Your password length (", password_length, ") is acceptable. Keep setting password of such length")
    #Test the frequence of each group of characters(alphabetical, numerical characters, symbols)
    for password_characters_type, password_characters_occurences in password_characters_occurences_dict.items():
        if password_characters_occurences < password_length // 4:
            print("\nBad :(\n───────")
            print(password_characters_type," must represent at least 1/4 of your password length")
            print(check_character_occurences_in_password(password_characters_occurences, password_characters_type))
        else:
            print("\nGood :)\n────────")
            print("Your password contains : ", password_characters_occurences, " " + password_characters_type + "\n")
            mixture_percentage += 25
        character_occurence_percentage.append(str(password_characters_occurences / password_length * 100)[:4] + "%")
    mixture_percentage = str(mixture_percentage) + "%"
    print("\n─────────────────────────S U M M A R Y ─ T A B L E──────────────────────────────────────\n")
    print("+=======================================================================+")
    print("|       Character Type           | Char_Type_Percentage_In_Password     |")
    print("|================================|======================================|")
    print("|       Special characters       |           ",character_occurence_percentage[0],"                    |")
    print("|================================|======================================|")
    print("|       Numbers                  |           ",character_occurence_percentage[1],"                    |")
    print("|================================|======================================|")
    print("|       Lower characters         |           ",character_occurence_percentage[2],"                    |")
    print("|================================|======================================|")
    print("|       Upper characters         |           ",character_occurence_percentage[3],"                    |")
    print("|================================|======================================|")
    print("|Password's characters mixture percentage is :  ",mixture_percentage,"                   |")
    print("+================================|======================================+")
    print("\n──────────────────────────────────────────────────────────────────────────────────────")
    for charset_type in alphanumerical_characters_list:
        #Knowing that alphanumerical_characters_list is a matrice, charset_type will be a list
        if len(charset_type) >= 4 :
            first_char = charset_type[0]
            counter = 0
            while counter < len(charset_type) :
                character_occurence = 1
                if first_char not in char_occurence_found:
                    for next_char in charset_type[1:]:
                        if first_char == next_char:
                            character_occurence += 1
                    if character_occurence >= len(charset_type) / 2:
                        found_excessive_occurences += 1
                        print("\nHmmm (=_=)' : \n─────────────")
                        if first_char == ' ':
                            first_char = 'space'
                        print("Amigo we have noticed ", character_occurence , "occurences of ", first_char, "character in your password")
                        print("You should change that by using other characters of the same type.\n")
                        if first_char == 'space':
                            first_char = ' '
                        char_occurence_found.append(first_char)
                charset_type.append(first_char)
                del(charset_type[0])
                first_char = charset_type[0]
                counter += 1 
    if not found_excessive_occurences:
        print("\nGood :=)\n──────────")
        print("Your password did not contain any excessive occurence of characters that compose it!")
        print("──────────────────────────────────────────────────────────────────────────────────────\n")