from sys import exit

def gold_room():
    print("The room is full of gold. How much do you take?")

    choice = int(input("> "))

    if choice < 50:
        print("Nice, you're not greedy, you win!")
    elif choice > 50:
        dead("You're greedy!")
    else:
        dead("Man, learn to type a number")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
            break
        else:
            print("I got no idea what that means.")

def chtulhu_room():
    print("Here you see the great evil Chtulhu.")
    print("He, it, whatever stares at you and you go insane")
    choice = input("Do you flee for your life or eat your head? ")

    if choice == "flee":
        start()
    elif choice == "head":
        dead("Well that was tasty!")
    else:
        chtulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    choice = input("Which one do you take? ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        chtulhu_room()
    else:
        dead("Yo stumble around the room until you starve.")

start()
