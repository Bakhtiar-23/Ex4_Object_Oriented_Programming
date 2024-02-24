from Mammal_ import Mammal

class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.pet = None  # Initialize pet as None

    def set_pet(self, mammal):
        if isinstance(mammal, Mammal):
            self.pet = mammal
        else:
            raise ValueError("Pet must be a Mammal object")

    def __str__(self):
        if self.pet:
            return f"Player: {self.name}, ID: {self.player_id}, Pet: {self.pet}"
        else:
            return f"Player: {self.name}, ID: {self.player_id}, No pet assigned"


if __name__ == "__main__":
    # Create some Mammal objects
    mammal1 = Mammal(1, "Dog", "Max", "Medium", "20 kg")
    mammal2 = Mammal(2, "Cat", "Whiskers", "Small", "5 kg")
    mammal3 = Mammal(3, "Elephant", "Dumbo", "Large", "2000 kg")

    # Create some Player objects and assign pets
    player1 = Player("Alice", 101)
    player1.set_pet(mammal1)

    player2 = Player("Bob", 102)
    player2.set_pet(mammal2)

    player3 = Player("Charlie", 103)
    player3.set_pet(mammal3)

    # Print player information
    print(player1)
    print(player2)
    print(player3)
