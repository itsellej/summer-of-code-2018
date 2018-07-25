# #1. Modify "a" for another name in my_dict
#
# my_dict = {
#     "a": 35000,
#     "b": 8000,
#     "z": 450
# }
#
# my_dict["a_new"] = 35000
#
# del(my_dict["a"])
#
# print(my_dict)


#2. Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary


# #3. Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.
#
# elle_dict = {
#     "name": "Elle",
#     "location": "London, UK"
# }
#
# print(elle_dict)
#
# #add another key value pair
# elle_dict["surname"] = "J"
# print(elle_dict)
#
# #modify a value
# elle_dict["surname"] = "H"
# print(elle_dict)
#
# #access location
# print(elle_dict["location"])
#
# #delete key-value pair
# del(elle_dict["surname"])
# print(elle_dict)



#4. Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

class Student():

    def __init__(self, name, fav_food, dream):
        self.name = name
        self.fav_food = fav_food
        self.dream = dream

    def s_print(self):
        return self.name + ", " + self.fav_food + ", " + self.dream

s1 = Student("Virginia Balseiro", "pasta", "moving to Europe")
s2 = Student("Deb Cupitt", "chocolate", "gender equality")
s3 = Student("Sacha Young", "french fries", "to return to research")
s4 = Student("Jessi RS", "pasta", "work as a developer")
s5 = Student("Bituin Callanta", "sashimi", "lessen the gender wage gap")

#test
print(s1.name)
print(s2.fav_food)
print(s3.dream)
print(s4.fav_food)
print(s5.name)

print(s1.s_print())
print(s2.s_print())
print(s3.s_print())
print(s4.s_print())
print(s5.s_print())
