import tkinter
from functools import partial
from tkinter import Tk, Frame, Listbox, Scrollbar, Button
from tkinter.constants import END, SEL_FIRST, SEL_LAST

from repository.index import todoRepository
from ui.AddTodo import AddTodo
from ui.UpdateTodo import UpdateTodo


class ListTodo:
    tasks = None
    window = None
    add_task_window = None

    def __init__(self):
        self.window = Tk()
        # giving a title
        self.window.title("To Do List")

        frame_task = Frame(self.window)
        frame_task.pack()

        self.listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font="Helvetica")
        self.update_task_list()

        self.listbox_task.pack(side=tkinter.LEFT)

        scrollbar_task = Scrollbar(frame_task)
        scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox_task.config(yscrollcommand=scrollbar_task.set)
        scrollbar_task.config(command=self.listbox_task.yview)

        entry_button = Button(self.window, text="Add task", width=50, command=partial(self.add_task))
        entry_button.pack(pady=3)

        delete_button = Button(self.window, text="Delete selected task", width=50, command=self.delete_task)
        delete_button.pack(pady=3)

        mark_button = Button(self.window, text="Mark as completed ", width=50, command=self.mark_as_completed)
        mark_button.pack(pady=3)

        update_button = Button(self.window, text="Update task", width=50, command=self.update_task)
        update_button.pack(pady=3)

        refresh_button = Button(self.window, text="Refresh", width=50, command=self.Refresh_list)
        refresh_button.pack(pady=3)

        self.window.mainloop()

    def update_task_list(self):
        self.tasks = todoRepository.get_tasks()
        self.listbox_task.delete(0, END)
        for task in self.tasks:
            content = ""
            if task["is_mark_as_completed"]:
                content = "✔"
            self.listbox_task.insert(END, task["content"] + content)

    def add_task(self):
        self.add_task_window = AddTodo(self.update_task_list)

    def update_task(self):
        selected = self.listbox_task.curselection()
        selected_task = self.tasks[selected[0]]
        self.add_task_window = UpdateTodo(selected_task["id"], )

    def delete_task(self):
        selected = self.listbox_task.curselection()
        selected_task = self.tasks[selected[0]]
        todoRepository.remove_todo(selected_task["id"])
        self.listbox_task.delete(selected[0])
        return

    def mark_as_completed(self):
        selected = self.listbox_task.curselection()
        selected_task = self.tasks[selected[0]]
        todoRepository.mark_as_completed(selected_task["id"], )
        self.listbox_task.insert(selected[0])
        self.update_task_list()
        return

    def Refresh_list(self):
        self.update_task_list()
        return
