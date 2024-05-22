
def save_quiz_result(name, score):
    """Save user's name and quiz result in a text file."""
    with open("quiz_results.txt", "a") as file:
        file.write(f"Name: {name}, Score: {score}\n")

def maths_quiz():
    """Maths quiz with three questions."""
    name = input("Enter your name: ")
    score = 0
    



    # Question 1
    answer1 = int(input("Find X. 2x + 5 = 17 : "))
    if answer1 == 6:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 2
    answer2 = int(input("12 + 8 × 2  : "))
    if answer2 == 28:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 3
    answer3 = int(input("3y − 7 = 20 : "))
    if answer3 == 9:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print(f"Hi {name}, your score is {score}/3.")
    save_quiz_result(name, score)

maths_quiz()
