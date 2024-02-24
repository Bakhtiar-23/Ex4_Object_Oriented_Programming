from Item import Item
from suitcase import Suitcase

class CargoHold:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._suitcases = []

    def add_suitcase(self, suitcase):
        total_weight = sum(sum(item.weight() for item in suitcase._items) for suitcase in self._suitcases)
        if total_weight + sum(item.weight() for item in suitcase._items) <= self._max_weight:
            self._suitcases.append(suitcase)

    def __str__(self):
        num_suitcases = len(self._suitcases)
        total_space = self._max_weight - sum(sum(item.weight() for item in suitcase._items) for suitcase in self._suitcases)
        return f"{num_suitcases} {'suitcase' if num_suitcases == 1 else 'suitcases'}, space for {total_space:.1f}kg"

cargo_hold = CargoHold(100)
print(cargo_hold)

book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)

cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)

cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)
