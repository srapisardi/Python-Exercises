#imports module
from sys import argv

#requires argument before running program
script, filename = argv

#opens the file name
txt = open(filename)

#reads the file name
print(f"Here's your file {filename}:")
print(txt.read())

#uses imput to enter a file name
print("Type the file name again: ")
file_again = input("> ")

#opens and reads the file
txt_again = open(file_again)
print(txt_again.read())
