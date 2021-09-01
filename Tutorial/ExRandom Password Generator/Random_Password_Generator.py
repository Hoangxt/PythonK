'''
Project: Random Password Generator
Password: adbXYZ-69_96
'''
import string
import random

LETTERS = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation


def password_generator(length=8):
    printable = f'{LETTERS}{NUMBER}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)  # dang o dang list
    random_password = ''.join(random_password)
    return random_password


def get_passwordlength():
    password_length = input("How long do you want your password: ")
    return int(password_length)


def main():
    password_length = get_passwordlength()
    password = password_generator(password_length)
    print(password)


if __name__ == "__main__":
    main()
