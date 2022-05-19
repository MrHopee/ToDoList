import tkinter
from tkinter import Tk, Text, Button

from repository.index import todoRepository


class AddTodo:
    def __init__(self, on_add):
        self.on_add = on_add
        self.window = Tk()
        self.window.title("Add task")

        self.entry_task = Text(self.window, width=40, height=4)
        self.entry_task.pack()

        self.add_button = Button(self.window, text="Add task", command=self.add)
        self.add_button.pack()

        self.cancel_button = Button(self.window, text="Cancel", command=self.close)
        self.cancel_button.pack()

        self.window.mainloop()

    def close(self):
        self.window.destroy()

    def __del__(self):
        self.close()

    def add(self):
        todo_input = self.entry_task.get(1.0, "end-1c")
        if todo_input == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            todoRepository.add_todo(todo_input)
            self.on_add()
            self.close()
