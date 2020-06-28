#   COS-205_assignment2b_MC.py
#   This program will find the sum of the first n natural numbers
#   with user input for the value of n.
#   by: Mike Crowley

# Defining main function of program.
def main():

# Printing sentence written below.
    print("This program is intended to find the sum of the natural numbers up to your specified value.")

# Printing blank line for readability while executing code.
    print()

# Asking user to input an integer and then assigning their value to the variable top_number
# which will be used to create the maximum value of our list below.
    top_number = int(input("Please provide a positive integer (counting number): "))

# Creating a list from 0 (by default) up to and including top_number provided earlier.
# Lists with range function will show all values from the lowest up to but not including the input
# so we included + 1 to our value to ensure top_number was included in our calculation below.
    list = range(top_number + 1)

# Printing the statement below and inserting the value provided by the user as well as the sum of all natural numbers
# ranging from 0 through the number provided.
    print("The sum of all natural numbers from 0 to", top_number, "is", sum(list))

# Executing main function defined above.
main()