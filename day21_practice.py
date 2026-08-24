#Use readline()

with open("students.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)

#Use readlines()

with open("students.txt", "r") as file:
    lines = file.readlines()

print(lines)
print(type(lines))

#Use seek(0)

with open("students.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    file.seek(0)
    print(file.readline())

# Suppose data.txt contains:
# Python
# SQL
# Python
# Power BI
# SQL
# Python

# Write a function:
# It should:
# Open the file.
# Read all the lines.
# Count how many lines are in the file.
# Return the count.
# For the file above, the expected result is:
# 6


def count_lines(filename):
    with open (filename,'r') as file:
        lines = file.readlines()
        lines_count = len(lines)
    return lines_count

print(count_lines("data.txt"))

# Write:
# def get_valid_number(filename):
# Requirements:
# Open the given file.
# Read its content.
# Convert it to an integer.
# If the file doesn't exist → return "File not found"
# If the content isn't a valid integer → return "Invalid number"
# Otherwise → return the integer.

def get_valid_number(filename):
    try:
        with open(filename,'r') as file:
            number = int(file.read())
        return number
    except FileNotFoundError:
        return "File Not Found"
    except ValueError:
        return "File does not contain a number"


print(get_valid_number("data.txt"))
print(get_valid_number("students.txt"))
print(get_valid_number("missing.txt"))
