from sys import argv

script, user_name = argv
prompt = 'Enter answer here: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to asked ytou a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print("Where do you live?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice!
""")
