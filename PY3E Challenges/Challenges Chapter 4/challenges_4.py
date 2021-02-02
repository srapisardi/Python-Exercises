#Challenge 1
starting_num = int(input("Enter a starting number: "))
ending_num = int(input("Enter a ending number: "))
count_by = int(input("What would you like to count by?: "))

for numbers in range(starting_num,ending_num,count_by):
    print(numbers)



#Challenge 2
message = input("Enter a message: ")

index = int(len(message)) - 1

backwards = ""

for new_message in message:
    backwards += message[index]
    index = index - 1

print(backwards)

#Challenge #3
# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
hint = word[0:3]
# create a variable to use later to see if the guess is correct
correct = word
number_of_guesses = 0
score = 0

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!

   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)


while True:
    guess = input("\nType in your guess. Type 'hint' if you're stuck. ").lower().strip()
    if guess == "hint":
        print(hint)
        continue
    if guess != correct:
        print("Sorry, that's not it.")
        number_of_guesses += 1
        continue
    if guess == correct:
        print("That's it!  You guessed it!\n")
        number_of_guesses += 1
        break

print("Thanks for playing.")
if number_of_guesses == 1:
    score += 5
    print("You guessed the word in",number_of_guesses,"try." "Your score is",score)
if number_of_guesses > 1:
    score += 1
    print("You guessed the word in",number_of_guesses,"tries.","Your score is",score)

input("\n\nPress the enter key to exit.")


#Challenge 4


words = ("apple","monkey","excellent","lightning","building")
random_word = random.choice(words)
word = ""
chosen_word = random_word + word

length = len(chosen_word)


hints = 5

print("The word has",length,"letters. Try to guess the word or ask if the letter is in the word.")
while hints > 0:
    letter = input("Ask if the letter is in the word: ")
    if letter in chosen_word:
        print("Yes.")
    else:
        print("No.")
    hints -= 1



guess = input("Try to guess the word: ").lower().strip()
if guess == chosen_word:
    print("Correct!")
else:
    print("Incorrect! The word is",chosen_word)


input("Press Enter to Exit.")
