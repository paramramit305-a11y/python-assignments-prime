# Write a function to return the sum of digits of a number, n.

def digits():
    sum = 0
    number = int(input("Enter a number: "))
    while number > 0:
        d = number % 10
        sum += d
        number = number // 10

    return sum

print(digits())