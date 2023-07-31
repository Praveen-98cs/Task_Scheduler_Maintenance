# Task_Scheduler_Maintenance
This a simple python Task Scheduler created for an assignment given in the university under the course module, Enterprise Application Development 
Task Scheduler
The Task Scheduler is a simple command-line program that allows you to create, assign, complete, and delete tasks. It provides a user-friendly interface for managing your tasks efficiently.

## Prerequisites
Before running the Task Scheduler, make sure you have the following installed on your system:
Python 3.x

## Getting Started
Clone the repository or download the source code.

Navigate to the project directory in your terminal.

Install the required dependencies by running the following command:

pip install colorama

## How to Use
Run the program by executing the following command:
Copy code
python task_scheduler.py
Main Menu Options:

#### Create Task:
Allows you to create a new task by providing the task name, description, due date, and priority.

#### Assign Task:
Lists all tasks and their current status. Enter the index of the task you want to assign and provide the name of the assignee.

#### Complete Task: 
Lists all assigned tasks. Enter the index of the task you have completed.

#### View All Tasks:
Displays a table of all tasks with their details, including name, description, due date, priority, status, and assignee (if assigned).

#### Delete Task:
Lists all tasks and their details in a table. Enter the index of the task you want to delete.

#### Exit: Save
all tasks to the file and exit the program.

### Date Format:

When creating a task, enter the due date in the format YYYY-MM-DD. For example, 2023-12-31.

## Priority:

When creating a task, specify the priority as one of High, Medium, or Low. The program is case-insensitive.

## Assigning a Task:

You can only assign tasks that are in the "Assigned" status. If a task is already assigned, you can change the assignee's name.

## Saving and Loading:

The tasks are automatically saved to a text file named task_scheduler.txt. When you run the program next time, it will load the tasks from this file.

## Termination:

To terminate the program, enter 0 in the main menu.

## Additional Information
The program uses the Colorama library to display colored output on Windows.

The task details are stored in memory while the program is running. To persist the tasks between sessions, they are saved to the text file.

The program checks for valid input for dates and priorities. It will prompt you to re-enter if the input is invalid.

## Troubleshooting
If you encounter any issues or have questions about the Task Scheduler, please feel free to reach out to the developer at [1praveenbhawantha@gmail.com].

## License
This project is licensed under the MIT License.
