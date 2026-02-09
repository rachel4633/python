salary = int(input("enter salary input: "))

if salary > 0 and salary < 5999:
    print("Ksh150.00")
elif salary > 6000 and salary < 7999:
    print("Ksh300.00")
elif salary > 12000 and salary < 14999:
    print("Ksh400.00") 
elif salary > 15000 and salary < 19999:
    print("Ksh500.00")   
elif salary > 20000 and salary < 24999:
    print("Ksh750.00") 
elif salary > 25000 and salary < 29999:
    print("Ksh850.00")   
elif salary > 30000 and salary < 49999:
    print("Ksh1000.00")  
elif salary > 50000 and salary < 99999:
    print("Ksh1550.00")
elif salary >=100000:
    print("Ksh2000.00")
else:
    print("Invalid input")                   

