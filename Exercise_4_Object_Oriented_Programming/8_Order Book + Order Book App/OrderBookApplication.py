# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    current_id = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.current_id
        Task.current_id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set(order.programmer for order in self.orders))

    def mark_finished(self, task_id):
        found = False
        for order in self.orders:
            if order.id == task_id:
                order.mark_finished()
                found = True
                break
        if not found:
            raise ValueError("Task with given ID not found")

    def finished_orders(self):
        return [order for order in self.orders if order.finished]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.finished]

    def status_of_programmer(self, programmer):
        finished_tasks = sum(1 for order in self.orders if order.programmer == programmer and order.finished)
        unfinished_tasks = sum(1 for order in self.orders if order.programmer == programmer and not order.finished)
        finished_workload = sum(order.workload for order in self.orders if order.programmer == programmer and order.finished)
        unfinished_workload = sum(order.workload for order in self.orders if order.programmer == programmer and not order.finished)
        if finished_tasks == 0 and unfinished_tasks == 0:
            raise ValueError("No programmer with the given name")
        return finished_tasks, unfinished_tasks, finished_workload, unfinished_workload


def main():
    orders = OrderBook()

    while True:
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

        command = input("command: ")

        if command == "0":
            break
        elif command == "1":
            try:
                description = input("description: ")
                programmer, workload = input("programmer and workload estimate: ").split()
                workload = int(workload)
                orders.add_order(description, programmer, workload)
                print("added!")
            except (ValueError, TypeError):
                print("erroneous input")
        elif command == "2":
            finished_tasks = orders.finished_orders()
            if not finished_tasks:
                print("no finished tasks")
            else:
                for task in finished_tasks:
                    print(task)
        elif command == "3":
            unfinished_tasks = orders.unfinished_orders()
            for task in unfinished_tasks:
                print(task)
        elif command == "4":
            try:
                task_id = int(input("id: "))
                orders.mark_finished(task_id)
                print("marked as finished")
            except ValueError:
                print("erroneous input")
        elif command == "5":
            programmers = orders.programmers()
            for programmer in programmers:
                print(programmer)
        elif command == "6":
            try:
                programmer = input("programmer: ")
                status = orders.status_of_programmer(programmer)
                print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
            except ValueError:
                print("erroneous input")
        else:
            print("erroneous input")


print("commands:")
print("0 exit")
print("1 add order")
print("2 list finished tasks")
print("3 list unfinished tasks")
print("4 mark task as finished")
print("5 programmers")
print("6 status of programmer")
