# Q3. Create a program that:

# 1. Has a list of numbers: [5, 10, 15, 20, 25]

# 2. Uses a list comprehension to create a new list with only numbers greater than 15

# 3.Print the new list

l = [5, 10, 15, 20, 25]

l = [val for val in l if val > 15]
print(l)