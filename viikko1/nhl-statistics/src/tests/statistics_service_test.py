import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub() # type: ignore
        )

    def test_search(self):
        self.assertEqual(str(self.stats.search("Kurri")), str(Player("Kurri", "EDM", 37, 53)))
        self.assertEqual(self.stats.search("Selanne"), None)

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_top(self):
        self.assertEqual(len(self.stats.top(3)), 4)
        self.assertEqual(str(self.stats.top(3, SortBy.GOALS)[0]), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertEqual(str(self.stats.top(3, SortBy.ASSISTS)[0]), str(Player("Gretzky", "EDM", 35, 89)))