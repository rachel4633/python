# Python list
#A list in python is a collection of items thta are orderded in a certain way.
# A list is introduced by the use of the square brackets []
# The items of a list are stored inside of indexes. Note: In programming we start counting from index zero(0). bwm, benz, hiance,...
# A list is mutable i.e the content of a list can be changed.

cars = ["BMW", "Benz", "Hiance", "Prado", "Probox","Mclaren", "Range"]
print(cars)
print(type(cars))

#Accessing item of a list
print(cars(2))
print("The car on index four is: ", cars[4])

#list slicing - This is creating a list from a given bigger list 
print(cars[4:])

#print from index zero index to three
print(cars[:4])

#printing from hiance to probox
print(cars[2:5])

#list-mutability
#We use function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

#We use pop function to remove an item at the end of the list
cars.pop()
print(cars)

# We can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

# We can use the function to sort out the items in alphabebitcal order
cars.sort()
print(cars)