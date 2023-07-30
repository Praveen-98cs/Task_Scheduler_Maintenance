import os
import colorama
import re

class Task:
    def __init__(self, name, description, due_date, priority, status="Pending", assignee=None):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.assignee = assignee

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.filename = "task_scheduler.txt"  # Define the filename

        # Load tasks from the existing file (if available)
        self.load_tasks_from_file()

    def create_task(self, task):
        self.tasks.append(task)

    def assign_task(self, task_index, assignee):
        self.tasks[task_index].status = "Assigned"
        self.tasks[task_index].assignee = assignee

    def complete_task(self, task_index):
        self.tasks[task_index].status = "Completed"

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
            self.save_tasks_to_file()  # Automatically save tasks after deletion
        else:
            print("Invalid task index. Please enter a valid task index.")

    def save_tasks_to_file(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.name},{task.description},{task.due_date},{task.priority},{task.status},{task.assignee}\n"
                )

    def load_tasks_from_file(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                name, description, due_date, priority, status, assignee = line.strip().split(",")
                task = Task(name, description, due_date, priority, status, assignee)
                self.tasks.append(task)

def print_menu():
    print("\n" + colorama.Fore.CYAN + "=" * 28 + " Task Scheduler Menu " + "=" * 28 + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "1. Create Task")
    print("2. Assign Task")
    print("3. Complete Task")
    print("4. View All Tasks")
    print("5. Delete Task")
    print("0. Exit" + colorama.Fore.RESET)

def get_user_input(prompt):
    while True:
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            print("Input interrupted. Please try again.")
        except Exception as e:
            print("Invalid value. Please try again.")

def is_valid_date(date):
    # Check if the date is in the format YYYY-MM-DD
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if not date_pattern.match(date):
        return False

    # Extract year, month, and day from the date string
    year, month, day = map(int, date.split("-"))

    # Check if the month is between 1 and 12, and day is between 1 and 31
    return 1 <= month <= 12 and 1 <= day <= 31

def is_valid_priority(priority):
    # Check if the priority is one of "High", "Medium", or "Low" (case insensitive)
    return priority.lower() in ["high", "medium", "low"]

def press_enter_to_continue():
    input("Hit Enter to go to Main Menu")

def main():
    # Initialize colorama to enable colored output on Windows
    colorama.init()

    task_manager = TaskManager()

    while True:
        print_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            name = get_user_input("Enter task name: ")
            description = get_user_input("Enter task description: ")

            # Get and validate the due date input
            while True:
                due_date = get_user_input("Enter due date (YYYY-MM-DD): ")
                if is_valid_date(due_date):
                    break
                else:
                    print("Invalid date format or out-of-range values. Please enter a valid date in the format YYYY-MM-DD.")

            # Get and validate the priority input
            while True:
                priority = get_user_input("Enter priority (High/Medium/Low): ")
                if is_valid_priority(priority):
                    break
                else:
                    print("Invalid priority. Please enter one of 'High', 'Medium', or 'Low'.")

            task = Task(name, description, due_date, priority)
            task_manager.create_task(task)
            print("Task created successfully.")
            task_manager.save_tasks_to_file()  # Automatically save tasks after creation

            press_enter_to_continue()

        elif choice == "2":
            if not task_manager.tasks:
                print("No tasks available. Create tasks first.")
                continue

            for i, task in enumerate(task_manager.tasks):
                print(f"{i}. {task.name} - {task.status}")

            while True:
                try:
                    task_index = int(get_user_input("Enter the index of the task to assign: "))
                    assignee = get_user_input("Enter the name of the assignee: ")

                    task_manager.assign_task(task_index, assignee)
                    print("Task assigned successfully.")
                    task_manager.save_tasks_to_file()  # Automatically save tasks after assignment
                    break  # Exit the loop if task assignment is successful
                except ValueError:
                    print("Invalid value. Please enter a valid task index.")
                except IndexError:
                    print("Invalid task index. Please enter a valid task index.")

            press_enter_to_continue()

        elif choice == "3":
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            for i, task in enumerate(task_manager.tasks):
                if task.status == "Assigned":
                    print(f"{i}. {task.name}")

            while True:
                try:
                    task_index = int(get_user_input("Enter the index of the completed task: "))
                    task_manager.complete_task(task_index)
                    print("Task completed successfully.")
                    task_manager.save_tasks_to_file()  # Automatically save tasks after completion
                    break  # Exit the loop if task completion is successful
                except ValueError:
                    print("Invalid value. Please enter a valid task index.")
                except IndexError:
                    print("Invalid task index. Please enter a valid task index.")

            press_enter_to_continue()

        elif choice == "4":
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            print("\n===== All Tasks =====")
            for task in task_manager.tasks:
                print(
                    f"{task.name} - {task.description} - Due: {task.due_date} - Priority: {task.priority} - Status: {task.status}"
                )

            press_enter_to_continue()

        elif choice == "5":
            if not task_manager.tasks:
                print("No tasks available.")
                continue

            for i, task in enumerate(task_manager.tasks):
                print(f"{i}. {task.name}")

            while True:
                try:
                   task_index = int(get_user_input("Enter the index of the task to delete: "))
                   task_manager.delete_task(task_index)
                   break  # Exit the loop if task deletion is successful
                except ValueError:
                   print("Invalid value. Please enter a valid task index.")
                except IndexError:
                   print("Invalid task index. Please enter a valid task index.")
            press_enter_to_continue()

        elif choice == "0":
            task_manager.save_tasks_to_file()  # Save tasks before exiting
            break

        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Task Scheduler!")

if __name__ == "__main__":
    main()
