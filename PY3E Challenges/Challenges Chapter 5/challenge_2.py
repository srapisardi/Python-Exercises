# Write a CharacterCreate Program for a role-playing game.
# The player should be given a pool of 30 points to spend on four attributes:
# Strength, Health, Wisdom, and Dexterity
# The player should be able to spend points from the pool on any attribute
# and should also be able to take points from an attribute and put them back
# in the pool.



attributes = {
"1. strength": 0,
"2. wisdom": 0,
"3. dexterity": 0,
"4. health": 0,
"5. quit": "Press 5 to exit this menu."
}

points = 30

while True:
    for key, value in attributes.items():
        print(key,value)
    print("You have",points,"points available.")
    stat = input("\nChoose an option: ")
    if points == 0:
        print("No points left to spend")
        continue
    if stat == "1":
        add_subtract_str = input("Press 1 to Add points. Press 2 to Subtract points")
        if add_subtract_str == "1":
            add_str = int(input("Enter a number to add: "))
            points -= add_str
            attributes["1. strength"] += add_str
            print("Strength: ",attributes["1. strength"],"Points left:",points)
        if add_subtract_str == "2":
            sub_str = int(input("Enter a number to subtract: "))
            if attributes["1. strength"] == 0:
                print("No points to subtract")
            else:
                points += add_str
                attributes["1. strength"] -= add_str
                print("Strength: ",attributes["1. strength"],"Points left:",points)


    if stat == "2":
        add_subtract_wis = input("Press 1 to Add points. Press 2 to Subtract points")
        if add_subtract_wis == "1":
            add_wis = int(input("Enter a number to add: "))
            points -= add_wis
            attributes["2. wisdom"] += add_wis
            print("Wisdom: ",attributes["2. wisdom"],"Points left:",points)
        if add_subtract_wis == "2":
            sub_wis = int(input("Enter a number to subtract: "))
            if attributes["2. wisdom"] == 0:
                print("No points to subtract")
            else:
                points += add_wis
                attributes["2. wisdom"] -= add_wis
                print("Wisdom: ",attributes["2. wisdom"],"Points left:",points)


    if stat == "3":
        add_subtract_dex = input("Press 1 to Add points. Press 2 to Subtract points")
        if add_subtract_dex == "1":
            add_dex = int(input("Enter a number to add: "))
            points -= add_dex
            attributes["3. dexterity"] += add_dex
            print("Dexterity: ",attributes["3. dexterity"],"Points left:",points)
        if add_subtract_dex == "2":
            sub_dex = int(input("Enter a number to subtract: "))
            if attributes["3. dexterity"] == 0:
                print("No points to subtract")
            else:
                points += add_dex
                attributes["3. dexterity"] -= add_dex
                print("Dexterity: ",attributes["3. dexterity"],"Points left:",points)


    if stat == "4":
        add_subtract_hel = input("Press 1 to Add points. Press 2 to Subtract points")
        if add_subtract_hel == "1":
            add_hel = int(input("Enter a number to add: "))
            points -= add_hel
            attributes["4. health"] += add_hel
            print("Health: ",attributes["4. health"],"Points left:",points)
        if add_subtract_hel == "2":
            sub_hel = int(input("Enter a number to subtract: "))
            if attributes["4. health"] == 0:
                print("No points to subtract")
            else:
                points += add_hel
                attributes["4. health"] -= add_hel
                print("Health: ",attributes["4. health"],"Points left:",points)


    if stat ==  "5":
        break
