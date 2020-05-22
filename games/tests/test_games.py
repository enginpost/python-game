import unittest

from games.enginpost.games import GuessingGame, SpaceShooter


class TestGuessingGame(unittest.TestCase):
    '''Testing the methods of the GuessingGame class'''

    def test_pluraled_singular(self):
        game = GuessingGame()
        result = game.pluraled('game', 'games', 1)
        self.assertEqual(result, 'game')

    def test_pluraled_plural(self):
        game = GuessingGame()
        result = game.pluraled('game', 'games', 2)
        self.assertEqual(result, 'games')

    def test_pluraled_nan(self):
        try:
            game = GuessingGame()
            game.pluraled('game', 'games', 'a')
        except ValueError:
            pass
        else:
            self.assertFalse(True, "ValueError Exception not raise")


class TestSpaceShooter(unittest.TestCase):
    '''Testing the methods of SpaceShooter'''

    def setUp(self):
        '''Setup SpaceShooter instance'''
        self.ssGame = SpaceShooter()

    def test_lives(self):
        '''Get remaining lives'''
        result = self.ssGame.lives()
        self.assertEqual(result, 3)

    def test_rocket_fuel_get(self):
        '''Get rocket fuel'''
        self.ssGame.reset_game()
        some_fuel = {'type': 'rocket'}
        result = self.ssGame.fuel(some_fuel)
        self.assertEqual(result, 0)

    def test_rocket_fuel_add(self):
        '''Set and get rocket fuel'''
        self.ssGame.reset_game()
        some_fuel = {'level': 5, 'type': 'rocket'}
        result = self.ssGame.fuel(some_fuel)
        self.assertEqual(result, 5)

    def test_nuclear_fuel_get(self):
        '''Get fuel'''
        self.ssGame.reset_game()
        some_fuel = {'type': 'nuclear'}
        result = self.ssGame.fuel(some_fuel)
        print(result)
        self.assertEqual(result, 0)

    def test_nuclear_fuel_add(self):
        '''Set and get nuclear fuel'''
        self.ssGame.reset_game()
        some_fuel = {'level': 5, 'type': 'nuclear'}
        result = self.ssGame.fuel(some_fuel)
        self.assertEqual(result, 5)
