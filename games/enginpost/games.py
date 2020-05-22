'''Object Oriented games'''


class GuessingGame:
    '''Object Oriented guessing game'''
    import random
    from os import system, name

    def __init__(self):
        '''initializer'''
        self.user_games_count = 0
        self.user_wins = 0
        self.user_losses = 0
        self.user_name = ''
        self.user_playing = True
        self.user_guesses = []
        self.user_difficulty = 1
        self.game_difficulties = {'easy': 1, 'medium': 2, 'hard': 3}
        self.game_number = 0
        self.user_won = False

    def clear(self):
        '''Clears the screen during play'''
        if self.name == 'nt':
            _ = self.system('cls')
        else:
            _ = self.system('clear')

    def pluraled(self, singular_text, plural_text, numeric_value):
        '''Display the right pluraled word'''
        if not isinstance(numeric_value, int):
            raise ValueError("The test value should be an int")
        if numeric_value == 1:
            return singular_text
        else:
            return plural_text

    def setup_game(self):
        '''Setup game after each round'''
        self.clear()
        if self.user_games_count == 0:
            self.user_name = input("Hello! What is your name? ")
            print(f'Welcome, {self.user_name}! This is your first game.')
        else:
            games = self.user_games_count
            out_message = f'Hey {self.user_name}, you have played '
            out_message += str(self.user_games_count) + ' '
            out_message += self.pluraled('game', 'games', games) + '.'
            print(out_message)
        self.user_games_count += 1
        self.user_playing = True
        self.user_guesses = []
        self.user_difficulty = 1
        self.game_number = 0
        self.user_won = False

    def set_difficulty(self, level):
        """Sets the difficulty level of the game"""
        game_dif_msg = f"You selected Difficulty #{level} "
        if level == 1:
            self.game_number = self.random.randint(1, 25)
            game_dif_msg += "so I will select a number between 1 and 25."
        elif level == 2:
            self.game_number = self.random.randint(1, 50)
            game_dif_msg += "so I will select a number between 1 and 50."
        else:
            self.game_number = self.random.randint(1, 100)
            game_dif_msg += "so I will select a number between 1 and 100."
        game_dif_msg += "\nYou get only 5 guesses!"
        return game_dif_msg

    def play_game(self):
        '''Play the game'''
        self.setup_game()
        while self.user_playing:
            input_msg = '1:Easy 2:Medium 3:Hard | Select a difficulty level: '
            input_difficulty = int(input(input_msg))
            print(self.set_difficulty(input_difficulty))
            print('OK, I have a number!')
            while len(self.user_guesses) < 5:
                message = ''
                self.user_guesses.append(int(input('Make a guess: ')))
                for user_guess in self.user_guesses:
                    guess_index = str(self.user_guesses.index(user_guess)+1)
                    message += "Guess #" + guess_index
                    message += " was " + str(user_guess) + "\n"
                if self.user_guesses[-1] > self.game_number:
                    message += 'Your last guess was too high!'
                elif self.user_guesses[-1] < self.game_number:
                    message += 'Your last guess was too low!'
                elif self.user_guesses[-1] == self.game_number:
                    message += 'YOU GUESSED THE NUMBER!'
                    self.user_wins += 1
                    self.user_won = True
                self.clear()
                print(message)
                if self.user_won:
                    break
            if self.user_won is False:
                self.user_losses += 1
                print("Oh no! You didn't guess the number. Game over!")
            play_again = input("Y/N: Would you like to play again? ")
            if play_again.lower() == 'n':
                self.user_playing = False
            else:
                self.setup_game()
        self.clear()
        end_message = f"Thank you for playing {self.user_name}. "
        end_message += f"You played {self.user_games_count} "
        end_message += self.pluraled('game', 'games', self.user_games_count)
        end_message += f" with {self.user_wins} "
        end_message += self.pluraled('win', 'wins', self.user_wins)
        end_message += f" and {self.user_losses} "
        end_message += self.pluraled('loss', 'losses', self.user_losses) + "."
        print(end_message)


class SpaceShooter:
    '''PyGame space shooter experiment'''
    import pygame

    def __init__(self):
        '''Initialization of SpaceShooter'''
        self.reset_game()

    def reset_game(self):
        self.remaining_lives = 3
        self.rocket_fuel = 0
        self.nuclear_fuel = 0

    def lives(self):
        '''doc'''
        return self.remaining_lives

    def fuel(self, fuel_container):
        '''Fueling the SpaceShooter'''
        if fuel_container:
            if fuel_container['type'] == 'rocket':
                if fuel_container.get('level') is not None:
                    self.rocket_fuel += fuel_container['level']
                return self.rocket_fuel
            elif fuel_container['type'] == 'nuclear':
                if fuel_container.get('level') is not None:
                    self.nuclear_fuel += fuel_container['level']
                return self.nuclear_fuel
