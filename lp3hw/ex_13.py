from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

item_one = input("Give person one an item.")
item_two = input("Give person two an item.")
item_three = input("Give person three an item.")
print(first,"is holding:", item_one)
print(second,"is holding:", item_two)
print(third, "is holding:", item_three)
