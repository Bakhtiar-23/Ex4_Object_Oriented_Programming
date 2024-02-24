from Item import Item

class Suitcase:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._items = []

    def add_item(self, item):
        total_weight = sum(item.weight() for item in self._items)
        if total_weight + item.weight() <= self._max_weight:
            self._items.append(item)

    def __str__(self):
        total_items = len(self._items)
        total_weight = sum(item.weight() for item in self._items)
        item_str = "item" if total_items == 1 else "items"  # Adjust plural based on total_items
        return f"{total_items} {item_str} ({total_weight}g)"
    
    
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

suitcase = Suitcase(500)
print(suitcase)

suitcase.add_item(book)
print(suitcase)

suitcase.add_item(phone)
print(suitcase)

suitcase.add_item(brick)
print(suitcase)
