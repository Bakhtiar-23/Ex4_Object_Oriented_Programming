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

    def list_finished_tasks(self):
        return [task for task in self.tasks if task.finished]

    def list_unfinished_tasks(self):
        return [task for task in self.tasks if not task.finished]

    def mark_finished(self, task_id):
        found = False
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                found = True
                print(f"Task with id: {task_id} marked as finished.")
                break
        if not found:
            print("Error: No task with that id found.")

    def programmers(self):
        return list(set(task.programmer for task in self.tasks))

    def status_of_programmer(self, programmer):
        finished_tasks = [task for task in self.tasks if task.programmer == programmer and task.finished]
        unfinished_tasks = [task for task in self.tasks if task.programmer == programmer and not task.finished]
        total_finished = len(finished_tasks)
        total_unfinished = len(unfinished_tasks)
        hours_finished = sum(task.workload for task in finished_tasks)
        hours_unfinished = sum(task.workload for task in unfinished_tasks)
        return total_finished, total_unfinished, hours_finished, hours_unfinished


def print_tasks(tasks):
    for task in tasks:
        print(task)


def main():
    orders = OrderBook()

    while True:
        print("\ncommands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

        command = input("command: ")
        if command == '0':
            print("Exiting the program.")
            break
        elif command == '1':
            description = input("description: ")
            programmer, workload = input("programmer and workload estimate: ").split()
            orders.add_order(description, programmer, int(workload))
            print("added!")
        elif command == '2':
            finished_tasks = orders.list_finished_tasks()
            if not finished_tasks:
                print("no finished tasks")
            else:
                print_tasks(finished_tasks)
        elif command == '3':
            unfinished_tasks = orders.list_unfinished_tasks()
            if not unfinished_tasks:
                print("no unfinished tasks")
            else:
                print_tasks(unfinished_tasks)
        elif command == '4':
            task_id = input("id: ")
            try:
                orders.mark_finished(int(task_id))
            except ValueError:
                print("erroneous input")
        elif command == '5':
            programmers = orders.programmers()
            print(programmers)
        elif command == '6':
            programmer = input("programmer: ")
            try:
                status = orders.status_of_programmer(programmer)
                print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
            except ValueError:
                print("erroneous input")
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
