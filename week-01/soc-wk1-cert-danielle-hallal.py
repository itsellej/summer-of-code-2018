#Exercises:

#WEEK 1 - DAY 1 - NUMBERS
print("WEEK 1, DAY 1 EXERCISES:")

seconds = 60
minutes = 60
hours = 24 

#Q1. How many hours are in a year?
hours_year = hours * 365 #Answer: 8760
print(f"Hours in a year: {hours_year}")

#Accounting for leap years
hours_leap_year = hours * 365.25 #Answer: 8766
print(f"Hours in a year (inc. leap year): {int(hours_leap_year)}")


#Q2. How many minutes are in a decade?
mins_decade = (hours_year * minutes) * 10 #Answer: 5256600
print(f"Minutes in a decade: {mins_decade}")

#Accounting for leap years
mins_decade_leap = (hours_leap_year * minutes) * 10 #Answer: 5259600
print(f"Minutes in a decade (inc. leap years) {int(mins_decade_leap)}")


#3. How many seconds old are you?
seconds_per_year = seconds * minutes * hours_leap_year
age = 32
age_seconds = age * seconds_per_year
print(f"My age in seconds: {int(age_seconds)}") #Answer: 1009843200


#4. Calculate Andreea's age (48618000 seconds old) #Is this meant to be 486180000 (extra 0 on the end)?
andreea_seconds = 48618000
andreea_age = andreea_seconds / seconds_per_year #Answer: 1
print(f"Andreea's age in years: {int(andreea_age)}")


#Tougher questions

#5. Calculate your age accurately based on your birthday
from datetime import datetime, timedelta
now = datetime.now()
birth_date = datetime(1986, 5, 25, 16, 4, 00)
age = now - birth_date
print(f"Elle's age: {age.days} days and {age.seconds} seconds")




#WEEK 1 - DAY 3 - LETTERS & NUMBERS
print("")
print("WEEK 1, DAY 3 EXERCISES:")


#1: Full name greeting:
first_name = input("What is your first name? ")
middle_name = input("What is your middle name? ")
last_name = input("What is your last name? ")
print(f"Hello {first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}!")


#2: Bigger, better favourite number:
fave_number = int(input("What's your favourite number? "))
print(f"{fave_number} is a great number. However, {fave_number + 1} is a bigger and better number")

#3 Angry Boss:
request = input("What do you want? ")
boss_says = f"Whaddaya mean \"{request}\"?!? You're fired!!"
print(boss_says.upper())


#4. Table of Contents:
line_width = 60
half_line_width = int(line_width / 2)
print("Chapter 1: Getting Started".ljust(half_line_width) + "page 1".rjust(half_line_width))
print("Chapter 2: Numbers".ljust(half_line_width) + "page 9".rjust(half_line_width))
print("Chapter 3: Letters".ljust(half_line_width) + "page 13".rjust(half_line_width))




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
