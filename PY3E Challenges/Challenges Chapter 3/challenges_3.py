#Challenge #1
import random
import time


while True:
    fortune = random.randint(1,5)
    open = input("Press Enter to Open Fortune Cookie. Type 'q' to quit.")
    if open == 'q':
        break
    if fortune == 1:
        print("Confucius say: He who goes to bed with itchy ass, wakes up with a smelly finger.\n\n")
        time.sleep(5)
    elif fortune == 2:
        print("Don't concentrate on the finger or you will miss all of the heavenly glory.\n\n")
        time.sleep(5)
    elif fortune == 3:
        print("Stay home if you sick, come over if you thicc.\n\n")
        time.sleep(5)
    elif fortune == 4:
        print("Fool me once. Shame on...shame on you...if you fool me you can't get fooled again!\n\n")
        time.sleep(5)
    elif fortune == 5:
        print("I won the election. By a lot!\n\n")
        time.sleep(5)



#Challenge #2
heads = 0
tails = 0
flips = 100

while flips > 0:
    coin = random.randint(1,2)
    flip = input("Press Enter to flip coin.")
    if coin == 1:
        print("Heads")
        heads = heads + 1
        flips = flips - 1
        print("Heads:",heads,"Tails",tails)
    elif coin == 2:
        print("Tails")
        tails = tails + 1
        flips = flips - 1
        print("Heads:",heads,"Tails",tails)

#Challenge #3

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 4

# guessing loop
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

input("\n\nPress the enter key to exit.")



#Challenge #4

#User will think of a random number
#User inputs the random number into the program
#Set a variable where computer generates a random number
#If the computer picks a random number correctly
#    User responds yes and the program ends
#If the computer pciks a random number incorrectly
#   User responds no and the program continues



while True:
    my_number = int(input("Pick a number between 1-10."))
    if my_number > 10:
        print("Number not in range.")
        continue
    elif my_number < 1:
        print("Number not in range.")
        continue
    else:
        break


while True:
    cpu_number = random.randint(1,10)
    print("My guess is",cpu_number)
    cpu_guess = input("Is this correct?")
    if cpu_guess == "yes":
        break
    else:
        continue

correct = input("I guessed your number! Press enter to exit.")
