#Challenge 3 Modify the new version of Guess MY Number you create in the last challenge
#so that hte program's code is in a function called main()


import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")


def ask_number(question, random):
    """Ask for a number within a range."""
    response = None
    while response not in range(random):
        response = int(input(question))
    return response

def main():
    global guess, tries, the_number
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = int(input("Take a guess: "))
        tries -= 1
        if tries == 0:
            break

    if tries == 0:
        print("No more tries")
    else:
        print("You guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!\n")

# set the initial values
the_number = random.randint(1, 100)
guess = ask_number("Guess a number between 1-100: ",the_number)
tries = 4

# guessing loop
main()

input("\n\nPress the enter key to exit.")
