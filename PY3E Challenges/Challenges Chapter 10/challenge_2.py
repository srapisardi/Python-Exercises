#Challenge 2 Write a version of the Guess My Number game using a GUI

from tkinter import *
import random

class Application(Frame):
    def __init__ (self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.random_number = random.randint(1,5)

    def create_widgets(self):
        Label(self,
              text="Enter a number to guess between 1-20").grid(row=0, column=0, sticky=W)

        self.number = Entry(self)
        self.number.grid(row=1, column=0, sticky=W)

        Button(self,
               text="Guess",
               command= self.guess_number).grid(row=2, column=0, sticky=W)

        self.message = Text(self, width=20, height=5, wrap = WORD)
        self.message.grid(row=3, column=0, sticky=W)

    def guess_number(self):
        number = int(self.number.get())
        if number == self.random_number:
            self.message.delete(0.0, END)
            self.message.insert(0.0, "That is the correct number!")
        else:
            self.message.delete(0.0, END)
            self.message.insert(0.0, "Incorrect! Guess Again")








root = Tk()
root.title("Guess The Number")
app = Application(root)
root.mainloop()
