# Write a Who's Your Daddy? program that lets the user enter the name of a male
# and produces the name of his father. Allow the user to add, replace, and
# delete son-father pairs.


father_son = {
"John Lennon": "Julian Lennon",
"Ken Griffey Sr.": "Ken Griffey Jr.",
"Bruce Matthews": "Clay Matthews",
"Jerry Stiller": "Ben Stiller",
"Martin Sheen": "Charlie Sheen",
}



print("""

    \t Who Is Your Daddy? Program
    \t 1. Add a Father/Son Pair
    \t 2. Replace a Father/Son Pair
    \t 3. Delete a Father/Son Pair
    \t 4. Show all Father/Son Pairs
    \t 5. Quit


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
        replace_father = input("Who's son do you want to replace? ")
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
        break


input("Press Enter to exit.")
