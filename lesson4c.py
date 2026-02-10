# A for loop can also be used to iterate through a list ,tuple, string or even a dictionary..

name = "Rakel"

for letter in name:
    if letter == "k":
        print("the letter is k")
    else:
        print(letter)    
    

print("=========================")

# below is a list of countries

counties = ["Nairobi", "Kisumu", "Nakuru","Eldoret","Kajiado","Machokos","Meru","Embu",]

print(counties)

for county in counties:
    print(county)

print("=========================")

for county in counties:
    if county == "Nairobi":
        print("The county is part of the list")
        break
    else:
        print("The county is not part of the list")
        

print("=========================")

player = {
    "name": "Neymar",
    "age": 25,
    "teams": ["PSG", "Monaco","France",],
    "nationality": "Brazilian"
}
for key in player:
    print(key)

print("=========================")


for value in player:
    print(player[value])

print("=========================")



for team in player["teams"]:
    print(team)
    