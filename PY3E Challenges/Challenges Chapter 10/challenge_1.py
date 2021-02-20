# Challenge 1 Write your own version of the Mad Lib program using a different arrangement of widgets

from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "My MadLib Program").grid(row=0, column=1, columnspan=2, sticky=N)

        Label(self,
              text = "Name").grid(row=1, column=0 ,sticky=W)
        self.name_entry = Entry(self)
        self.name_entry.grid(row=1, column=1, sticky=W)

        Label(self,
              text="Thing").grid(row=2, column=0, sticky=W)
        self.thing_entry = Entry(self)
        self.thing_entry.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Verb").grid(row=3, column=0, sticky=W)

        self.verb_entry = Entry(self)
        self.verb_entry.grid(row=3, column=1, stick=W)

        Label(self,
              text="Adjectives").grid(row=4, column=0, sticky=W)
        self.is_smelly = BooleanVar()
        Checkbutton(self,
                    text="Smelly",
                    variable = self.is_smelly).grid(row=4, column=1, sticky=W)

        self.is_funny = BooleanVar()
        Checkbutton(self,
                    text="Funny",
                    variable = self.is_funny).grid(row=5, column=1, sticky=W)

        self.is_angry = BooleanVar()
        Checkbutton(self,
                    text="Angry",
                    variable = self.is_angry).grid(row=6, column=1, sticky=W)


        Label(self,
              text="Cars").grid(row=7, column=0, sticky=W)
        self.choose_car = StringVar()
        self.choose_car.set(None)

        Radiobutton(self,
                    text="Sports Car",
                    variable = self.choose_car,
                    value = "Sports Car").grid(row=7, column=1, sticky=W)

        Radiobutton(self,
                    text="Pickup Truck",
                    variable = self.choose_car,
                    value = "Pickup Truck").grid(row=8, column=1, sticky=W)

        Radiobutton(self,
                    text="Clown Mobile",
                    variable = self.choose_car,
                    value= "Clown Movile").grid(row=9, column=1, sticky=W)

        Button(self,
               text="Create a Story!",
               command = self.create_story).grid(row=10, column=1, sticky=W)

        self.story = Text(self, width=50, height=35, wrap=WORD)
        self.story.grid(row=11, column=0, columnspan=3, rowspan=3, sticky=S)


    def create_story(self):
        name = self.name_entry.get()
        thing = self.thing_entry.get()
        verb = self.verb_entry.get()
        adjectives = ""
        if self.is_smelly.get():
            adjectives += "smelly "
        if self.is_funny.get():
            adjectives += "funny "
        if self.is_angry.get():
            adjectives += "angry "

        car = self.choose_car.get()

        story = "There was a famous athelete named "
        story += name
        story += " who's favorite thing about the sport he played was "
        story += thing
        story += ". One day when he was doing his daily "
        story += verb
        story += " until a strange man came to his house. The strange man had a "
        story += adjectives
        story += " vibe to him. It creeped "
        story += name
        story += " so he got in his "
        story += car
        story += " and drove to the nearby stadium so he can practice his "
        story += thing
        story += ". When he was practicing, he noticed he started feeling "
        story += adjectives
        story += ". The feeling came from the strange man. He finished "
        story += verb
        story += " got back into his"
        story += car
        story += " and drove away. That's when he realized this story makes no damn sense. The End"

        self.story.delete(0.0, END)
        self.story.insert(0.0, story)







root = Tk()
root.title("My MadLib Program")
root.geometry("500x500")
app = Application(root)
root.mainloop()
