from player import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()

def render_top_scorers_by_nationality(stats, season, nationality: str):
    players = stats.top_scorers_by_nationality(nationality)
    if not players:
        console.print(f"No players from {nationality}", style="bold red")
        return

    title = f"Season {season} players from {nationality}"
    table = Table(title=title, box=box.SQUARE)
    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))

    console.print(table)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    season = Prompt.ask("Season", choices=stats.get_seasons(), default="2024-25")

    while True:
        nationality = Prompt.ask("Nationality", choices=stats.get_nationalities(), default="")
        if nationality == "":
            continue

        render_top_scorers_by_nationality(stats, season, nationality.upper())

if __name__ == "__main__":
    main()
