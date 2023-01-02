import sys
import time
import re
from rich.console import Console

"""
|───────────────────────────────────────────────────────────────────────────────────|
|This module is composed of 3 functions namely :                                    |
|                                                                                   |
==> test_password(user_password, dictionary_file_path)                              |
|   This function takes 2 parameters and returns nothing :                          |
|-- user password is the password of the user                                       |
|-- dictionary_file_path is the dictionary file  which                              |
|   contains a list of leaked passwords or well-known passwords.                    |
|                                                                                   |
|-- In a nutshell, test_password will check if the user password is part or not     |
|   of the dictionary file entered as an argument.                                  |
|___________________________________________________________________________________|
|                                                                                   |
==> determine_elapsed_time(start_time, end_time)                                    |
|   This function takes 2 parameters ans return the time (hours, minutes, seconds)  |
|-- start_time represents the time when we start the dictionary attack against the  |
|   user password.                                                                  |
|-- end_time represents the time when the user password has been found, which means |
|   that the dictionary attack was successfull.                                     |
|___________________________________________________________________________________|
|                                                                                   |
==> format_time(hours, minutes, seconds)                                            |
|   This function takes 3 parameters and return a string which represents the       |
|   time format.                                                                    |
|   This function is necessary in order to format the time properly.                |
|   If we choose to get rid of it, it certain that we're gonna get an elapsed_time  |
|   in the following format(0h:0min:5s) instead of (5s)                             |
|___________________________________________________________________________________|
"""

def determine_elapsed_time(start_time, end_time):
    elapsed_time = end_time - start_time
    hours = minutes = 0
    seconds = elapsed_time
    if elapsed_time >= 3600 :
        hours = elapsed_time // 3600
        elapsed_time = elapsed_time % 3600 #elapsed_time - (hours * 3600)
    if elapsed_time >= 60 :
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
    return hours, minutes, seconds

def format_time(hours, minutes, seconds):
    #Set hour.s format
    time_format=str() if not hours else str(hours) + 'h:'
    #Set minute format 
    time_format += str(minutes) + 'min:' if minutes else ''        
    return time_format + str(seconds) + 's'

def crack_password(user_password, passwords_dictionary_file_path='/Users/cyberwarr10r/Documents/Programming/PasswordChecker/rockyou.txt'):
    console =  Console()
    printc = console.print
    password_found = False
    start_time = time.perf_counter()
    try:
        passwords_dictionary = open(re.sub(r'\\', '/', passwords_dictionary_file_path), encoding="utf-8", errors="ignore")
        passwords = passwords_dictionary.readlines()
    except FileNotFoundError:
        print('No such file: ', passwords_dictionary_file_path)
        print('Make sure that the specified file path exists!')
        sys.exit(-1)
    except Exception as e:
        sys.exit(e)
    finally:
        passwords_dictionary.close()
    
    for password in passwords:
        if password.rstrip() == user_password:
            end_time = time.perf_counter()
            password_found = True
            hours, minutes, seconds = determine_elapsed_time(start_time, end_time)
            elapsed_time = format_time(hours, minutes, seconds)
            break
    if password_found :
        printc("\n[red3 b][-][/red3 b] Password found in the password list entered =_='")
        printc(f"Password cracked in {elapsed_time}")
        printc("[yellow b][!][yellow b]You must change it ASAP. Otherwise, your security is at risk !!!")
        print("───────────────────────────────────────────────────────────────────")
    else:
        printc("\n[green b][+][/green b] Hoorah \o/ : Your password has not been found in the password dictionary file")
        printc("[yellow b][!][/yellow b] However, don't overestimate your password strenght")
        printc("[deep_pink4 b u]Tip:[/deep_pink4 b u] You should test it using other dictionaries to make sure that it is enough safe")
