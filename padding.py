import random
import string


class Padding:
    """ Add padding to blocks less than 5 characters to make it five.
    And Those larger than 5 are split up into 5 letter chunks,
    and add remaining characters to create a 5 letter block."""

    def __init__(self):
        self.output = ''

    # set up a helper to add padding to the blocks less than 5 characters
    def _helper(self, word):
        block = list(word)
        # pick a random alphabet
        random_char = random.choices(string.ascii_uppercase, k=(5-len(block)))
        # insert those random alphabet to a random position in the block
        for item in random_char:
                block.insert(random.randint(0, 5), item)
        # append the block to the output
        self.output += ''.join(block) + ' '

    # add padding method to figure out which block needs padding
    def add_padding(self, text):
        """Create an output of 5 character blocks"""

        for word in text.split(' '):
            # 5 character blocks added straight
            if len(word) == 5:
                self.output += word + ' '
            # calling the helper method to fill the blocks
            elif len(word) < 5:
                self._helper(word)
            # split the block up into 5 letter chunks
            elif len(word) > 5:
                block = ''
                for letter in word:
                    block += letter
                    if len(block) == 5:
                        # append the chunk to output
                        self.output += block + ' '
                        block = ''
                self._helper(block)

        return self.output.upper()
