def calculate_average_speed(distance, time):
    return distance / time

distance = input("Enter the distance in meters: ")
time = input("Enter the time in seconds: ")

try:
    distance = float(distance)
    time = float(time)

    if time == 0:
        print("Error: Time cannot be zero.")
    else:
        average_speed = calculate_average_speed(distance, time)
        print(f"The average speed is {average_speed} meters per second.")

except ValueError:
    print("Error: Please enter valid numeric values for distance and time.")
