"""
|───────────────────────────────────────────────────────────────────────────────────
|   This module is composed of 4 functions namely :                                |
|                                                                                  |
==> get_password_alphabetical_words() takes 1 parameter and returns a string       |
|   which contain the alphabetical words found in the user password.               |
|                                                                                  |
|-- password parameter represents the user password                                |
|__________________________________________________________________________________|
|                                                                                  |
|==> get_password_numbers(password) takes 1 parameter(password) as                 |
|    the previous function and returns a list of numbers converted into int        |
|    because as you might know the password is a string.                           |
|                                                                                  |
|-- password parameter represents the user password                                |
|__________________________________________________________________________________|
|                                                                                  |
|==> check_birthday_format(user_given_birthday) takes 1 parameter and returns      |
|    the user birthday converted into int instead of keeping the string value.     |
|--  user_given_birthday represents the birthday entered by the user.              |
|    It must be on the following format('DD/MM/YYYY')                              |
|    It checks if the birthday format is correct.                                  |
|    If it is not correct, it will exit the program and                            |
|    display the reason on the screen.                                             |
|__________________________________________________________________________________| 
|                                                                                  |
==> check_name_surname_birthday_city_in_password() takes 6 parameters namely :     |
|                                                                                  |
|-- user_password which represents the user password(string)                       |
|-- user_first_name which represents the user's first name(string)                 |
|-- user_last_names which represents a list of user last names(list)               |
|-- user_birthday which represents the user birthday(string)                       |
|-- user_country which represents the user country(string)                         |
|-- user_city which represents the user city(string)                               |
|   All in all, this function is gonna check if the user password contains         |
|   any of the last 5 parameters listed above.                                     |
|__________________________________________________________________________________|   
"""
import re
import sys
def get_password_words(password):
    alphabetical_words_pattern = '[a-zéï]+'
    return ''.join(re.findall(alphabetical_words_pattern, password, flags=re.IGNORECASE)) #string

def get_password_numbers(password):
    number_pattern = '[0-9]{1,}'
    password_numbers = re.findall(number_pattern, password) #list of strings : each string is a number
    try:
        convert_password_numbers_into_int = [int(number) for number in password_numbers]
    except (TypeError, IndexError):
            print("Oops! ", sys.exc_info[0], " occured :(")
    return convert_password_numbers_into_int

def check_birthday_format(user_given_birthday):
    user_birthday = re.split('[-/]', user_given_birthday)
    if len(user_birthday) != 3:
        print("Oops, it seems that your birthday format is incorrect :(")
        sys.exit("Please, make sure that you used the right format(DD/MM/YYYY or DD-MM-YYYY)")
    try: #birthday_values represent the birth[day, month and year]
        convert_birthday_values_into_int = [int(x) for x in user_birthday ]
    except TypeError:
        print("Oops, it seems that your birthday format is incorrect :(")
        sys.exit("Please, make sure that you only used numbers as specified in the format(DD/MM/YYYY)")
    return convert_birthday_values_into_int

