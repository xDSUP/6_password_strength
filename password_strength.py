from blacklist import blacklist

personal_information = ["phone", 'address', 'email']


def check_password_len(password):
    if len(password) > 12:
        return 2
    elif len(password) > 6:
        return 1
    else:
        return 0


def find_in_blacklist(password):
    if password in blacklist:
        return 0
    else:
        return 1


def check_password_numbers(password):
    if not password.isdigit():
        numbers = 0
        for char in password:
            if char.isdigit():
                numbers += 1
        if numbers >= 4:
            return 2
        else:
            return 1
    else:
        return 0


def check_password_register(password):
    if not password.isupper() and not password.islower():
        return 2
    else:
        return 0


def check_password_special_characters(password):
    if not password.isalnum():
        return 1
    else:
        return 0


def check_password_letters(password):
    if not password.isalpha():
        return 1
    else:
        return 0


def check_password_personal_info(password):
    if password in personal_information:
        return 0
    else:
        return 1


def get_password_strength(password):
    strength = 0
    strength += check_password_len(password)
    strength += find_in_blacklist(password)
    strength += check_password_letters(password)
    strength += check_password_numbers(password)
    strength += check_password_personal_info(password)
    strength += check_password_register(password)
    strength += check_password_special_characters(password)
    return strength

if __name__ == '__main__':
    user_password = input("Input you password :  ")
    if user_password:
        print("strength:", get_password_strength(user_password))
    else:
        print("you have not entered a password")
