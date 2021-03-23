ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print("Wait there are not 10 things in the list. Let's fix that.")

stuff = ten_things.split()

more_stuff = ["Day", "Corn", "Night", "Song", "Frisbee", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print("There are",len(stuff),"items in the list.")

print("There we go", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-3])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff))
