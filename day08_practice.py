# Exercise 1
# Create a file: notes.txt.Write: Hello Python.Then close the file.

file = open('notes.txt','w')
file.write('Hello Python')
file.close()

# Exercise 2
# Read the file and print its contents.

with open ('notes.txt','r') as file:
    print(file.read())

# Exercise 3
# Append:Learning File Handling.Read the file again.

with open ('notes.txt','a') as file:
    file.write('\nLearning File Handling\n')

with open ('notes.txt','r') as file:
    print(file.read())

# Exercise 4
# Create a file: students.txt
# Write:
# Ali
# Sara
# John
# Read it using a loop.

with open('students.txt','w') as file:
    file.write('Ali\nSara\nJohn')

with open ('students.txt','r') as file:
    for line in file:
        print(line)

# ⭐ Mini Project – Simple Notes App
# Ask the user:Enter a note.
# Save it to:notes.txt.using append mode.
# Every time the user runs the program, the new note should be added instead of replacing the old ones.

note = input("Enter a note: \n")
with open ('notes.txt','a') as file:
    file.write(note + '\n')
with open ('notes.txt','r') as file:
    print(file.read())
