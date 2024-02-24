import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = random.randint(1, self.sides)

    def show_side(self):
        return self.value

def roll_dice(dice_list):
    for dice in dice_list:
        dice.roll()

def get_sum_of_rolls(dice_list):
    return sum(dice.show_side() for dice in dice_list)

def play_game(num_dice):
    dice_list = [Dice() for _ in range(num_dice)]

    roll_dice(dice_list)
    sum_of_rolls = get_sum_of_rolls(dice_list)

    print("Initial rolls:", [dice.show_side() for dice in dice_list])
    print("Initial sum of rolls:", sum_of_rolls)

    while True:
        max_sum = max(get_sum_of_rolls(dice_list) for _ in range(num_dice))
        if get_sum_of_rolls(dice_list) == max_sum:
            break
        else:
            roll_dice(dice_list)

    print("Winner:", [dice.show_side() for dice in dice_list])
    print("Winner sum of rolls:", get_sum_of_rolls(dice_list))

def test_game():
    num_dice = 3
    print(f"Playing game with {num_dice} dice:")
    play_game(num_dice)

if __name__ == "__main__":
    test_game()
