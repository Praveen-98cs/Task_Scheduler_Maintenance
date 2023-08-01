# Task Scheduler System

## Introduction

The Task Scheduler System is a simple command-line program that helps you manage your tasks efficiently. It allows you to create, assign, complete, and delete tasks with ease. This system provides a user-friendly interface to keep track of your tasks and their statuses.

## Features

- Create tasks with a name, description, due date, and priority.
- Assign tasks to specific individuals.
- Mark tasks as completed once they are finished.
- View all tasks in a tabular format.
- Delete tasks that are no longer needed.

## Prerequisites

Before running the Task Scheduler System, ensure that you have the following installed on your system:

- Python 3.x

Required libraries:

- colorama

## Getting Started

1. Extract the contents of the provided ZIP folder to your desired location on your computer.

2. Open a terminal or command prompt and navigate to the directory where the extracted files are located.

3. Install the required dependency by running the following command:

   ```
   pip install colorama
   ```

## How to Use

1. Open a terminal or command prompt in the directory where the files are located.

2. To run the Task Scheduler System, use the following command:

   ```
   python task_scheduler.py
   ```

3. The main menu will be displayed with various options:

   - **Create Task:** Enter task details such as name, description, due date (YYYY-MM-DD), and priority (High/Medium/Low).

   - **Assign Task:** Assign a task to a specific individual. You can choose from the list of tasks and provide the assignee's name.

   - **Complete Task:** Mark a task as completed. You can select the completed task from the list.

   - **View All Tasks:** Display a table with all tasks and their details, including name, description, due date, priority, status, and assignee (if assigned).

   - **Delete Task:** Delete a task from the list. You can select the task to be deleted from the table.

   - **Exit:** Save all tasks to the file and exit the program.

4. Date Format:

   When creating a task, enter the due date in the format `YYYY-MM-DD`. For example, `2023-12-31`.

5. Priority:

   When creating a task, specify the priority as one of `High`, `Medium`, or `Low`. The program is case-insensitive.

6. Assigning a Task:

   You can only assign tasks that are in the "Assigned" status. If a task is already assigned, you can change the assignee's name.

7. Saving and Loading:

   The tasks are automatically saved to a text file named `task_scheduler.txt`. When you run the program next time, it will load the tasks from this file.

## Usage

Here is a step-by-step guide with images to demonstrate how to use each function of the Task Scheduler System:

### Create Task

[Image: Create Task]

1. Select "Create Task" from the main menu.

2. Enter the task name, description, due date, and priority.

3. Press Enter to create the task.

### Assign Task

[Image: Assign Task]

1. Select "Assign Task" from the main menu.

2. View the list of tasks and their current status.

3. Enter the index of the task you want to assign.

4. If the task is unassigned, enter the name of the assignee and press Enter.

5. If the task is already assigned, you can change the assignee's name by entering a new name.

### Complete Task



1. Select "Complete Task" from the main menu.

2. View the list of assigned tasks.

3. Enter the index of the task you have completed and press Enter.

### View All Tasks



1. Select "View All Tasks" from the main menu.

2. A table will be displayed with all tasks and their details.

### Delete Task



1. Select "Delete Task" from the main menu.

2. View the list of tasks and their details in a table.

3. Enter the index of the task you want to delete and press Enter.

### Exit

Select "Exit" from the main menu to save all tasks to the file and exit the program.

## Additional Information

- The program uses the Colorama library to display colored output on Windows.

- The task details are stored in memory while the program is running. To persist the tasks between sessions, they are saved to the text file.

- The program checks for valid input for dates and priorities. It will prompt you to re-enter if the input is invalid.

## Troubleshooting

If you encounter any issues or have questions about the Task Scheduler System, please feel free to reach out to the developer at [1praveenbhawantha@gmail.com].

## License

This project is licensed under the [MIT License](LICENSE).

