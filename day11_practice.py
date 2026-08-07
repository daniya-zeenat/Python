# Exercise 1
# Create a class: Student
# Store:
# name
# age
# Create two students.Print both.

class Student:
    pass

student1 = Student()
student1.name = 'Ali'
student1.age = 25

student2 = Student()
student2.name = 'John'
student2.age = 56

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

# Exercise 2
# Create: Car
# Store:
# brand
# model
# Create two cars.
# Print their details.

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = car('suzuki','kia')
car2 = car('mercedes','benz')

print(car1.brand)
print(car1.model)
print(car2.brand)
print(car2.model)

# Exercise 3
# Add a method:
# introduce()
# Output:
# Hi, I am (name)        

class name():
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print('Hi I am ',self.name)

names = name('Mina')
names.introduce() 

# Exercise 4
# Create a class:
# Rectangle
# Store:
# length
# width
# Create a method:
# area()
# Return:
# length * width

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

formula = Rectangle(10,10)
print(formula.area())

# ⭐ Mini Project – Bank Account
# Create a class: BankAccount
# Attributes:
# account_holder
# balance
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Example:
# account = BankAccount("Ali",1000)
# account.deposit(500)
# account.withdraw(200)
# account.display_balance()
# Output:
# Balance: 1300

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,deposit_amount):
          self.balance = deposit_amount + self.balance
    def withdraw(self,withdrawn_amount):
        if withdrawn_amount<= self.balance:
             self.balance = self.balance - withdrawn_amount
        else:
            print("Insufficient Balance")
    def display_balance(self):
        print('Current Balance = ', self.balance)
    
account = BankAccount('Farida',2000)
account.deposit(5000)
account.withdraw(200)
account.display_balance()


        
        