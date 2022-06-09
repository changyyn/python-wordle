from color import Color
from wordle import Wordle


"""
Class for the actual game that will use the wordle class to play the game
"""
class Game():

    def __init__(self, word, max_guesses=6):
        self.wordle : Wordle = Wordle(word)
        self.max_guesses = max_guesses
        self.results = []
        self.guesses = []
        self.is_win = False

    def guess(self, guess_word):
        
        self.guesses.append(guess_word)
        result = self.wordle.get_result_from_guess(guess_word)

        if Color.BLACK not in result and Color.YELLOW not in result:
            self.is_win = True

        self.results.append(result)
        
    def get_results_str(self):

        result_str = ''
        for result in self.results:
            result_str += ''.join(r.value for r in result) + "\n"

        return result_str

    def get_all_guesses(self):

        return self.guesses.copy()

    def get_num_guesses_left(self):
        return self.max_gusses - len(self.results)

    def has_lost(self):
        return not self.is_win and len(self.results) >= self.max_guesses

    def has_won(self):
        return self.is_win
