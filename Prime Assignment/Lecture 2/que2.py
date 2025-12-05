# Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

a = int(input("Enter a:"))
b = int(input("Enter b:"))

def even():
    for i in range(a, b+1):
        if(i % 2 == 0):
            print(i)

even()