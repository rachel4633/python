# Tuple
# A tuple is an immutable type of a list (it cannot change)


countries = ("Nairobi", "Mombasa", "Nakuru","Eldoret" ,"Kajiado", "Kisii")

print(countries)
print(type(countries))

#slicing of tuple
print(countries[3:])

#Accessing items of a tuple by use of indexes
print(countries[5:]) 

# Note: Below will generate an error
# Attribute error
countries.append("Machakos")
print(countries)