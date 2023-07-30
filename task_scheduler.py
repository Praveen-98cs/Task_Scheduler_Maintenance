import colorama

class Task:
    def __init__(self, name, description, due_date, priority, status="Pending", assignee=None):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.assignee = assignee

import os

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def assign_task(self, task_index, assignee):
        self.tasks[task_index].status = "Assigned"
        self.tasks[task_index].assignee = assignee

    def complete_task(self, task_index):
        self.tasks[task_index].status = "Completed"

    def save_tasks_to_file(self):
        with open("task_scheduler.txt", "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.name},{task.description},{task.due_date},{task.priority},{task.status},{task.assignee}\n"
                )

    def load_tasks_from_file(self):
        if not os.path.exists("task_scheduler.txt"):
            return

        with open("task_scheduler.txt", "r") as file:
            for line in file:
                name, description, due_date, priority, status, assignee = line.strip().split(",")
                task = Task(name, description, due_date, priority, status, assignee)
                self.tasks.append(task)

def print_menu():
    heading = "Task Scheduler Menu"
    menu_options = [
        "1. Create Task",
        "2. Assign Task",
        "3. Complete Task",
        "4. View All Tasks",
        "0. Exit",
    ]

    # Determine the width of the box
    box_width = max(len(heading), max(len(option) for option in menu_options)) + 4

    # Print the heading box
    print(colorama.Fore.CYAN + "=" * box_width)
    print(" " * ((box_width - len(heading)) // 2) + heading)
    print("=" * box_width + colorama.Fore.RESET)

    # Print the menu options
    for option in menu_options:
        print(colorama.Fore.YELLOW + "|" + colorama.Fore.RESET, option, " " * (box_width - len(option) - 3), colorama.Fore.YELLOW + "|" + colorama.Fore.RESET)

    # Print the bottom border of the box
    print(colorama.Fore.CYAN + "=" * box_width + colorama.Fore.RESET)

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    # Initialize colorama to enable colored output on Windows
    colorama.init()

    task_manager = TaskManager()
    task_manager.load_tasks_from_file()

    while True:
        print_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            name = get_user_input("Enter task name: ")
            description = get_user_input("Enter task description: ")
            due_date = get_user_input("Enter due date (YYYY-MM-DD): ")
            priority = get_user_input("Enter priority (High/Medium/Low): ")

            task = Task(name, description, due_date, priority)
            task_manager.create_task(task)
            print("Task created successfully.")

        elif choice == "2":
            if not task_manager.tasks:
                print("No tasks available. Create tasks first.")
                continue

            for i, task in enumerate(task_manager.tasks):
                print(f"{i}. {task.name} - {task.status}")

            task_index = int(get_user_input("Enter the index of the task to assign: "))
            assignee = get_user_input("Enter the name of the assignee: ")

            task_manager.assign_task(task_index, assignee)
            print("Task assigned successfully.")

        elif choice == "3":
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            for i, task in enumerate(task_manager.tasks):
                if task.status == "Assigned":
                    print(f"{i}. {task.name}")

            task_index = int(get_user_input("Enter the index of the completed task: "))
            task_manager.complete_task(task_index)
            print("Task completed successfully.")

        elif choice == "4":
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            print("\n===== All Tasks =====")
            for task in task_manager.tasks:
                print(
                    f"{task.name} - {task.description} - Due: {task.due_date} - Priority: {task.priority} - Status: {task.status}"
                )

        elif choice == "0":
            task_manager.save_tasks_to_file()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
