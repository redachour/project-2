import string

from ciphers import Cipher


class Caesar(Cipher):
    """Caesar cipher is one of the simplest and most widely known
    encryption techniques. It is a type of substitution cipher in
    which each letter in the plaintext is replaced by a letter
    some fixed number of positions down the alphabet."""

    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
