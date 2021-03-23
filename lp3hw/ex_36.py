import random

inventory = []

def bug_area():
    bugs = ("Ant", "Spider", "Ladybug")
    random_bug = random.choice(bugs)
    print("You've found a", random_bug)

    choice = input("Do you want to keep it?")

    if choice == "yes":
        print(random_bug,"placed in your bag.")
        inventory.append(random_bug)
    elif choice == "no":
        print("You put the", random_bug,"down.")
    else:
        print("Not sure what you want to do")

def forest():
    choice = input("You're entered the forest. Chop down trees?")
    if choice == "yes":
        print("You've chopped down some trees and collected wood.")
        inventory.append("Wood")
    elif choice == "no":
        print("You do not chop down any trees.")
    else:
        print("Not sure what you want to do.")

def lake():
    choice = input("You found a lake. Do you want to fish? ")
    if choice == "yes":
        random_number = random.randint(0,3)
        if random_number == 1:
            fish = ("Koi", "Goldfish", "Catfish")
            random_fish = random.choice(fish)
            print("You've caught a", random_fish)
            inventory.append(random_fish)
        else:
            print("Nothing is biting today.")
    elif choice == "no":
        print("You do not feel like fishing today.")
    else:
        print("Not sure what you want to do.")

def main():
    print("Welcome to Animal Crossing!")

    while True:
        print("""
              Choose where you want to go:
              1. Hunt for Bugs
              2. Go Fishing
              3. Go to the Forest
              4. Show inventory
              5. Quit
              """)

        choice = input("Where would you like to go? ")

        if choice == "1":
            bug_area()
        elif choice == "2":
            lake()
        elif choice == "3":
            forest()
        elif choice == "4":
            for list in inventory:
                print(list)
        elif choice == "5":
            print("Thanks for playing!")
            break



main()
