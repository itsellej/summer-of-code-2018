# #1. There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)
#
# for i in range(65,123):
#     if chr(i).isalpha():
#         print(i, " stands for ", chr(i))
#
# #2. Make a function that prints A-Z and a-z

# def alpha():
#     for i in range(65,123):
#         if chr(i).isalpha():
#             print(i, " stands for ", chr(i))
#
# #test
# alpha()

#3. Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher )

def cypher(message):
    letters = list(message)
    print(letters)

    decoded = []
    for i in letters:
    #     if i == " ":
    #         decoded.append(" ")
    # else:
        decoded.append(ord(i))


    print(decoded)

#test
cypher("I LOVE YOU")

#4. Optional - caeser cypher
