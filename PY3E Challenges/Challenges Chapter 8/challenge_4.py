# Critter Caretaker
# A virtual pet to care for

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        crit_name = "Name: " + self.name
        crit_hunger = "Hunger:", self.hunger
        crit_boredom = "Boredom", self.boredom
        return crit_name
        return crit_boredom
        return crit_hunger

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
        print("I'm", self.name, "and I feel", self.mood, "now.")
        print("Boredom: ",self.boredom)
        print("Hunger: ",self.hunger)
        self.__pass_time()


    def eat(self, food = 4):
        print("Feeding",self.name)
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
        print("Playing with",self.name)
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
    crit_name_1 = input("What do you want to name your first critter?: ")
    crit_name_2 = input("What do you want to name your second critter?: ")
    crit_name_3 = input("What do you want to name your third critter?: ")
    crit_1 = Critter(crit_name_1, hunger = random.randint(0,3), boredom = random.randint(0,3))
    crit_2 = Critter(crit_name_2, hunger = random.randint(0,3), boredom = random.randint(0,3))
    crit_3 = Critter(crit_name_3, hunger = random.randint(0,3), boredom = random.randint(0,3))

    farm = [crit_1, crit_2, crit_3]

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        4 - Show Farm
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit_1.talk()
            crit_2.talk()
            crit_3.talk()

        # feed your critter
        elif choice == "2":
            crit_1.eat()
            crit_2.eat()
            crit_3.eat()

        # play with your critter
        elif choice == "3":
            crit_1.play()
            crit_2.play()
            crit_3.play()

        elif choice == "4":
            for crits in farm:
                print(crits)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
