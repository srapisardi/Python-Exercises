# Improve the Who's Your Daddy? program by adding a choice that lets the user
# enter a name and get back a grandfather. Your program should still only use
# one dictionary of son-father pairs. Make sure to include several
# generations in your dictionary so that a match can be found.




father_son = {
"John Lennon": "Julian Lennon",
"Ken Griffey Sr.": "Ken Griffey Jr.",
"Bruce Matthews": "Clay Matthews",
"Jerry Stiller": "Ben Stiller",
"Martin Sheen": "Charlie Sheen",
"John Lennon Sr.": "John Lennon",
"Joseph Griffey": "Ken Griffey Sr.",
"Michael Matthews": "Bruce Matthews",
"Ben Stiller Sr.": "Jerry Stiller",
"Vincent Sheen": "Martin Sheen",
}


print("""

    \t Who Is Your Daddy? Program
    \t 1. Add a Father/Son Pair
    \t 2. Replace a Father/Son Pair
    \t 3. Delete a Father/Son Pair
    \t 4. Show all Father/Son Pairs
    \t 5. Show Grandfather
    \t 6. Quit

    """)




while True:
    choice = input("Enter a number: ")
    if choice == "1":
        add_father = input("Enter a father name: ")
        if add_father not in father_son:
            add_son = input("Add the son's name: ")
            father_son[add_father] = add_son
            print(add_father,"and",add_son,"have been added.")
        else:
            print("Name already in database.")

    elif choice == "2":
        replace_father = input("Who's do you want to replace? ")
        if replace_father in father_son:
            new_son = input("Who is the new son?")
            father_son[replace_father] = new_son
            print(new_son,"is the new son of",replace_father)
        else:
            print("Name not found in database.")

    elif choice == "3":
        delete_father = input("Who do you want to remove? ")
        if delete_father in father_son:
            del father_son[delete_father]
            print(delete_father,"has been deleted.")
        else:
            print("Name not found.")

    elif choice == "4":
        for key, value in father_son.items():
            print(key,value)

    elif choice == "5":
        grandfather = input("What grandfather are you looking for? ")
        if grandfather not in father_son:
            print("Name not found.")
        else:
            grandchild = father_son[father_son[grandfather]]
            print(grandfather,"is the father of",father_son[grandfather],"and the grandfather of",grandchild)

    elif choice == "6":
        break


input("Press Enter to exit.")
