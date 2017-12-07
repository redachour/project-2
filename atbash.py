import string

from ciphers import Cipher


class Atbash(Cipher):
    """The Atbash cipher is a particular type of monoalphabetic cipher formed
    by taking the alphabet and mapping it to its reverse, so that the first
    letter becomes the last letter, the second letter becomes the second to
    last letter, and so on."""

    def encrypt(self, text):
        """ Encrypting by reversing the letters"""
        
        alphabet = string.ascii_uppercase
        output = []
        for char in text.upper():
            try:
                index = alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(alphabet[25 - index])
        return ''.join(output)

    def decrypt(self, text):
        """Decrypting text is the same as encrypting"""

        return self.encrypt(text)
