# Boolean - This is a adata type that evaluates to true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidLoan = True
print(paidLoan)
print(type(paidLoan))

# comparison operators are use to compare two or more statements and they usually return a boolean answer 

number1 = 2
number2 = 5

print("is number1 greater than number2? ", number1 > number2)
print("is number1 less than number2? ", number1 < number2)
print("is number1 greater than or equal to number2? ", number1 >= number2)
print("is number1 less than or equal to number2? ", number1 <= number2)

print("is number1 equal to number2? ", number1 == number2)
print("is number1 not equal to number2? ", number1 != number2)

# Logical operators 
#Logical AND 
# It returns true if and only if the condition/statement evaluates to true
print((3 > 1) and (7>6))

# Logical or
# It evaluates true if one of the statement /condition is true
print((3 > 1) or (7 < 6)) 

#Logical not
#it is used to negate a statement/condition
print(not(90 > 70))
