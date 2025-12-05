# Q7. Write a program that takes a string from the user and prints the number of spaces in the string.

user = input("Enter a string: ")

space = 0

for ch in user:
    if ch == " ":
        space += 1

print(space)