# age = int(input("enter the age: "))
try:
    age = int(input("enter the age"))
except ValueError:
    print("Invalid Age")
else:
    print("No Exception were thrown")
    print("program will continue execution")
