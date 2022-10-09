"""
|───────────────────────────────────────────────────────────────────────────────────|
|   This module contains 1 function which takes 4 parameters and return nothing.    |
|                                                                                   |
==> check_name_surname_country_city_format checks if the format of the 4 arguments  |   
|   it is gonna to receive is correct.                                              |
|   If one of them's format is incorrect, it will exit the program and display an   |
|   error message on the screen.                                                    |
|-- first_name represents the user first_name(string)                               |
|-- last_names represents a list of user last names(list)                           |
|-- country represents the country entered by the user(string)                      |                           
|-- city represents the city entered by the user(string)                            |
|___________________________________________________________________________________|
"""
import sys
import re
def check_name_surname_country_city_format(first_name, last_names, country, city):
    name_surname_pattern = '^[a-zéïôùûè]+$'
    if len(first_name) == 0:
        print("Whoops ! It seems that you didn't specify your first_name :(")
        sys.exit("Thank you to enter it. It is necessary for checking your password quality!!")
    elif len(first_name.split()) > 1:
        print("Whoops ! It seems that you entered more than one word for your first name")
        sys.exit("Thank you to correct that before going on!!")
    elif len(last_names) == 0:
        print("Whoops ! It seems that you didn't specify your last_name :(")
        sys.exit("Thank you to enter it. It is necessary for checking your password quality!!")
    elif len(country) == 0:
        print("Whoops ! It seems that you didn't specify your country :(")
        sys.exit("Thank you to enter it. It is necessary for checking your password quality!!")
    elif len(city) == 0:
        print("Whoops ! It seems that you didn't specify your city :(")
        sys.exit("Thank you to enter it. It is necessary for checking your password quality!!")
    elif re.search(name_surname_pattern, first_name, flags=re.IGNORECASE) == None:
        print("Whoops! It seems that you entered characters other that only alphabetical characters when entering your first_name")
        sys.exit("Please, make sure to correct that, and try again !!")
    elif re.search(name_surname_pattern, country, flags=re.IGNORECASE) == None:
        print("Whoops! It seems that you entered characters other that only alphabetical characters when entering your country")
        sys.exit("Please, make sure to correct that, and try again !!")
    elif re.search(name_surname_pattern, city, flags=re.IGNORECASE) == None:
        print("Whoops! It seems that you entered characters other that only alphabetical characters when entering your city")
        sys.exit("Please, make sure to correct that, and try again !!")
    for last_name in last_names:
        if re.search(name_surname_pattern, last_name, flags=re.IGNORECASE) == None:
            print("Whoops! It seems that you entered characters other that only alphabetical characters when entering your last_name")
            sys.exit("Please, make sure to correct that, and try again !!")