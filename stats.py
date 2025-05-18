def get_num_words(book):

    print("----------- Word Count ----------")

    return len(book.split())

def get_num_characters(book):

    # First lets make everything in the book lowercase using "lower()"
    book_lowercase = book.lower()

    # Next, lets separate all the individual characters of the book using "list(book_name_here)"
    characters_list = list(book_lowercase)

    # Intialize the Dictionary
    characters_dict = {}

    # Format and feed the Dictionary
    # ie:   'p' : #_of_p
    #       'r' : #_of_r
    #       'o' : #_of_o
    for character in characters_list:
        if character.isalpha() != True:
            continue

        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1

    return characters_dict

def print_sorted_characters(unsorted_dict):

    print("--------- Character Count -------")

    sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))

    for i in sorted_dict:
        print(f"{i}: {sorted_dict[i]}")

    return
