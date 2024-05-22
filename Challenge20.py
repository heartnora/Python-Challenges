guess=0

while guess != 7:
    guess = int(input("Enter your guess: "))
    if guess != 7:
        print("Incorrect... guess again")
        
print ("Well done!")