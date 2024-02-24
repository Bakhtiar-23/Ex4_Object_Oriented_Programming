import random
from Mammal_ import Mammal
from Add_attribute import Player

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def select_mammal(players, mammals):
    for player in players:
        sum_dice = roll_dice()
        print(f"{player.name} rolled {sum_dice}")
        
        # Find the mammal with weight closest to the sum of the dice
        closest_weight_diff = float('inf')
        selected_mammal = None
        for mammal in mammals:
            weight_diff = abs(int(mammal.weight[:-3]) - sum_dice)
            if weight_diff < closest_weight_diff:
                closest_weight_diff = weight_diff
                selected_mammal = mammal

        # Assign the selected mammal as the player's pet
        player.set_pet(selected_mammal)

        # Print player's information and selected pet's information
        print(player)
        print(f"Selected pet: {selected_mammal.name}, Species: {selected_mammal.species}, Size: {selected_mammal.size}, Weight: {selected_mammal.weight}\n")

if __name__ == "__main__":
    # Create some Mammal objects
    mammals = [
        Mammal(1, "Dog", "Max", "Medium", "20 kg"),
        Mammal(2, "Cat", "Whiskers", "Small", "5 kg"),
        Mammal(3, "Elephant", "Dumbo", "Large", "2000 kg")
    ]

    # Create some Player objects
    players = [
        Player("Alice", 101),
        Player("Bob", 102),
        Player("Charlie", 103)
    ]

    # Select pet mammal for each player
    select_mammal(players, mammals)
