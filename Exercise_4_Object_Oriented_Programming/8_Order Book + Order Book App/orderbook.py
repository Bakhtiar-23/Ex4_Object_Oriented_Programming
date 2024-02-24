from task import Task

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        unique_programmers = set(order.programmer for order in self.orders)
        return list(unique_programmers)


# Test the OrderBook class
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    #print(order)
    print()

for programmer in orders.programmers():
    print(programmer)