import string

from ciphers import Cipher


class Polybius(Cipher):
    """Polybius square is a device invented for fractionating
    plaintext characters so that they can be represented
    by a smaller set of symbols"""

    def _polybius_square(self):
        """Create a dictionary, where the key is the letter
        of the alphabet and the value is the (x,y) coordinates
        for that letter in the square."""

        alphabet = string.ascii_uppercase
        x = 1
        y = 1
        polybius = {}

        for letter in alphabet:
            polybius[letter] = [x, y]
            # I and J have the same coornidate
            if letter != "I":
                y += 1
            if y > 5:
                y = 1
                x += 1

        return polybius

    def encrypt(self, text):
        """ Retrieve the coordinates for that letter
        and append to the output """

        output = []
        for char in text.upper():
            # append alphabet characters to output
            if str.isalpha(char):
                pair = self._polybius_square()[char]
                for x in pair:
                    output.append(str(x))
            # append spaces to output
            elif char == " ":
                output.append(char)

        return ''.join(output)

    def decrypt(self, text):
        """Convert the encrypted string back to plain text I need
        to split the numbers into groups of 2."""

        output = []
        # Replace spaces by 2 characters
        text = text.replace(' ', "__")
        # Split the string into chunks of 2.
        pairs = [text[i: i+2] for i in range(0, len(text), 2)]
        # Looping through each pair to match polybius square pairs
        for pair in pairs:
            # Append spaces
            if pair == "__":
                output.append(" ")
            else:
                try:
                    # trying to create a matching list with integers
                    match = [int(x) for x in pair]
                except ValueError:
                    # if cannot convert, append the pair straight
                    output.append(pair)
                else:
                    for key, value in self._polybius_square().items():
                        # find a match in the polybius square
                        if value == match:
                            output.append(key)

        return ''.join(output)
