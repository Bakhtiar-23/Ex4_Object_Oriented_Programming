class Task:
    def __init__(self, id, description, programmer, workload):
        self.id = id
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __repr__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.orders = []
        self.current_id = 1

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(self.current_id, description, programmer, workload))
        self.current_id += 1

    def mark_finished(self, task_id):
        found = False
        for order in self.orders:
            if order.id == task_id:
                order.finished = True
                found = True
                break
        if not found:
            raise ValueError("Task with given ID not found")

    def finished_orders(self):
        return [order for order in self.orders if order.finished]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.finished]

    def all_orders(self):
        return self.orders


# Usage Example
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.mark_finished(1)
orders.mark_finished(2)
for order in orders.all_orders():
    print(order)
