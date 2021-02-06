import pickle


try:
    file = open("py_trivia.txt","r")
except:
    print("File does not exist in this directory.")
    input("Press Enter to exit.")

def question():
    question_number = file.readline()
    question = file.readline()
    print(question_number)
    print(question)

def choices():
    for i in range(4):
        print(file.readline())

def answer():
    global score
    answer = input("Enter answer here: ")
    correct_answer = file.readline()
    correct_answer = correct_answer.rstrip()
    if answer == correct_answer:
        print("Correct!")
        points = int(file.readline())
        score += points
    else:
        print("Incorrect!")
        no_points = file.readline()

def main():
    for i in range(3):
        question()
        choices()
        answer()

score = 0

main()
print("Game Over! Final score: ",score)


name_score = {}
name = input("Enter your name to go onto the leaderboard: ")
name_score[name] = score
leaderboard = open("leaderboard.dat", "wb")
pickle.dump(name_score, leaderboard)



input("Press Enter to quit.")
