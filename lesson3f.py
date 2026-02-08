# Create a python program that is able to determine whether a number entered is either an odd number or even number.

# number = int(input("Enter your number here: "))
# if number % 2 == 0:
#     print("The number is even")
# else:
    # print("The number is odd")    

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person.if the weight is greater than 50kg and age 18. then the person can donate blood else not possible

age = int(input("Enter age: "))
weight = float(input("Enter weight:"))

if age >= 18 and weight >= 50:
    print("Can donate")
else:
    print("Not possible")    