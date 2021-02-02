#Challenge #1 Good and Bad Variable names
# - Good: x,y,name,new_item
# - Bad: _person, PeOePL3, 242kfkf

print("Challenge #2")
food_one = input("What is your favorite food?")
#food_two = input("What is your second favorite food?")

foods = print("Your two favorite foods are",food_one,"and",food_two)


print("Challenge #3")
total = int(input("Enter bill amount: "))

tip_one = total *.15
tip_two = total * .20

print("15% is equal to",tip_one)
print("20% is equal to",tip_two)


print("Challenge #4")
car_price = int(input("Enter price of the car: "))

tax = float(car_price * .07)

license = float(car_price * .10)

dealer_prep = int(100)
destination_charge = int(200)

total = car_price + tax + license + dealer_prep + destination_charge

print("The total price of the car is",total)
