#WEEK 1 - DAY 4 - LOOPS AND CONDITIONS
print("")
print("WEEK 1, DAY 4 EXERCISES:")

#1. 99 Bottles of Beer on the Wall

bottles = 99

while bottles > 0:
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall")
        bottles -=1
    else:
        print(f"{bottles} bottle of beer on the wall")
        break
print(f"No more bottles of beer on the wall")


# 2.Deaf grandma

talk = input("What would you like to say to Grandma? ")

while talk != talk.upper():
    print("HUH? SPEAK UP, GIRL!")
    talk = input("What would you like to say to Grandma? ")

print("NO, NOT SINCE 1938!")


# 3. Deaf grandma extended, part 1
# Grandma shouts different numbers, and doesn't stop talking until you say BYE

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


# 4. Deaf grandma extended, part 2
# Grandma keeps talking until you say "BYE" three times in a row

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


# 5 Leap years

start_year = int(input("What's your start year? "))
end_year = int(input("What's your end year? "))

print(f"Here are the leap years between {start_year} and {end_year}")

while start_year <= end_year:
    if start_year % 4 == 0 and start_year % 100 != 0:
        print(start_year)

    elif start_year % 400 == 0:
        print(start_year)

    start_year += 1


# 6 daily life calculation - amount of people on the tube

people_in_carriage = int(input("How many people are in your carriage? "))
number_of_carriages = int(input("How many carriages are there? "))
print(f"There are approximately {people_in_carriage * number_of_carriages} people on this train")


# 7 Building and sorting a list

list = []
word = input("Please enter a word: ")

while len(list) < 2:
    if len(word) == 0:
        word = input("You have less than two items in your list. Please add a word: ")
    else:
        while len(word) != 0:
            list.append(word)
            word = input("Please add another word to your list: ")

print(f"Here is your sorted list: {sorted(list)}")


#8. Table of contents, revisited

contents = ["Chapter 1: Getting Started", "page 1", "Chapter 2: Numbers", "page 9", "Chapter 3: Letters", "page 13"]

line_width = 60
half_line_width = int(line_width / 2)

print(contents[0].ljust(half_line_width) + contents[1].rjust(half_line_width))
print(contents[2].ljust(half_line_width) + contents[3].rjust(half_line_width))
print(contents[4].ljust(half_line_width) + contents[5].rjust(half_line_width))


#9 Moo function

def moo (n):
    big_moo = "moo " * n
    print(big_moo)

#test
moo (5)
moo (10)
moo (44)


#10 Old-school Roman numerals

#Advanced question, which I will revisit when I have more Python and programming knowledge
