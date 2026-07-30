'''Exercise 1 - Take a number and determine whether it is:

Positive
Negative
Zero'''

number = int(input("Enter the number: "))
if number>0:
    print("The number is a positive number")
elif number==0:
    print("The number is zero")
else:
    print("The number is a negative number")

'''Exercise 2
Take marks as input.
Print:
A (90–100)
B (75–89)
C (50–74)
Fail (<50)'''

marks = int(input("Enter the total marks"))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=90:
    print("The grade is A")
elif marks>=75:
    print("The grade is B")
elif marks>=50:
    print("The grade is C")
else:
    print("Fail")


'''Take three numbers.
Print the largest.'''

first_number = int(input("Enter the first number "))
second_number = int(input("Enter the second number "))
third_number = int(input("Enter the third number "))
if first_number>=second_number and first_number>=third_number:
    print("The first number" ,first_number, "is the largest")
elif second_number>=first_number and second_number>=third_number:
    print("The second number",second_number," is the largest",)
elif third_number>=first_number and third_number>=second_number:
    print("The third number",third_number," is the largest",)


'''Exercise 4
Check whether a year is a leap year.'''

year = int(input("Enter the year"))
if year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


'''Exercise 5
Password checker.
Correct password:
python123
If the entered password matches, print:
Access Granted
Otherwise:
Access Denied'''

password = input("Enter the password")
if password == 'python123':
    print("Access Granted")
else:
    print("Access Denied")


'''Mini Project: Smart Calculator
Requirements:

Use if, elif, else
Handle invalid operators
Prevent division by zero'''

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Enter the operation:  ")
if operation == '+':
    print("Result = ",first_number+second_number)
elif operation == '-':
    print("Result = ",first_number-second_number)
elif operation == '*':
    print("Result = ",first_number*second_number)
elif operation == '/':
    if second_number == 0:
        print("Division with zero is not possible")
    else:
        print("Result = ",first_number/second_number)
else:
    print("The entered operator is invalid.Please enter a valid operator from +,-,*,/")



'''Write a program that asks for:

Username
Password'''

username = input("Enter the username")
password = input("Enter the password")
if username == 'testuser' and password == 'test101':
    print("Welcome user")
else:
    print("Invalid Credentials")

