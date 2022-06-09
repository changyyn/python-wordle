from game import Game

def main():

    game = Game('trout')

    while not game.has_won() and not game.has_lost():

        guess = input("Guess a five letter word: ")
        
        game.guess(guess)

        print(game.get_results_str())

    if game.has_won():
        print("Conglaturation you have won!")
    else:
        print("Nice try :)")



if __name__ == '__main__':
    main()