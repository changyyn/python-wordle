from color import Color
from collections import Counter

class Wordle:

    def __init__(self, word):
        self.word = word.upper()
        self.word_size = len(word)

    def get_result_from_guess(self, guess):
        
        if len(guess) != self.word_size:
            return None

        guess = guess.upper()
        
        letter_count = Counter(self.word)
        result = [Color.BLACK] * len(self.word)

        # First pass through to get all the correctly positioned letters
        for i, (word_c, guess_c) in enumerate(zip(self.word, guess)):
            if word_c == guess_c:
                result[i] = Color.GREEN
                letter_count[word_c] -= 1
        # Get the leftovers
        for i, (color, guess_c) in enumerate(zip(result, guess)):
            if color == Color.BLACK and guess_c in letter_count and letter_count[guess_c] > 0:
                result[i] = color.YELLOW
                letter_count[guess_c] -= 1

        return result
