def Area():
    length = 24
    width = 8
    multiply = length * width
    print("The area of a rectangle is: ",multiply)

Area()    

print('''''''''''''''''''''''''''''''')

def math (x,y):
    sum = x + y
    difference = x - y
    product = x * y
    quotient = x / y if y !=0 else "undefined"
    return sum, difference, product,quotient
    

results = math (10,2)
print(f"results (sum, difference, product,quotient):{results}")

print('''''''''''''''''''''''''''''''')

def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

check_number()

print('''''''''''''''''''''''''''''''')


def sum_up_to_n(n):
    total_sum = 0
    for x in range(1, n + 1):
        total_sum += x
    print(f"The sum of numbers from 1 to {n} is: {total_sum}")    

sum_up_to_n(5)

def square_numbers():
    n = int(input("Enter a number to square up to: "))
    x = 1
    while x <= n:
         print(f"The Square of {x} is {x ** 2}")
         x += 1

square_numbers()