""" Number guessing game """
import random
from os import system, name

# Rules:
#  1. The range selectable as a difficulty:
#     easy = 1-25, medium = 1-50, hard = 1-100
#  2. Player gets 5 guesses to determine the number
#  3. At each chance, the guesses are displayed and the user is told if
#     the guess is high or low
#  4. Player is given the opportunity to play again at the end of the game.
#  5. Player can exit the game at any time by typing "exit"
#  6. When the user exits, the game tells them how many times
#     they played and the number of wins and losses

# global game variables

user_games_count = 0
user_wins = 0
user_losses = 0
user_name = ''
user_playing = True
user_guesses = []
user_difficulty = 1
game_difficulties = {'easy': 1, 'medium': 2, 'hard': 3}
game_number = 0
user_won = False


def clear():
    """clear the screen to keep the game presentation nice"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def setup_game():
    """ Initialize the variables at the start of a new game """
    global user_playing, user_guesses, user_difficulty
    global user_name, game_number, user_won, user_games_count

    clear()
    if user_games_count == 0:
        user_name = input("Hello! What is your name? ")
        print(f'Welcome, {user_name}! This is your first game.')
    else:
        out_message = f'Hey {user_name}, you have played {user_games_count} '
        out_message += pluraled('game', 'games', user_games_count) + '.'
        print(out_message)
    user_games_count += 1
    user_playing = True
    user_guesses = []
    user_difficulty = 1
    game_number = 0
    user_won = False


def set_difficulty(level):
    """Sets the difficulty level of the game"""
    global game_number
    game_dif_msg = f"You selected Difficulty #{level} "
    if level == 1:
        game_number = random.randint(1, 25)
        game_dif_msg += "so I will select a number between 1 and 25."
    elif level == 2:
        game_number = random.randint(1, 50)
        game_dif_msg += "so I will select a number between 1 and 50."
    else:
        game_number = random.randint(1, 100)
        game_dif_msg += "so I will select a number between 1 and 100."
    game_dif_msg += "\nYou get only 5 guesses!"
    return game_dif_msg


def pluraled(singular_text, plural_text, numeric_value):
    """ display the right pluraled word """
    if numeric_value == 1:
        return singular_text
    else:
        return plural_text


setup_game()

while user_playing:
    input_msg = '1:Easy 2:Medium 3:Hard | Select a difficulty level: '
    input_difficulty = int(input(input_msg))
    print(set_difficulty(input_difficulty))
    print('OK, I have a number!')
    while len(user_guesses) < 5:
        message = ''
        user_guesses.append(int(input('Make a guess: ')))
        for user_guess in user_guesses:
            message += "Guess #" + str(user_guesses.index(user_guess)+1)
            message += " was " + str(user_guess) + "\n"
        if user_guesses[-1] > game_number:
            message += 'Your last guess was too high!'
        elif user_guesses[-1] < game_number:
            message += 'Your last guess was too low!'
        elif user_guesses[-1] == game_number:
            message += 'YOU GUESSED THE NUMBER!'
            user_wins += 1
            user_won = True
        clear()
        print(message)
        if user_won:
            break
    if user_won is False:
        user_losses += 1
        print("Oh no! You didn't guess the number. Game over!")
    play_again = input("Y/N: Would you like to play again?")
    if play_again.lower() == 'n':
        user_playing = False
    else:
        setup_game()
clear()
end_message = f"Thank you for playing {user_name}. "
end_message += f"You played {user_games_count} "
end_message += pluraled('game', 'games', user_games_count)
end_message += f" with {user_wins} " + pluraled('win', 'wins', user_wins)
end_message += f" and {user_losses} "
end_message += pluraled('loss', 'losses', user_losses) + "."
print(end_message)
