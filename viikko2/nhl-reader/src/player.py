import requests

class Player:
    def __init__(self, json):
        self.name = json['name']
        self.nationality = json['nationality']
        self.assists = int(json['assists'])
        self.goals = int(json['goals'])
        self.team = json['team']
        self.games = int(json['games'])
        self.id = int(json['id'])

    def __str__(self):
        return f"{self.name:22}{self.team:16}{self.goals:2} + {self.assists:2} = {self.points}"

    @property
    def points(self):
        return self.goals + self.assists

# pylint: disable=too-few-public-methods
class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players = []
        response = requests.get(self.url, timeout=10).json()

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
# pylint: enable=too-few-public-methods

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        def sort_by_points(player):
            return player.points

        players = [p for p in self.reader.get_players() if p.nationality == nationality]
        return sorted(players, key=sort_by_points, reverse=True)

    def get_seasons(self):
        return [
            "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"
        ]

    def get_nationalities(self):
        return sorted(list({player.nationality for player in self.reader.get_players()}))
