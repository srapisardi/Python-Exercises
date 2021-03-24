states = {
"Oregon": "OR",
"New York": "NY",
"New Jersey": "NJ",
"California": "CA",
"Massachusetts": "MA"
}

cities = {
"OR": "Portland",
"NY": "Brooklyn",
"NJ": "New Brunswick",
"CA": "San Diego"
}

#Add some more cities
cities["TX"] = "Dallas"
cities["MA"] = "Boston"

#Print cities
print("=" * 10)
print("NY State has: ", cities["NY"])
print("TX State has: ", cities["TX"])

#Print abbreviations

print("New Jersey Abbreviaion is", states["New Jersey"])
print("California Abbreviation is", states["California"])

print("New Jersey has:", cities[states["New Jersey"]])
print("Massachusetts has", cities[states["Massachusetts"]])

print("=" * 10)
#Print every state abbreviations
for state, abbrev in list(states.items()):
    print(state, abbrev)

print("=" * 10)
#Print every city
for state, city in list(cities.items()):
    print(state, city)

print("=" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has a city {cities[abbrev]}")

print("=" * 10)

state = states.get("Maryland")

if not state:
    print("Sorry no Maryland")

print("=" * 10)
city = cities.get("MD", 'Does Not Exist')
print("The city for the state 'MD' is", {city})
