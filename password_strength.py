import re
from blacklist import blacklist

personal_information = ["phone", 'address', 'email']


def get_password_strength(password):
    if password in blacklist:
        return 1
    if len(password) < 8:
        return 2
    if password.isdigit():
        return 3
    if password.isalpha():
        return 4
    if password.isupper():
        return 5
    if password.islower():
        return 6
    if password in personal_information:
        return 7
    if password.isalnum():
        return 8
    if len(password) < 15:
        return 9
    return 10

if __name__ == '__main__':
    while True:
        user_password = input("Input you password :  ")
        if user_password:
            print("strength:", get_password_strength(user_password))
        else:
            break
