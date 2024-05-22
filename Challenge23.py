import math

def calculate_turf_needed(length, width, radius):
    lawn_area = length * width
    circle_area = math.pi * (radius ** 2)
    turf_needed = lawn_area - circle_area

    return turf_needed
 
length = float(input("Enter the length of the lawn (in meters): "))
width = float(input("Enter the width of the lawn (in meters): "))   
radius = float(input("Enter the radius of the circle (in meters): "))

turf_needed = calculate_turf_needed(length, width, radius)

print(f"The amount of turf needed is {turf_needed:.2f} square meters.")

