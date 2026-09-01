#Exercise 1
print("Hello , Welocme to python")

#Exercise 2 - Take your name as input.
x = input("Enter your name:")
print("Hello",x)

#Exercise 3 - Take two numbers.Sum , diff , mul , div

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
add = (a+b)
sub = (a-b)
mul = (a*b)
div = (a/b)
print(add,sub,mul,div)

#Exercise 4 - Take age as input.

age = int(input("Enter you age:"))
print("Your age is",age)

#Exercise 5 Convert 100 into an integer. Print its type before and after conversion.

number = ("100")
print(type(number))
number = int(number)
print(type(number))

#Exercise 6 Write a simple calculator 

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
addition = (x+y)
subtraction = (x-y)
multiplication = (x*y)
division = (x/y)
print("addition:",addition)
print("subtraction:",subtraction)
print("multiplication:",multiplication)
print("division:",division)

#Exercise 6 Ask the user for a number and print "Even" if it's divisible by 2, otherwise print "Odd".

num = int(input("Enter the number:"))
if (num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")
