<img width="926" alt="image" src="https://user-images.githubusercontent.com/64969369/210290907-e00a0768-75f2-4062-b3c4-5735bac46c95.png">

# PasswordChecker
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/) 
![Version 1.0](http://img.shields.io/badge/version-v1.0-orange.svg) ![License](https://img.shields.io/badge/license-GPLv3-red.svg) <img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f"> 
 
 ## Purpose
PasswordChecker is a Python program that analyzes how strong a user's password is by performing several checks.
These checks include:
- Checking if the user's password has been exposed in HaveIBeenPwned's data breaches
- Verifying that the password meets a certain length requirement
- Calculating the percentage of characters in the password that belong to different character types (such as lowercase/uppercase letters, numbers, and symbols)
- Highlighting any characters that occur too frequently in the password
- Calculating the password's entropy, which is a measure of how difficult the password would be for an attacker to guess
- Generating a new, strong password for the user to use if desired."

## Preview
![image](https://github.com/0liverFlow/PasswordChecker/assets/64969369/075079dc-1402-4a72-b083-bb490f9f015c)
![image](https://github.com/0liverFlow/PasswordChecker/assets/64969369/a30a3a7d-4205-444a-9ea3-c41eefa80373)



## Installation & Usage
PasswordChecker is a cross platform script that works with python **3.x**.
```
git clone https://github.com/0liverFlow/PasswordChecker
cd ./PasswordChecker
pip3 install -r requirements.txt
```
Then you can run it
```
python3.x PasswordChecker.py
```
## Note
Some features of this script such as the entropy calculation and the minimum generated password length appreciation are based on <a href='https://www.ssi.gouv.fr/uploads/2021/10/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf'>ANSSI's password recommendations</a>.<br>
Feel free to take a look at it to learn more.
