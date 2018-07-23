#Separating upper and lower case

def count_letters(filename):

    #open file and read fuke
    file = open(filename, "r")
    read_book = file.read()

    from collections import Counter

    #Create dictionary using letter as key and quantity as value pair
    characters = Counter(read_book)

    #sort the dictionary by key
    # if the key is alphabetic, print key value pair
    for key, value in sorted(characters.items()):
        if key.isalpha():
            print(key, value)

    file.close()

    
count_letters("01-test2.txt")
count_letters("01-test.txt")


#Condensing total of all letters (upper and lower case)
