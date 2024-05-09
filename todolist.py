import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(m, root):
        m.root = root
        m.root.title("To-Do List App")
        m.root.geometry("500x400")
        m.root.config(bg="#000000")  
        m.tasks = []

        m.task_entry = tk.Entry(root, width=30, font=('Arial', 14))
        m.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Task", command=m.add_task, font=('Arial', 12), bg="#2ecc71", fg="#ecf0f1")  # Set button colors
        add_button.grid(row=0, column=1, padx=10, pady=10)

        m.task_listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 12), bg="#ecf0f1", fg="#2c3e50", selectbackground="#3498db")  # Set listbox colors
        m.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        remove_button = tk.Button(root, text="Remove Task", command=m.remove_task, font=('Arial', 12), bg="#e74c3c", fg="#ecf0f1")  # Set button colors
        remove_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        complete_button = tk.Button(root, text="Complete Task", command=m.complete_task, font=('Arial', 12), bg="#58940B", fg="#ecf0f1")  # Set button colors
        complete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        m.task_listbox.bind('<Double-Button-1>', lambda event: m.complete_task())

    def add_task(m):
        task = m.task_entry.get()
        if task:
            m.tasks.append(task)
            m.update_task_list()
            m.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(m):
        selected_task_index = m.task_listbox.curselection()
        if selected_task_index:
            m.tasks.pop(selected_task_index[0])
            m.update_task_list()

    def complete_task(m):
        selected_task_index = m.task_listbox.curselection()
        if selected_task_index:
            completed_task = m.tasks.pop(selected_task_index[0])
            completed_task = f"[Done] {completed_task}"
            m.tasks.append(completed_task)
            m.update_task_list()

    def update_task_list(m):
        m.task_listbox.delete(0, tk.END)
        for task in m.tasks:
            m.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()



