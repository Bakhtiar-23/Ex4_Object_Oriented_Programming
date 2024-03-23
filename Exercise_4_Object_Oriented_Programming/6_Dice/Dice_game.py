import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()

    def roll_dice(self):
        return self.dice.roll()

    def __str__(self):
        return f"Player {self.name} (ID: {self.player_id})"

def play_dice_game(players):
    while True:
        player_scores = {}
        for player in players:
            score = sum(player.roll_dice() for _ in range(3))
            player_scores[player] = score
            print(f"{player}: {score}")

        max_score = max(player_scores.values())
        winners = [player for player, score in player_scores.items() if score == max_score]

        if len(winners) == 1:
            print(f"\nWinner: {winners[0]} with a score of {max_score}")
            break
        else:
            print("Tie! Rolling again...")
            continue

def main():
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ")
        player_id = i
        players.append(Player(name, player_id))

    play_dice_game(players)

    # Part 4: Create a mammal object
    class Mammal:
        def __init__(self, ID, species, name, size, weight):
            self.ID = ID
            self.species = species
            self.name = name
            self.size = size
            self.weight = weight

    # Part 5: Add pet attribute to Player class
    for player in players:
        player.pet = Mammal(player.player_id, "Mammal", f"{player.name}'s pet", random.randint(10, 50), random.randint(5, 30))

    # Part 6: Let players select their pet mammal
    print("\nSelecting pets based on dice rolls:")
    for player in players:
        pet_roll = sum(player.roll_dice() for _ in range(2))
        print(f"{player}: Rolled {pet_roll} for pet selection")
        if pet_roll > 7:
            player.pet.species = "Elephant"
            player.pet.size = 50
            player.pet.weight = 500
        else:
            player.pet.species = "Rabbit"
            player.pet.size = 10
            player.pet.weight = 15

    # Print each player and their pet information
    print("\nPlayers and their pets:")
    for player in players:
        print(f"{player}: {player.pet.species} named {player.pet.name}, size: {player.pet.size}, weight: {player.pet.weight}")

if __name__ == "__main__":
    main()
