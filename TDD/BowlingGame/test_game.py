from unittest import TestCase, skip

from game import Game


# 10개의 frame
class TestGame(TestCase):
    def test_모두0점(self):
        game = Game()

        for i in range(20):
            game.roll(0)

        self.assertEqual(0, game.score())

    def test_모두1점(self):
        game = Game()

        for i in range(20):
            game.roll(1)

        self.assertEqual(20, game.score())

    def test_normal(self):
        game = Game()

        game.roll(1)
        game.roll(2)

        for i in range(18):
            game.roll(0)

        self.assertEqual(3, game.score())

    # @skip
    def test_스페어(self):
        game = Game()
        game.roll(3)
        game.roll(7)  # spare
        game.roll(5)

        for i in range(17):
            game.roll(0)

        self.assertEqual(20, game.score())



    @skip
    def test_스트라이크(self):
        game = Game()
        game.roll(10)  # 스트라이크
        game.roll(3)
        game.roll(4)
        for i in range(8 * 2):
            game.roll(0)
        self.assertEqual(17 + 7, game.score())

    @skip
    def test_퍼펙트게임(self):
        game = Game()
        for i in range(12):
            game.roll(10)

        self.assertEqual(300, game.score())

    @skip
    def test_샘플게임(self):
        game = Game()
        game.roll(1)
        game.roll(4)
        game.roll(4)
        game.roll(5)
        game.roll(6)
        game.roll(4)
        game.roll(5)
        game.roll(5)
        game.roll(10)
        game.roll(0)
        game.roll(1)
        game.roll(7)
        game.roll(3)
        game.roll(6)
        game.roll(4)
        game.roll(10)
        game.roll(2)
        game.roll(8)
        game.roll(6)

        self.assertEqual(133, game.score())