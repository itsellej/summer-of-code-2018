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
