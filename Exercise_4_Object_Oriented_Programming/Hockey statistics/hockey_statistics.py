import json

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:<20}{self.team:>5}{self.goals:>3} + {self.assists:>3} = {self.points():>3}"

class NHLStats:
    def __init__(self, file_name):
        self.players = []
        self.load_data(file_name)

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for player_data in data:
                    player = Player(**player_data)
                    self.players.append(player)
                print(f"read the data of {len(self.players)} players")
        except FileNotFoundError:
            print("File not found.")

    def search_player(self, name):
        for player in self.players:
            if player.name == name:
                print(player)
                return
        print("Player not found.")

    def list_teams(self):
        teams = sorted(set(player.team for player in self.players))
        for team in teams:
            print(team)

    def list_countries(self):
        countries = sorted(set(player.nationality for player in self.players))
        for country in countries:
            print(country)

    def list_players_in_team(self, team):
        team_players = [player for player in self.players if player.team == team]
        if team_players:
            sorted_players = sorted(team_players, key=lambda player: player.points(), reverse=True)
            for player in sorted_players:
                print(player)
        else:
            print("No players found for the team.")

    def list_players_from_country(self, country):
        country_players = [player for player in self.players if player.nationality == country]
        if country_players:
            sorted_players = sorted(country_players, key=lambda player: player.points(), reverse=True)
            for player in sorted_players:
                print(player)
        else:
            print("No players found from the country.")

    def most_points(self, n):
        sorted_players = sorted(self.players, key=lambda player: (player.points(), player.goals), reverse=True)[:n]
        for player in sorted_players:
            print(player)

    def most_goals(self, n):
        sorted_players = sorted(self.players, key=lambda player: (player.goals, player.games))[:n]
        for player in sorted_players:
            print(player)

def main():
    file_name = input("file name: ")
    stats = NHLStats(file_name)

    while True:
        print("\ncommands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

        command = input("command: ")

        if command == "0":
            break
        elif command == "1":
            name = input("name: ")
            stats.search_player(name)
        elif command == "2":
            stats.list_teams()
        elif command == "3":
            stats.list_countries()
        elif command == "4":
            team = input("team: ")
            stats.list_players_in_team(team)
        elif command == "5":
            country = input("country: ")
            stats.list_players_from_country(country)
        elif command == "6":
            n = int(input("how many: "))
            stats.most_points(n)
        elif command == "7":
            n = int(input("how many: "))
            stats.most_goals(n)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
