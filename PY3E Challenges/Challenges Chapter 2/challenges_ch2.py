#Challenge #1 Good and Bad Variable names
# - Good: x,y,name,new_item
# - Bad: _person, PeOePL3, 242kfkf




# Chapter 2, Challenge 2
# Write a program that allows a user to enter his or her two favourite foods.
# The program should then print out the name of a new food by joining the original food names together.
print("Challenge #2")
food_one = input("What is your favorite food?")
food_two = input("What is your second favorite food?")

foods = print("Your two favorite foods are",food_one,"and",food_two)



# Chapter 2, Challenge 3
# Write a Tipper program where the user enters a restaurant bill total.
# The program should then display two amounts: a 15 percent tip and a 20 percent tip.
print("Challenge #3")
total = int(input("Enter bill amount: "))

tip_one = total *.15
tip_two = total * .20

print("15% is equal to",tip_one)
print("20% is equal to",tip_two)





# Chapter 2, Challenge 4
# Write a Car Salesman program where the user enters the base price of a car.
# The program should add on a bunch of extra fees such as tax, license, dealer prep, and destination charge.
# Make tax and license a percent of the base price.
# The other fees should be set values.
# Display the actual price of the car once all the extras are applied.
print("Challenge #4")
car_price = int(input("Enter price of the car: "))

tax = float(car_price * .07)

license = float(car_price * .10)

dealer_prep = int(100)
destination_charge = int(200)

total = car_price + tax + license + dealer_prep + destination_charge

print("The total price of the car is",total)
