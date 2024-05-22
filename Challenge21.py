def centi(cm):
    return cm / 2.54

def inches(inches):
    return inches * 2.54


print("Welcome to the conversion program!")
value = float(input("Please enter the value you want to convert: "))
print("Choose the conversion type:")
print("1: Centimeters to Inches")
print("2: Inches to Centimeters")
    
choice = input("Enter your choice (1 or 2): ")
    
if choice == "1":
    result = inches(value)
    print(f"{value} cm is equal to {result:.2f} inches.")
elif choice == "2":
    result = centi(value)
    print(f"{value} inches is equal to {result:.2f} cm.")
else:
    print("Invalid choice. Please select either 1 or 2.")

