# Create a program that prints a list of words in a random order.
# The program should print all the words and not repeat any.


import random

words = ["Apple","Orange","Banana","Peach","Strawberry"]
length = int(len(words))
count = 0
empty_list = []

while count < length:
    random_word = random.choice(words)
    if random_word not in empty_list:
        empty_list.append(random_word)
        count += 1

for list in empty_list:
    print(list)
