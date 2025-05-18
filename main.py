import os
import sys

from stats import get_num_words, get_num_characters, print_sorted_characters

def get_book_text(filepath):    # use a string of a filepath/filename

    print(f"Analyzing book found at {filepath}")

    with open(filepath) as f:   # open the file as object "f"
        return f.read()         # read the text as a return "string"

def main():

    # First we're going to clear the terminal at program startup'
#    os.system("clear")

    print("=================================")
    print("=                               =")
    print("=           BOOKBOT             =")
    print("=                               =")
    print("=================================\n")

    try:
        # read the file's text into a string
        read = get_book_text(sys.argv[1])
    except:
        print("This application requires you to include a filepath to a book (in a txt file)")
        print("Unfortunately your entry did not work.")
        print("Below is the syntax, followed by an example:")
        print("")
        print("Usage: python3 main.py <path_to_book>")
        print("")
        print("Example: python3 main.py books/frankenstein.txt")
        print("")
        print("Please try again, and thank you for using Bookbot!\n\n")
        sys.exit(1)

    # count the number of words in the string
    counted = get_num_words(read)

    print(f"Found {counted} total words")

    # count the number of letters in the words
    characters_dict = get_num_characters(read)

    print_sorted_characters(characters_dict)

    print("============= END ===============")


if __name__ == "__main__":
	main()
