def calculate(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"

print(calculate(10, 2))
print(calculate(10, 0))
print(calculate("10", 2))


def test():
    try:
        print("A")
        x = 10 / 0
        print("B")
    except ZeroDivisionError:
        print("C")
    finally:
        print("D")

test()

def test():
    try:
        print("A")
    except:
        print("B")
    else:
        print("C")
    finally:
        print("D")

test()

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

print(check_age(20))
print(check_age(15))

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

try:
    print(check_age(15))
except ValueError as e:
    print(e)

# Write a function:
# Requirements:
# If amount > balance, raise a custom InsufficientBalanceError.
# Otherwise, return the remaining balance.
# Use try/except when calling the function.
# Test it with:
# withdraw(5000, 2000)
# withdraw(5000, 7000)

class insufficientbalance(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise insufficientbalance ("Insuffiecient Balance")
    return balance - amount
try:
    print(withdraw(5000,2000))
    print(withdraw(5000,7000))
    
except insufficientbalance as e:
    print(e)


# Build a function:
# def register_user(username, age):
# Requirements:
# If username is empty, raise a custom InvalidUsernameError.
# If age is less than 18, raise a custom UnderAgeError.
# If everything is valid, return:
# "Registration successful"
# Create both custom exception classes.
# Use try/except when calling the function.
# Test all three cases:
# register_user("riva", 22)
# register_user("", 26)
# register_user("Alex", 16)

class InvalidUsernameError(Exception):
    pass
class UnderAgeError(Exception):
    pass

def register_user(username, age):
    if age < 18:
        raise UnderAgeError ("User is Under Age")
    if username == '':
        raise InvalidUsernameError("Invalid Username")
    return ("Registration successful")

try:
    print(register_user("riva", 22))

except UnderAgeError as e:
        print(e)
except InvalidUsernameError as e:
     print(e)
