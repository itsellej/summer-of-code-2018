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

#2.Deaf grandma

# talk = input("What would you like to say to Grandma? ")
#
# while talk != talk.upper():
#     print("HUH? SPEAK UP, GIRL!")
#     talk = input("What would you like to say to Grandma? ")
#
# print("NO, NOT SINCE 1938!")


#3. Deaf grandma extended, part 1
#Grandma shouts different numbers, and doesn't stop talking until you say bye

# from random import randint
#
# talk = input("What would you like to say to Grandma? ")
#
# while talk != "BYE":
#     if talk == talk.upper():
#         random_number = randint(1930, 1950)
#         print(f"NO, NOT SINCE {random_number}")
#     else:
#         print("HUH?! SPEAK UP, GIRL")
#
#     talk = input("What would you like to say to Grandma? ")
#
# print("GOODBYE DEAR. SEE YOU SOON")


#4. Deaf grandma extended, part 2
#Grandma keeps talking until you say "BYE" three times in a row

from random import randint

bye_count = 0
talk = input("What would you like to say to Grandma? ")

while bye_count < 3:
    if talk == talk.upper() and talk !="BYE":
        random_number = randint(1930, 1950)
        print(f"NO, NOT SINCE {random_number}")
        bye_count = 0

    elif talk == "BYE":
        bye_count += 1

        if bye_count != 3:
            print("HUH?! SPEAK UP, GIRL")
        else:
            print("GOODBYE DEAR")
            break

    else:
        print("STOP WHISPERING, GIRL!")
        bye_count = 0

    talk = input("What would you like to say to Grandma? ")




# while talk != "BYE":
#     bye_count = 0
#     if talk == talk.upper():
#         random_number = randint(1930, 1950)
#         print(f"NO, NOT SINCE {random_number}")
#         talk = input("What would you like to say to Grandma? ")
#     else:
#         print("STOP WHISPERING, GIRL!")
#         talk = input("What would you like to say to Grandma? ")
#
# while talk == "BYE":
#     bye_count +=1
#     if bye_count != 3:
#         print("HUH?! SPEAK UP, GIRL")
#         talk = input("What would you like to say to Grandma? ")
#
#     else:
#         print("GOODBYE DEAR. SEE YOU SOON")
#         break
