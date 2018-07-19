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