def check_name_surname_birthday_city_in_password(user_password, user_first_name, user_last_names, user_birthday, user_country, user_city):
    found_first_name = found_surname = found_birthday = found_country = found_city = False
    found_month = found_year = False
    password_words = get_password_words(user_password).lower()
    user_last_names  = user_last_names.split()
    user_lower_last_names = [last_name.lower() for last_name in user_last_names]
    number_iterations = 3 #user_first_name, user_country,  #
    password_numbers = get_password_numbers(user_password)
    user_birthday = check_birthday_format(user_birthday) #Check if the user entered a right format of birthday
    birth_day = user_birthday[0]
    birth_month = user_birthday[1]
    birth_year = user_birthday[-1]
    months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
                      'août', 'septembre', 'octobre', 'novembre', 'décembre', 'january',
                      'jan', 'february', 'fev', 'march', 'april', 'may', 'june', 'july',
                      'august', 'september', 'sept','october', 'oct', 'november', 'nov',
                      'december', 'dec', 'j4nv1er', 'f3vr13r', 'm4rs', '4pr1l', 'm41'
             ]
    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 22, 21,
                  20, 19, 18, 17, 16, 15, 14, 13, 12
            ]
    #Test if the user password contains any part of their birthday
    if len(password_numbers):
        if birth_day in password_numbers:
            found_birthday = True
            password_numbers.remove(birth_day)
            print("\nHmmm X_X, you must not use AT ALL your day of birth ({}) in your password".format(birth_day))
            print("You must change your password ASAP because it can be guessed intuitively")
            print("It highly advisable to use a password generator and a password manager for your password in order to avoid such situation")
        if birth_month in password_numbers:
            found_birthday = True
            password_numbers.remove(birth_month)
            print("\nHmmm X_X, you must not use AT ALL your birth month ({}) in your password".format(birth_month))
            print("You must change your password ASAP because it can be guessed intuitively")
            print("It highly advisable to use a password generator and a password manager for your password in order to avoid such situation")
        if birth_year in password_numbers or int(str(birth_year)[-2:]) in password_numbers :
            found_birthday = True
            try:
                password_numbers.remove(birth_year)
            except ValueError:
                password_numbers.remove(int(str(birth_year)[-2:]))
                print(f'\nHmmm X_X, you must not use your birth year({int(str(birth_year)[-2:])}) in your password')
            else:
                print(f'\nHmmm X_X, you must not use your birth year({birth_year}) in your password')
            print("You must change your password ASAP because it can be guessed intuitively")
            print("It highly advisable to use a password generator and a password manager in order to avoid such situation")
        #check if the user password contains their birthday's numbers other than birth_day, birth_month and birth_year
        if len(password_numbers):
            user_birthday_str = [str(value) for value in user_birthday]
            user_birthday_str = ''.join(user_birthday_str)
            for birthday_value in password_numbers:
                if str(birthday_value) in user_birthday_str:
                    found_birthday = True
                    user_birthday_str = re.sub(birthday_value, '', user_birthday_str, 1, flags=re.IGNORECASE)
                    print(f"\nHmmm X_X, you must not use AT ALL your birthday's numbers ({birthday_value}) in your password")
                    print("You must change your password ASAP because it can be guessed intuitively")
                    print("It highly advisable to use a password generator and a password manager in order to avoid such situation")
        #Check if the user password contains a year
        if len(password_numbers):
            for year in password_numbers:
                if year in  years:
                    found_year = True
                    password_numbers.remove(year)
                    print("\nHmmm X_X, you must not use AT ALL a year ({}) in your password".format(year))
                    print("You must change your password ASAP because it can be guessed intuitively")
                    print("It highly advisable to use a password generator and a password manager in order to avoid such situation")
    #Check if the password contains any part of the user name or surname
    if len(password_words):
        while number_iterations > 0:
            if user_first_name.lower() in password_words:
                found_first_name = True
                password_words = re.sub(user_first_name, '', password_words, 1, flags=re.IGNORECASE)
                print(f'\nHmmm X_X, you must not use AT ALL your first name in your name ({user_first_name}) password')
                print("You must change your password ASAP because it can be guessed intuitively")
                print("Don't forget that password generator and a password manager are your best friends :)")
            elif user_country.lower() in password_words:
                found_country = True
                password_words = re.sub(user_country, '', password_words, 1, flags=re.IGNORECASE)
                print(f'\nHmmm X_X, you must not use AT ALL your country ({user_country}) in your password')
                print("You must change your password ASAP because it can be guessed intuitively")
                print("Don't forget that password generator and a password manager are your best friends :)")
            elif user_city.lower() in password_words:
                found_city = True
                password_words = re.sub(user_city, '', password_words, 1, flags=re.IGNORECASE)
                print(f'\nHmmm X_X, you must not use AT ALL your city ({user_city}) in your password')
                print("You must change your password ASAP because it can be guessed intuitively")
                print("Don't forget that password generator and a password manager are your best friends :)")
            number_iterations -= 1
        for last_name in user_lower_last_names:
            if last_name in password_words:
                found_surname = True
                password_words = re.sub(last_name, '', password_words, 1, flags=re.IGNORECASE)
        #Check the user password a month
        if len(password_words):
            for month in months:
                if month in password_words:
                    found_month = True
                    password_words = re.sub(month, '', password_words, 1, flags=re.IGNORECASE)
                    print("\nHmm X_X, you must not use AT ALL a month or a month abbreviation ({}) in your password".format(month))
                    print("You must change your password ASAP")
                    print("It advisable to use a password generator and a password manager for your password")
    if found_first_name or found_surname or found_birthday or found_month or found_year or found_country or found_city:
        print("\nYour password is unsecure because it's can easily be guested by malveillant people")
        print("Thanks to change it ASAP ;-)")
        print("I will keep an eye on you amigo until you change it :)")
        print("──────────────────────────────────────────────────────────────────────────────────────────\n")


