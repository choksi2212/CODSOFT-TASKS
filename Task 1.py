import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create a frame for the listbox and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Create a listbox to display tasks
        self.listbox = tk.Listbox(self.frame, width=50, height=15, bd=0, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry widget to add a new task
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=20)

        # Button to add a task
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Button to update a task
        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        # Button to delete a task
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Button to mark a task as completed
        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Load tasks if any exist
        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            selected_task = self.listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Update Task", "Update the selected task:", initialvalue=selected_task)
            if new_task:
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def complete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_task_index)
            self.listbox.delete(selected_task_index)
            self.listbox.insert(tk.END, task + " (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.save_tasks)
    root.mainloop()
