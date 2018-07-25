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


#3. Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.

elle_dict = {
    "name": "Elle",
    "location": "London, UK"
}

print(elle_dict)

#add another key value pair
elle_dict["surname"] = "J"
print(elle_dict)

#modify a value
elle_dict["surname"] = "H"
print(elle_dict)

#access location
print(elle_dict["location"])

#delete key-value pair
del(elle_dict["surname"])
print(elle_dict)
