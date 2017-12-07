import os
import sys

from caesar import Caesar
from atbash import Atbash
from polybius import Polybius
from transposition import Transposition
from onetimepad import OneTimePad
from padding import Padding


def clear():
    """this function is to clear the screen for better view"""

    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    """Enable the user to select a cipher and either encrypt or
    decrypt a message or add a padding."""

    clear()
    ciphers = {'1': Caesar, '2': Atbash, '3': Polybius, '4': Transposition}

    # printing the menu containing ciphers and quit command
    print("""This is the Secret Messages project for Treehouse Techdegree.\n
    There are the current available ciphers:\n
            1 - Caesar
            2 - Atbash
            3 - Polybius
            4 - Transposition\n
    Press 'q' to quit\n""")

    # Select cipher type.
    choice = None
    while choice is None:
        choice = input("Select 1, 2, 3, or 4 to start >> ").lower()
        if choice not in ['1', '2', '3', '4']:
            if choice == 'q':
                print("Good Bye.")
                sys.exit()
            else:
                print("Invalid selection, Try again.")
                choice = None

    # Ask user for the message
    text = input("That's an excellente cipher. what's the message? >> ")

    # Select Encryption or decryption.
    crypt = None
    while crypt is None:
        crypt = input("Are we going to encrypt or decrypt? >> ").lower()
        if crypt not in ['encrypt', 'decrypt']:
            if crypt == 'q':
                print("Good Bye.")
                sys.exit()
            else:
                print("Invalid selection, try again or quit.")
                crypt = None

    # ask user for one time pad
    otp = input("would you like a one time pad [Y/n] >> ").lower()
    if otp == 'y':
        if crypt == 'encrypt':
            print("Your result: {}".format(OneTimePad().encrypt(text)))
        else:
            key = input("provide key same length as message or bigger >> ")
            print("Your result: {}".format(OneTimePad().decrypt(text, key)))
    else:
        method = ciphers[choice]()
        add = Padding().add_padding(method.encrypt(text))
        if crypt == 'encrypt':
            padding = input("would you like padding [Y/n] >> ").lower()
            if padding == 'y':
                print("Your result: {}".format(add))
            else:
                print("Your result: {}".format(method.encrypt(text)))
        else:
            print("Your result: {}".format(method.decrypt(text)))

    # Ask user to restart or quit.
    restart = input("Encrypt/decrypt another message? [Y/n] >> ").lower()
    if restart == 'y':
        run()
    else:
        print("Good Bye.")
        sys.exit()


if __name__ == "__main__":
    run()
