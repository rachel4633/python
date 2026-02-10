# Python function
# They are a block of code /statement that performs a given task/action. They can be reused through out the program to perform different tasks.
# Function are defined using the def keyword. (deifine)

#We have two main types of function i.e :
#1. In-built function -> They come preinstalled with interpreter i.e print() ,pop(),range(), append() etc...
# 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.

def greeting():
    print("Hello, How are you?")


greeting()

print('''''''''''''''''''''''''''''''')

# Additional function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

addition()

print('''''''''''''''''''''''''''''''')   

# create a function that is able to multiply 3 values\

def multiply():
    num1 = 3
    num2 = 3
    num3 = 2
    product = num1 * num2 * num3
    print("The answer of the multiplication: ", product) 

multiply() 

# Below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 /number2
    print("The answer is : ",quotient)

    print("-----------------------")


for function in range(3):
    divide()   
     
