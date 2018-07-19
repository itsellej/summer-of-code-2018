# #WEEK 1 - DAY 4 - LOOPS AND CONDITIONS
# print("")
# print("WEEK 1, DAY 4 EXERCISES:")
#
# #1. 99 Bottles of Beer on the Wall
#
# bottles = 99
#
# while bottles > 0:
#     if bottles > 1:
#         print(f"{bottles} bottles of beer on the wall")
#         bottles -=1
#     else:
#         print(f"{bottles} bottle of beer on the wall")
#         break
# print(f"No more bottles of beer on the wall")

#Deaf grandma

# talk = input("What would you like to say to Grandma? ")
#
# while talk != talk.upper():
#     print("HUH? SPEAK UP, GIRL!")
#     talk = input("What would you like to say to Grandma? ")
#
# print("NO, NOT SINCE 1938!")


#Deaf grandma extended

from random import randint

talk = input("What would you like to say to Grandma? ")

while talk != "BYE":
    if talk == talk.upper():
        random_number = randint(1930, 1950)
        print(f"NO, NOT SINCE {random_number}")
    else:
        print("HUH?! SPEAK UP, GIRL")

    talk = input("What would you like to say to Grandma? ")

print("GOODBYE DEAR. SEE YOU SOON")
