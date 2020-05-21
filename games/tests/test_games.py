import unittest
from games.enginpost.games import GuessingGame


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
