""" Number guessing game """
import random

# Rules:
#  1. The range selectable as a difficulty: easy = 1-25, medium = 1-50, hard = 1-100
#  2. Player gets 5 guesses to determine the number
#  3. At each chance, the guesses are displayed and the user is told if
#     the guess is high or low
#  4. Player is given the opportunity to play again at the end of the game.
#  5. Player can exit the game at any time by typing "exit"
#  6. When the user exits, the game tells them how many times they played and the number of wins and losses

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
user_won = False;

def setup_game():
    """ Set all of the initial variables and values at the start of a new game """
    global user_playing, user_guesses, user_difficulty, game_number, user_won
    user_playing = True
    user_guesses = []
    user_difficulty = 1
    game_number = 0
    user_won = False

setup_game()

while user_playing:
    if user_games_count == 0:
        user_name = input("Hello! What is your name?")
        print(f'Welcome, {user_name}! This is your first game.')
    else:
        print(f'Hey {user_name}, you have played {user_games_count} games.')
    input_difficulty = int( input('1:Easy 2:Medium 3:Hard | Select a difficulty level:') )
    print(f'game difficult:{input_difficulty}')
    if input_difficulty == 1:
        game_number = random.randint(1, 25)
    elif input_difficulty == 2:
        game_number = random.randint(1, 50)
    else:
        game_number = random.randint(1, 100)
    print(f'OK, I have a number!{game_number}')
    while len(user_guesses) < 5:
        message = ''
        user_guesses.append(int(input('Make a guess:')))
        for user_guess in user_guesses:
            message += "Guess #" + str(user_guesses.index(user_guess)+1) + " was " + str(user_guess) + "\n"
        if user_guesses[-1] > game_number:
            message += 'Your last guess was too high!'
        elif user_guesses[-1] < game_number:
            message += 'Your last guess was too low!'
        elif user_guesses[-1] == game_number:
            message += 'YOU GUESSED THE NUMBER!'
            user_wins += 1
            user_won = True
        print(message)
        if user_won:
            break
    if user_won == False:
        user_losses += 1
        print("Oh no! You didn't guess the number. Game over!")
    play_again = input("Y/N: Would you like to play again?")
    if play_again.lower() == 'n':
        user_playing = False
    else:
        user_games_count += 1
        setup_game()
print(f"Thank you for playing {user_name}. You played {user_games_count} games with {user_wins} wins and {user_losses} losses.")
