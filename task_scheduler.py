class Task:
    def __init__(self, name, description, due_date, priority, status="Pending"):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

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
                    f"{task.name},{task.description},{task.due_date},{task.priority},{task.status}\n"
                )

    def load_tasks_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    name, description, due_date, priority, status = line.strip().split(",")
                    task = Task(name, description, due_date, priority, status)
                    self.tasks.append(task)

def print_menu(user):
    print("\n===== Task Scheduler Menu =====")
    print("\n===== Created by Praveen CS/2017/017 =====")
    print("1. Create Task")
    if user.role in ["Admin", "Task Admin"]:
        print("2. Assign Task")
    if user.role in ["Admin", "Task Admin"]:
        print("3. Complete Task")
    print("4. View All Tasks")
    if user.role in ["Admin", "Task Admin"]:
        print("5. Save Tasks to File")
    if user.role in ["Admin", "Task Admin"]:
        print("6. Load Tasks from File")
    print("0. Exit")

def get_user_input(prompt):
    return input(prompt).strip()

class User:
    def __init__(self, role):
        self.role = role

def login():
    print("\n===== Login =====")
    username = get_user_input("Enter your username: ")
    password = get_user_input("Enter your password: ")

    # In a real application, you'd validate the username and password against a database or some other method.
    # For simplicity, we'll use hardcoded credentials here.
    users = {
        "admin": User("Admin"),
        "task_admin": User("Task Admin"),
        "user": User("Normal User"),
    }

    if username in users and password == "password":
        return users[username]
    else:
        print("Invalid username or password.")
        return None

def main():
    user = login()
    if not user:
        return

    task_manager = TaskManager()

    while True:
        print_menu(user)
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            name = get_user_input("Enter task name: ")
            description = get_user_input("Enter task description: ")
            due_date = get_user_input("Enter due date (YYYY-MM-DD): ")
            priority = get_user_input("Enter priority (High/Medium/Low): ")

            task = Task(name, description, due_date, priority)
            task_manager.create_task(task)
            print("Task created successfully.")

        # Rest of the code snippets will be added in the second part.
def main():
    user = login()
    if not user:
        return

    task_manager = TaskManager()

    while True:
        print_menu(user)
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            name = get_user_input("Enter task name: ")
            description = get_user_input("Enter task description: ")
            due_date = get_user_input("Enter due date (YYYY-MM-DD): ")
            priority = get_user_input("Enter priority (High/Medium/Low): ")

            task = Task(name, description, due_date, priority)
            task_manager.create_task(task)
            print("Task created successfully.")

        elif choice == "2" and user.role in ["Admin", "Task Admin"]:
            if not task_manager.tasks:
                print("No tasks available. Create tasks first.")
                continue

            print("\n===== Task Assignment =====")
            for i, task in enumerate(task_manager.tasks):
                if task.status == "Pending":
                    print(f"{i}. {task.name}")

            task_index = int(get_user_input("Enter the index of the task to assign: "))
            if 0 <= task_index < len(task_manager.tasks):
                assignee = get_user_input("Enter the name of the assignee: ")
                task_manager.assign_task(task_index, assignee)
                print("Task assigned successfully.")
            else:
                print("Invalid task index.")

        elif choice == "3" and user.role in ["Admin", "Task Admin"]:
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            print("\n===== Task Completion =====")
            for i, task in enumerate(task_manager.tasks):
                if task.status == "Assigned":
                    print(f"{i}. {task.name}")

            task_index = int(get_user_input("Enter the index of the completed task: "))
            if 0 <= task_index < len(task_manager.tasks):
                task_manager.complete_task(task_index)
                print("Task completed successfully.")
            else:
                print("Invalid task index.")

        elif choice == "4":
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            print("\n===== All Tasks =====")
            for task in task_manager.tasks:
                print(
                    f"{task.name} - {task.description} - Due: {task.due_date} - Priority: {task.priority} - Status: {task.status}"
                )

        elif choice == "5" and user.role in ["Admin", "Task Admin"]:
            filename = get_user_input("Enter the filename to save tasks (e.g., tasks.txt): ")
            task_manager.save_tasks_to_file(filename)
            print("Tasks saved successfully.")

        elif choice == "6" and user.role in ["Admin", "Task Admin"]:
            filename = get_user_input("Enter the filename to load tasks from (e.g., tasks.txt): ")
            task_manager.load_tasks_from_file(filename)
            print("Tasks loaded successfully.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
