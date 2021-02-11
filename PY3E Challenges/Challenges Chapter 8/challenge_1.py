# Challenge 1 Improve the program by allowing the user to specify how much food he or she feeds the critter and how long he or she plays with the critter.
# Have these values affect how quickly the critter's hunger and boredom levels drop.


# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        print("Boredom: ",self.boredom)
        print("Hunger: ",self.hunger)
        self.__pass_time()

    def eat(self, food = 4):
        food = int(input("How many apples do you want to feed? Choose between 1-9: "))
        while food < 1 or food > 9:
            food = int(input("Invalid number. Choose between 1-9: "))
        self.food = food
        self.hunger -= food
        print("Brruppp.  Thank you.")
        if self.hunger < 0:
            self.hunger = 0
        print("Boredom: ",self.boredom)
        print("Hunger: ",self.hunger)
        self.__pass_time()

    def play(self, fun = 4):
        fun = int(input("How many hours do you want to play? Choose between 1-9: "))
        while fun < 1 or fun > 9:
            food = int(input("Invalid number. Choose between 1-9: "))
        self.fun = fun
        self.boredom -= fun
        print("Wheee!")
        if self.boredom < 0:
            self.boredom = 0
        print("Boredom: ",self.boredom)
        print("Hunger: ",self.hunger)
        self.__pass_time()


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
