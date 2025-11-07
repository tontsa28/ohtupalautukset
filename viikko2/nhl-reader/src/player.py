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
