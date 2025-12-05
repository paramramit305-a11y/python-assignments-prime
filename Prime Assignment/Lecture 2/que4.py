# Write a function to return the count the number of digits in a number, n.

number = input("Enter a number: ")

def digits():
    count = 0
    for ch in number:
        count += 1
    return count

print(digits())