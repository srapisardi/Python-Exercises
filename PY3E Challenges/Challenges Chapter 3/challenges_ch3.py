# Chapter 3, Challenge 1
# Fortune Cookies Generator
# Write a program that simulates a fortune cookie.
# The program should display one of five unique fortunes, at random, each time it's run.
import random
import time


while True:
    fortune = random.randint(1,5)
    open = input("Press Enter to Open Fortune Cookie. Type 'q' to quit.")
    if open == 'q':
        break
    if fortune == 1:
        print("Confucius say: He who goes to bed with itchy butt, wakes up with a smelly finger.\n\n")
        time.sleep(5)
    elif fortune == 2:
        print("Don't concentrate on the finger or you will miss all of the heavenly glory.\n\n")
        time.sleep(5)
    elif fortune == 3:
        print("You miss 100% of the shots you don't take.\n\n")
        time.sleep(5)
    elif fortune == 4:
        print("Fool me once. Shame on...shame on you...if you fool me you can't get fooled again!\n\n")
        time.sleep(5)
    elif fortune == 5:
        print("I won the election. By a lot!\n\n")
        time.sleep(5)




# Chapter 3, Challenge 2
# Flip A Coin program
# Write a program that flips a coin 100 times and then tells you the number of heads and tails.
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


# Chapter 3, Challenge 3
# Guess My Number with fixed number of tries
# Modify the Guess My Number game so that the player has a limited number of guesses.
# If the player fails to guess in time, the program should display an appropriately chastising message.
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


# Computer guesses number game
# Write the pseudocode for a program where the player and the computer trade places in the number guessing game.
# That is, the player picks a random number between 1 and 100 that the computer has to guess.
# Before you start, think about how you guess.
# If all goes well, try coding the game.



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
