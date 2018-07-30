
def count_letters(filename):

    #open file and read file
    file = open(filename, "r")
    read_book = file.read()

    from collections import Counter

    #Create dictionary using letter as key and quantity as value pair
    characters = Counter(read_book)

    #sort the dictionary by key
    # if the key is alphabetic, add key : value pair to chars dictionary
    chars = {}

    for key, value in characters.items():
        if key.isalpha():
            # print(key, value)
            chars.update({key : value})


    # add value of same letter lower and upper case keys to create total as lower case key
    chars_condensed =  {k.lower(): v for k, v in chars.items()}

    #sort alphabetically by key and print key value pairs
    for key, value in sorted(chars_condensed.items()):
        print(f"{key}: {value}")

    file.close()

count_letters("01-alice_in_wonderland.txt")
