# A dictionary is a data type that stores data in terms of key- value pair .
# It is introduced by the use of curly braces {}
# The values stored inside of a dictionary can be of any data type.
# To access the value in a dictionary we use the keys


phonebook = {
    "Benson" : "254712345",
    "Mary" : "254712345",
    "Rakel" : "25412345"
}
#showing the entire dictionary
print(phonebook)


#print out benson's number
print(phonebook["Benson"])

print("============================")

player = {
    "Name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"]
}

print(player["teams"][1])                                   