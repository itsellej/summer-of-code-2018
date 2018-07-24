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

# #3. Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher )
#
# def cypher(message):
#     letters = list(message)
#
#     decoded = []
#     for i in letters:
#         decoded.append(ord(i))
#
#     for n, i in enumerate(decoded):
#         if i == 32:
#             decoded[n] = " "
#
#     print(decoded)
#
# #test
# cypher("I LOVE YOU")
# cypher("A B C D E")
# cypher("Elle J")


#4. Print out all elements of the board using a function

M = "M"
o = "o"
world = [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]

def print_board(board):
    for i in board:
        for x in i:
            print(x, end=" ")

print_board(world)
