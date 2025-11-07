import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = int(dict['assists'])
        self.goals = int(dict['goals'])
        self.points = self.goals + self.assists
        self.team = dict['team']
        self.games = int(dict['games'])
        self.id = int(dict['id'])

    def __str__(self):
        return f"{self.name:22}{self.team:16}{self.goals:2} + {self.assists:2} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players = []
        response = requests.get(self.url).json()

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        def sort_by_points(player):
            return player.points

        return sorted([player for player in self.reader.get_players() if player.nationality == nationality], key=sort_by_points, reverse=True)

    def get_seasons(self):
        return ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]

    def get_nationalities(self):
        return sorted(list(set([player.nationality for player in self.reader.get_players()])))
