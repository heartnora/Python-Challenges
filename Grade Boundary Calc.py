# Grade Boundry Calc


# Defining the Grade boundries via if statements
def get_grade(mark):
    if 0 <= mark <= 39:
        return "Awarded Grade U"
    
    elif 40 <= mark <= 49:
        return "Awarded Grade E"
    
    elif 50 <= mark <= 59:
        return "Awarded Grade D"
    
    elif 60 <= mark <= 69:
        return "Awarded Grade C"
    
    elif 70 <= mark <= 79:
        return "Awarded Grade B"
    
    elif 80 <= mark <= 100:
        return "Awarded Grade A"
    
    else:
        return "You have to enter a number between 0 and 100"


# Creating a while loop to be able to contstantly
# put in grades without constantly running the program

while True:
    user_input = input("Enter the exam mark (or press Enter to exit): ")
    print("-"*30)
    if user_input == "":
        break
    try:
        mark = int(user_input)
        result = get_grade(mark)
    except ValueError:
        result = "You have to enter a number between 0 and 100"
    print(result)
