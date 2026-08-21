x = 10

def test():
    x = 20
    print(x)

test()
print(x)

# Exercise 2
x = 10

def test():
    print(x)

test()

#Exercise 3 
# This code will give error the local variable is assigned after trying to print the value 
# x = 10

# def test():
#     print(x)
#     x = 20

# test()

# Exercise 5 — global
x = 10

def test():
    global x
    x = 20

test()
print(x)

#Exercise -

x = 100

def outer():
    x = 200

    def inner():
        print(x)

    inner()

# Exercise - nonlocal 

def counter():
    count = 0

    def increment():
        nonlocal count 
        count += 1
        return count

    return increment

my_counter = counter()

print(my_counter())
print(my_counter())
print(my_counter())
