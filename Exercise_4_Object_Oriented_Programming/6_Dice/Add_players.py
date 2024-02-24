import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = random.randint(1, self.sides)

    def show_side(self):
        return self.value

class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()

    def roll_dice(self):
        self.dice.roll()

    def __str__(self):
        return f"Player ID: {self.player_id}, Name: {self.name}, Dice side: {self.dice.show_side()}"

def create_players(num_players):
    players = {}
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        player_id = i + 1
        players[player_id] = Player(name, player_id)
    return players

def roll_players_dice(players):
    for player in players.values():
        player.roll_dice()

def print_players_info(players):
    for player in players.values():
        print(player)

def test_game():
    num_players = int(input("Enter the number of players: "))
    players = create_players(num_players)
    roll_players_dice(players)
    print("Players information after rolling dice:")
    print_players_info(players)

if __name__ == "__main__":
    test_game()
