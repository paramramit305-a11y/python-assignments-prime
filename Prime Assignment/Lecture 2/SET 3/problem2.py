# Create a function to return largest of 3 numbers - a, b & c.

def largest(a, b, c):
    if(a > b and a > c):
        print("a is largest")

    elif(b > a and b > c):
        print("b is largest")

    elif(c > a and c > b):
        print("c is largest")

largest(115, 15, 6)