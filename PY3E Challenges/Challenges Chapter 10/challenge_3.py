# Challenge 3 Create a GUI program, Order Up!, that presents the user with a simple restaurant menu,
# which lists items and prices. Let the user select different items and then show the user the total bill.

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self,
              text="Hamburger:  $2.50").grid(row=2, column=0, sticky=W)
        self.hamburger_entry = Entry(self)
        self.hamburger_entry.insert(0, "0")
        self.hamburger_entry.grid(row=2, column=1, sticky=W)
        Label(self,
              text="Cheeseburger:  $3.50").grid(row=3, column=0, sticky=W)
        self.cheeseburger_entry = Entry(self)
        self.cheeseburger_entry.insert(0, "0")
        self.cheeseburger_entry.grid(row=3, column=1, sticky=W)
        Label(self,
              text="Bacon Cheeseburger:  $5.00").grid(row=4, column=0, sticky=W)
        self.bacon_cheeseburger_entry = Entry(self)
        self.bacon_cheeseburger_entry.insert(0, "0")
        self.bacon_cheeseburger_entry.grid(row=4, column=1, sticky=W)
        Label(self,
              text="Turkey Burger:  $4.00").grid(row=5, column=0, sticky=W)
        self.turkey_burger_entry = Entry(self)
        self.turkey_burger_entry.insert(0, "0")
        self.turkey_burger_entry.grid(row=5, column=1, sticky=W)


        Label(self,
              text="Doneness").grid(row=7, column=0, sticky=W)
        self.doneness = StringVar()
        self.doneness.set(None)
        Radiobutton(self,
                    text="Rare",variable=self.doneness, value="Rare").grid(row=7, column=1, sticky=W)
        Radiobutton(self,
                    text="Medium Rare",variable=self.doneness, value="Medium Rare").grid(row=7, column=2, sticky=W)
        Radiobutton(self,
                    text="Medium", variable=self.doneness, value="Medium").grid(row=7, column=3, sticky=W)
        Radiobutton(self,
                    text="Medium Well", variable=self.doneness, value="Medium Well").grid(row=7, column=4, sticky=W)
        Radiobutton(self,
                    text="Welldone", variable=self.doneness, value="Welldone").grid(row=7, column=5, sticky=W)


        Label(self,
              text="Toppings (+$.50)").grid(row=9, column=0, sticky=W)
        self.onions = BooleanVar()
        Checkbutton(self,
                    text="Onions", variable=self.onions).grid(row=9, column=1, sticky=W)
        self.peppers = BooleanVar()
        Checkbutton(self,
                    text="Peppers", variable=self.peppers).grid(row=9, column=2, sticky=W)
        self.mushrooms = BooleanVar()
        Checkbutton(self,
                    text="Mushrooms", variable=self.mushrooms).grid(row=9, column=3, sticky=W)
        self.lettuce = BooleanVar()
        Checkbutton(self,
                    text="Lettuce", variable=self.lettuce).grid(row=9, column=4, sticky=W)
        self.tomatoes = BooleanVar()
        Checkbutton(self,
                    text="Tomatoes", variable=self.tomatoes).grid(row=9, column=5, sticky=W)
        self.pickles = BooleanVar()
        Checkbutton(self,
                    text="Pickles", variable=self.pickles).grid(row=9, column=6, sticky=W)

        Label(self,
              text="Sides").grid(row=10, column=0, sticky=W)
        self.french_fries = BooleanVar()
        Checkbutton(self,
                    text="French Fries:  $2.00", variable=self.french_fries).grid(row=10, column=1, sticky=W)
        self.onion_rings = BooleanVar()
        Checkbutton(self,
                    text="Onion Rings:  $3.00", variable=self.onion_rings).grid(row=10, column=2, sticky=W)
        self.mozzerella_sticks = BooleanVar()
        Checkbutton(self,
                    text="Mozzerella Sticks:  $5.00", variable=self.mozzerella_sticks).grid(row=10, column=3, sticky=W)

        Label(self,
              text = "Desserts").grid(row=11, column=0, sticky=W)
        self.ice_cream = BooleanVar()
        Checkbutton(self,
                    text="Ice Cream:  $2.00", variable=self.ice_cream).grid(row=11, column=1, sticky=W)
        self.brownies = BooleanVar()
        Checkbutton(self,
                    text="Brownies:  $1.00", variable=self.brownies).grid(row=11, column=2, sticky=W)
        self.cookies = BooleanVar()
        Checkbutton(self,
                    text="Cookies:  $100", variable=self.cookies).grid(row=11, column=3, sticky=W)

        Label(self,
              text="$").grid(row=13, column=1, sticky=E)

        Label(self,
              text="Total"). grid(row=12, column=2)
        self.total = Text(self, width=10, height=2, wrap=WORD)
        self.total.grid(row=12, column=2)

        Button(self,
               text="Add to Order",
               command=self.order).grid(row=14, column=2)

    def order(self):
        total = 0.0
        hamburgers = int(self.hamburger_entry.get())
        cheeseburgers = int(self.cheeseburger_entry.get())
        bacon_cheeseburgers = int(self.bacon_cheeseburger_entry.get())
        turkey_burger = int(self.turkey_burger_entry.get())

        if self.hamburger_entry:
            total += 2.50 * hamburgers
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.cheeseburger_entry:
            total += 3.50 * cheeseburgers
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.bacon_cheeseburger_entry:
            total += 5.00 * bacon_cheeseburgers
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.turkey_burger_entry:
            total += 4.00 * turkey_burger
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.onions.get():
            total += .50
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.peppers.get():
            total += .50
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.mushrooms.get():
            total += .50
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.lettuce.get():
            total += .50
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.tomatoes.get():
            total += .50
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.pickles.get():
            total += .50
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.french_fries.get():
            total += 2.00
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.onion_rings.get():
            total += 3.00
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.mozzerella_sticks.get():
            total += 5.00
            self.total.delete(0.0, END)
            seld.total.insert(0.0, total)
        if self.ice_cream.get():
            total += 2.00
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.brownies.get():
            total += 1.00
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)
        if self.cookies.get():
            total += 1.00
            self.total.delete(0.0, END)
            self.total.insert(0.0, total)


root = Tk()
root.title("Order Up!")
app = Application(root)
root.mainloop()
