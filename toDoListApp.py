import tkinter as tk

class toDoList:
    def __init__(self):
        self.toDos = []

    def addTodo(self, toDo):
        self.toDos.append(toDo)

    def delToDo(self, toDo):
        if toDo in self.toDos:
            self.toDos.remove(toDo)

    def isToDoDone(self, toDo):
        if toDo.isDone:
            pass
        else:
            print("You still have not done with this to do")

    def showToDoList(self):
        return self.toDos

class ToDo:
    def __init__(self, description):
        self.description = description
        self.isDone = False

    def __str__(self):
        status = "Done" if self.isDone else "Not Done yet!"
        return f"{self.description} - {status}"

class toDoApp:
    def __init__(self, master):
        self.master = master
        master.title("ToDo List App")

        self.todo_list = toDoList()

        self.label = tk.Label(master, text="ToDo List App")
        self.label.pack()

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.pack()
        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.show_button = tk.Button(master, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack()

        self.done_button = tk.Button(master, text="Mark as Done", command=self.mark_done)
        self.done_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.task_listbox = tk.Listbox(master)
        self.task_listbox = tk.Listbox(master, height=15)
        self.task_listbox = tk.Listbox(master, width=45)

        self.task_listbox.pack()

        master.geometry("400x300")

    def add_task(self):
        task = self.task_entry.get()
        todo = ToDo(task)
        self.todo_list.addTodo(todo)
        self.show_tasks()

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        todos = self.todo_list.showToDoList()
        for i, todo in enumerate(todos, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {todo}")

    def mark_done(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            todo = self.todo_list.toDos[task_index[0]]
            todo.isDone = True
            print("Task marked as done.")
            self.show_tasks()

    def delete_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            todo = self.todo_list.toDos[task_index[0]]
            self.todo_list.delToDo(todo)
            print("Task deleted.")
            self.show_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = toDoApp(root)
    root.mainloop()
