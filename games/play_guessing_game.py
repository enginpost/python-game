'''Play the guessing game'''
from enginpost.games import GuessingGame

my_game = GuessingGame()
# my_game.play_game()
result = my_game.pluraled('s', 'p', 'a')
print(result)
