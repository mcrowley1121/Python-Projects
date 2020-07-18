#   This program calculates and prints out the numeric value of a single name, provided as input by the user.
#   by: Mike Crowley

#   Defining main function of the program.
def main():
    # Explaining program with print function, while utiizing '\n' to create line breaks for readability.
    print("Numerologists claim to be able to determine a person’s\n"
          "character traits based on the “numeric value” of their name.\n"
          "By providing your name, we will calculate your name's numeric value.\n")

    # Taking input from user and storing it in variable 'name'.
    name = input("Please enter your first name: ")

    # Converting string to all lowercase letters for consistency across inputs.
    lowercase_name = name.lower()

    # Creating an empty list to store the results of the following for loop.
    numeric_value_list = []

    # Creating a for loop to convert the characters of string 'lowercase_name'
    # into a list of integers to be used for the calculation.
    for characters in lowercase_name:

        # Utilizing '.append' to append the values produced by the loop to our original list so that they
        # may be accessed outside of the for loop.

        # By translating the lowercase letters into their ASCII values
        # we can subtract 96 to allow their new values to match the character's place in
        # the English alphabet.
        numeric_value_list.append(ord(characters) - 96)

    # Adding the contents of the list together to get the total numeric value of the user's provided name.
    numeric_value = sum(numeric_value_list)

    # Printing the statement below showing the total numeric value for the user's name.
    # Utilizing string formatting {} to display user's name and
    # allow the entry of the numeric value and closing '.' to not have a space between them when printed.
    print("{}, the numeric value of your name is {}.".format(name, numeric_value))

# Executing main function of the program.
main()
