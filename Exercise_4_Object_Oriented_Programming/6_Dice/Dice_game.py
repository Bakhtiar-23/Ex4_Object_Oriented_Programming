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

    def get_dice_side(self):
        return self.dice.show_side()

    def __str__(self):
        return f"Player {self.name}, ID: {self.player_id}"

def main():
    # Part 1
    print("Part 1: Simple dice game")
    players = [Player("Player 1", 1), Player("Player 2", 2), Player("Player 3", 3)]

    for player in players:
        player.roll_dice()
        print(f"{player.name} rolled {player.get_dice_side()}")

    # Part 2
    print("\nPart 2: Add dices")
    num_dices = int(input("Enter the number of dices: "))
    players = [Player(f"Player {i}", i) for i in range(1, num_dices + 1)]

    for player in players:
        player.roll_dice()
        print(f"{player.name} rolled {player.get_dice_side()}")

    # Part 3
    print("\nPart 3: Add Players")
    players_dict = {}
    num_players = int(input("Enter the number of players: "))

    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ")
        player = Player(name, i)
        player.roll_dice()
        print(f"{player.name} rolled {player.get_dice_side()}")
        players_dict[player.player_id] = player

    # Part 4
    class Mammal:
        def __init__(self, ID, species, name, size, weight):
            self.ID = ID
            self.species = species
            self.name = name
            self.size = size
            self.weight = weight

    # Part 5
    print("\nPart 5: Add a pet mammal to each player")
    for player_id, player in players_dict.items():
        pet = Mammal(player_id, "Dog", "Fido", "Medium", "20kg")
        player.pet = pet
        print(f"{player.name}'s pet is {player.pet.name}, a {player.pet.species} weighing {player.pet.weight}")

    # Part 6
    print("\nPart 6: Select pet mammal using dice roll")
    for player_id, player in players_dict.items():
        player.roll_dice()
        dice_sum = player.get_dice_side()
        if dice_sum > 7:
            pet = Mammal(player_id, "Elephant", "Dumbo", "Large", "1000kg")
        else:
            pet = Mammal(player_id, "Cat", "Whiskers", "Small", "5kg")
        player.pet = pet
        print(f"{player.name}'s pet is {player.pet.name}, a {player.pet.species} weighing {player.pet.weight}")

if __name__ == "__main__":
    main()
