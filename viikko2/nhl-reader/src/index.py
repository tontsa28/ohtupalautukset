import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    def sort_by_points(player):
        return player.points

    print("Players from FIN\n")
    players.sort(key=sort_by_points, reverse=True)

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
