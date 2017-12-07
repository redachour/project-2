from ciphers import Cipher


class Transposition(Cipher):
    """A transposition cipher is a method of encryption by which the positions
    held by units of plaintext are shifted according to a regular system."""

    def encrypt(self, text):
        """Remove spaces and join with different postion as required
        and split it up into 5 character chunks """

        # removing spaces from the message
        text = text.replace(" ", "")
        # creating the cryption
        crypt = ''.join(text[0::4]+text[1::2]+text[2::4])
        # spliting the cryption into 5 character chunks
        return ' '.join(crypt[i:i+5] for i in range(0, len(crypt), 5))

    def decrypt(self, text):
        """ creating a list of '-', to replace those characters with
        the right ones to get the original message"""
        
        # removing spaces
        text = text.replace(" ", "")
        # create a list of '-' replacing each character of the text
        crypt = ['-' for _ in text]
        # replacing the first line
        index = 0
        for item in text[0:len(text[0::4]):]:
            crypt[index] = item
            index += 4
        # replacing second line
        index = 1
        for item in text[len(text[0::4]):len(text[0::4] + text[1::2])]:
            crypt[index] = item
            index += 2
        # replacing third line
        index = 2
        for item in text[len(text[0::4] + text[1::2]):]:
            crypt[index] = item
            index += 4

        return ''.join(crypt)
