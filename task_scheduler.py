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

    def save_tasks_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.name},{task.description},{task.due_date},{task.priority},{task.status},{task.assignee}\n"
                )

    def load_tasks_from_file(self, filename):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            for line in file:
                name, description, due_date, priority, status, assignee = line.strip().split(",")
                task = Task(name, description, due_date, priority, status, assignee)
                self.tasks.append(task)


def print_menu():
    print("\n===== Task Scheduler Menu =====")
    print("1. Create Task")
    print("2. Assign Task")
    print("3. Complete Task")
    print("4. View All Tasks")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("0. Exit")


def get_user_input(prompt):
    return input(prompt).strip()


def main():
    task_manager = TaskManager()

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

        elif choice == "5":
            filename = get_user_input("Enter the filename to save tasks (e.g., tasks.txt): ")
            task_manager.save_tasks_to_file(filename)
            print("Tasks saved successfully.")

        elif choice == "6":
            filename = get_user_input("Enter the filename to load tasks from (e.g., tasks.txt): ")
            task_manager.load_tasks_from_file(filename)
            print("Tasks loaded successfully.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to go back to the main menu.")

if __name__ == "__main__":
    main()
