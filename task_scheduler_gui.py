import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog

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

    def create_task(self, task):
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

class TaskSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Scheduler Application")

        self.task_manager = TaskManager()

        self.create_widgets()

    def create_widgets(self):
        lbl_instructions = tk.Label(self.root, text="Select an option:")
        lbl_instructions.pack()

        btn_create_task = tk.Button(self.root, text="1. Create Task", command=self.create_task)
        btn_create_task.pack()

        btn_assign_task = tk.Button(self.root, text="2. Assign Task", command=self.assign_task)
        btn_assign_task.pack()

        btn_complete_task = tk.Button(self.root, text="3. Complete Task", command=self.complete_task)
        btn_complete_task.pack()

        btn_view_tasks = tk.Button(self.root, text="4. View All Tasks", command=self.view_all_tasks)
        btn_view_tasks.pack()

        btn_save_tasks = tk.Button(self.root, text="5. Save Tasks to File", command=self.save_tasks)
        btn_save_tasks.pack()

        btn_load_tasks = tk.Button(self.root, text="6. Load Tasks from File", command=self.load_tasks)
        btn_load_tasks.pack()

        btn_exit = tk.Button(self.root, text="0. Exit", command=self.root.destroy)
        btn_exit.pack()

        self.listbox_tasks = tk.Listbox(self.root, width=60)
        self.listbox_tasks.pack()

    def create_task(self):
        self.clear_listbox()
        lbl_instructions = tk.Label(self.root, text="Enter task details below:")
        lbl_instructions.pack()

        self.task_name_var = tk.StringVar()
        lbl_name = tk.Label(self.root, text="Task Name:")
        lbl_name.pack()
        entry_name = tk.Entry(self.root, textvariable=self.task_name_var)
        entry_name.pack()

        self.task_description_var = tk.StringVar()
        lbl_description = tk.Label(self.root, text="Task Description:")
        lbl_description.pack()
        entry_description = tk.Entry(self.root, textvariable=self.task_description_var)
        entry_description.pack()

        self.task_due_date_var = tk.StringVar()
        lbl_due_date = tk.Label(self.root, text="Due Date (YYYY-MM-DD):")
        lbl_due_date.pack()
        entry_due_date = tk.Entry(self.root, textvariable=self.task_due_date_var)
        entry_due_date.pack()

        self.task_priority_var = tk.StringVar()
        lbl_priority = tk.Label(self.root, text="Priority (High/Medium/Low):")
        lbl_priority.pack()
        entry_priority = tk.Entry(self.root, textvariable=self.task_priority_var)
        entry_priority.pack()

        btn_add_task = tk.Button(self.root, text="Add Task", command=self.add_task)
        btn_add_task.pack()

    def add_task(self):
        name = self.task_name_var.get()
        description = self.task_description_var.get()
        due_date = self.task_due_date_var.get()
        priority = self.task_priority_var.get()

        task = Task(name, description, due_date, priority)
        self.task_manager.create_task(task)

        self.listbox_tasks.insert(tk.END, f"{task.name} - {task.status}")

    def assign_task(self):
        self.clear_listbox()
        lbl_instructions = tk.Label(self.root, text="Enter task index and assignee below:")
        lbl_instructions.pack()

        self.task_index_var = tk.IntVar()
        lbl_task_index = tk.Label(self.root, text="Task Index:")
        lbl_task_index.pack()
        entry_task_index = tk.Entry(self.root, textvariable=self.task_index_var)
        entry_task_index.pack()

        self.task_assignee_var = tk.StringVar()
        lbl_assignee = tk.Label(self.root, text="Assignee:")
        lbl_assignee.pack()
        entry_assignee = tk.Entry(self.root, textvariable=self.task_assignee_var)
        entry_assignee.pack()

        btn_confirm_assignment = tk.Button(self.root, text="Assign Task", command=self.confirm_assignment)
        btn_confirm_assignment.pack()

    def confirm_assignment(self):
        task_index = self.task_index_var.get()
        assignee = self.task_assignee_var.get()

        if task_index < 0 or task_index >= len(self.task_manager.tasks):
            messagebox.showerror("Error", "Invalid task index")
            return

        task = self.task_manager.tasks[task_index]
        task.status = "Assigned"
        task.assignee = assignee

        self.listbox_tasks.delete(task_index)
        self.listbox_tasks.insert(task_index, f"{task.name} - {task.status}")

    def complete_task(self):
        self.clear_listbox()
        lbl_instructions = tk.Label(self.root, text="Enter task index to mark as completed:")
        lbl_instructions.pack()

        self.task_index_var = tk.IntVar()
        lbl_task_index = tk.Label(self.root, text="Task Index:")
        lbl_task_index.pack()
        entry_task_index = tk.Entry(self.root, textvariable=self.task_index_var)
        entry_task_index.pack()

        btn_confirm_completion = tk.Button(self.root, text="Complete Task", command=self.confirm_completion)
        btn_confirm_completion.pack()

    def confirm_completion(self):
        task_index = self.task_index_var.get()

        if task_index < 0 or task_index >= len(self.task_manager.tasks):
            messagebox.showerror("Error", "Invalid task index")
            return

        task = self.task_manager.tasks[task_index]
        task.status = "Completed"

        self.listbox_tasks.delete(task_index)
        self.listbox_tasks.insert(task_index, f"{task.name} - {task.status}")

    def view_all_tasks(self):
        self.clear_listbox()
        for task in self.task_manager.tasks:
            self.listbox_tasks.insert(tk.END, f"{task.name} - {task.status}")

    def save_tasks(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not filename:
            return

        with open(filename, "w") as file:
            for task in self.task_manager.tasks:
                file.write(f"{task.name},{task.description},{task.due_date},{task.priority},{task.status},{task.assignee}\n")

    def load_tasks(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not filename:
            return

        self.clear_listbox()
        self.task_manager.tasks = []
        with open(filename, "r") as file:
            for line in file:
                name, description, due_date, priority, status, assignee = line.strip().split(",")
                task = Task(name, description, due_date, priority, status, assignee)
                self.task_manager.tasks.append(task)

        self.view_all_tasks()

    def clear_listbox(self):
        self.listbox_tasks.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TaskSchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
