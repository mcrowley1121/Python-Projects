#   This program prompts a user for a text file name and counts the number of words in the text file.
#   The program will be considering anything that is separated by white space or new line on either
#   side of a contiguous group of characters or character as a word.
#   by: Mike Crowley

#   Defining main function of the program.
def main():

    # Explaining program with print function, while utiizing '\n' to create line breaks for readability.
    print("This program will count the number of words within your text file,\n"
          "provided that you write out the file's full title (including extension: '.txt') \n"
          "and the file is located in the same folder as this program.\n")

    # Prompting user to provide the file name for the word counting program.
    filename = input("Please enter the filename: ")

    # Opening the file in a read only format.
    infile = open(filename, "r")

    # Assigning the data that was read from the opened file to the variable 'data',
    # essentially creating and storing a long string.
    data = infile.read()

    # Using len function to count the total words in the string
    # by splitting the string into substrings and adding them to a list 'word_count'.
    word_count = len(data.split())

    # Printing the statement below detailing the total word count of user's the file.
    # Utilizing string formatting {} to allow the word count and closing '.'
    # to not have a space between them when printed.
    print("The total word count for your file is {} words.".format(word_count))

# Executing main function of the program.
main()

