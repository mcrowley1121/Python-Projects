#   COS-205_assignment2a_MC.py
#   This program will calculate the area of a
#   triangle given the length of its three sides a, b, and c based on user input.
#   by: Mike Crowley

# Importing square root function from math set built into Python language.
import math

# Defining main function of program.
def main():

# Printing sentence written below.
    print("This program is intended to calculate the area of a triangle using numeric values provided by you.")

# Printing blank line for readability while executing code.
    print()

# Requesting input from user on the length of each side of their triangle and assigning it to their
# respective variables after turning it into a float value.
    side_a = float(input("Please input the length of side A: "))
    side_b = float(input("Please input the length of side B: "))
    side_c = float(input("Please input the length of side C: "))

# Utilizing the formula provided by the assignment to find value for "s"
    s = (side_a + side_b + side_c) / 2

# Utilizing the formula provided by the assignment, as well as the square root function
# imported from math to assign the total area of the triangle to a variable named area.
    area = math.sqrt((s * (s - side_a) * (s - side_b) * (s - side_c)))

# Printing the statement below to display the string and area value.
    print("The area of your triangle is", area)

# Executing the function defined above.
main()


