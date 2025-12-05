# Design a program continuously input a number n from user & print if it is positive or negative until the user enters "Quit".

n = input("Enter a number :")

while (n != "Quit"):
    num = int(n)
    if(num > 0):
        print("Positive")

    elif(num < 0):
        print("Negative")

    else:
        print("Zero")

    n = input("Enter a number :")