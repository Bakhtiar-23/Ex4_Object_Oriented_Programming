class Task:
    next_id = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.next_id
        Task.next_id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.tasks.append(task)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set(task.programmer for task in self.tasks))

    def mark_finished(self, task_id):
        found = False
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                found = True
                break
        if not found:
            raise ValueError(f"No task with id {task_id} found.")

    def finished_orders(self):
        return [task for task in self.tasks if task.finished]

    def unfinished_orders(self):
        return [task for task in self.tasks if not task.finished]

    def status_of_programmer(self, programmer):
        finished_tasks = [task for task in self.tasks if task.programmer == programmer and task.finished]
        unfinished_tasks = [task for task in self.tasks if task.programmer == programmer and not task.finished]
        total_finished = len(finished_tasks)
        total_unfinished = len(unfinished_tasks)
        hours_finished = sum(task.workload for task in finished_tasks)
        hours_unfinished = sum(task.workload for task in unfinished_tasks)
        return total_finished, total_unfinished, hours_finished, hours_unfinished


# Part 1: Testing Task class
print("\nPart 1:")
t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.finished)
t1.mark_finished()
print(t1)
print(t1.finished)
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)

# Part 2: Testing OrderBook class
print("\nPart 2:")
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)
print()
for programmer in orders.programmers():
    print(programmer)

# Part 3: Testing mark_finished method
print("\nPart 3:")

orders.mark_finished(4)  # Marking task with ID 4 as finished
orders.mark_finished(5)  # Marking task with ID 5 as finished


# Print all orders after marking
for order in orders.all_orders():
    print(order)
    

# Part 4: Testing status_of_programmer method
print("\nPart 4:")
status = orders.status_of_programmer("Adele")
print(f"Status of programmer Adele: {status}")
