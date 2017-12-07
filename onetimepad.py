import random
import string

from ciphers import Cipher


class OneTimePad(Cipher):
    """
    One time pad is a technique that requires the use of a one-time
    pre-shared key the same size as, or longer than the message being sent.
    In this technique, a plaintext is paired with a random secret key Then,
    each bit or character of the plaintext is encrypted by combining it with
    the corresponding bit or character from the pad using modular addition.
    """

    def encrypt(self, message):
        """Encrypt the message and return the encrypted message
        and its cypher key"""

        message = message.replace(" ", "")
        alphabet = string.ascii_uppercase
        text = ''
        key = ''
        inde = 0
        letters = []
        rand_list = []

        try:
            for letter in message.upper():
                rand = random.randint(0, 25)
                num = alphabet.index(letter)
                add = (num + rand) % 26
                letters.append(add)
                rand_list.append(rand)
            for num in letters:
                for keys in alphabet:
                    if alphabet.index(keys) == num:
                        text += keys
                    if alphabet.index(keys) == rand_list[inde]:
                        key += keys
                inde += 1
        except ValueError:
            return 'The text should has only alphabet characters'

        return "The pad result is: {}\nand its key is: {}".format(text, key)

    def decrypt(self, text, key):
        """Decrypts a message back to the original text  with the use of the
        cypher key generated."""

        alphabet = string.ascii_uppercase
        unencrypt = ''
        try:
            index = 0
            for letter in text.upper():
                enum = alphabet.index(letter)
                cnum = alphabet.index(key[index].upper())
                num = (enum-cnum) % 26
                # Convert number to decrypted letter and append
                for letter in alphabet:
                    if alphabet.index(letter) == num:
                        unencrypt += letter
                index += 1
        except (IndexError, ValueError):
            return 'Either text or key are wrong'

        return unencrypt
