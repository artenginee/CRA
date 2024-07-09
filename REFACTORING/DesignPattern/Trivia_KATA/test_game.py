import io
import random
import sys
from unittest import TestCase

import IGame
from game_better import GameBetter
from game import Game


class TestGameBetter(TestCase):
    def play_game(self, game: IGame, seed):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            game.add("Chet")
            game.add("Pat")
            game.add("Sue")

            random.seed(seed)
            while True:
                game.rolling(random.randrange(6) + 1)

                if random.randrange(9) == 7:
                    not_a_winner = game.wrong_answer()
                else:
                    not_a_winner = game.was_correctly_answered()

                if not not_a_winner:
                    break
        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        return captured_output

    def test_characterized(self):
        seed = [1,100,1000,10000,100000]
        for s in seed:
            with self.subTest(f'{s} seed test'):
                self.assertEqual(self.play_game(Game(),s), self.play_game(GameBetter(),s))