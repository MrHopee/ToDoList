import tkinter
from tkinter import Tk, Text, Button

from repository.index import todoRepository


class UpdateTodo:
    def __init__(self, id, ):
        self.id = id
        self.window = Tk()
        self.window.title("Update task")

        self.entry_task = Text(self.window, width=40, height=4)
        self.entry_task.pack()

        self.update_button = Button(self.window, text="Update task", command=self.update)
        self.update_button.pack()

        self.cancel_button = Button(self.window, text="Cancel", command=self.close)
        self.cancel_button.pack()

        self.window.mainloop()

    def close(self):
        self.window.destroy()

    def __del__(self):
        self.close()

    def update(self, ):
        todo_input = self.entry_task.get(1.0, "end-1c")
        if todo_input == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            todoRepository.edit_todo(self.id, todo_input, )
            self.close()
