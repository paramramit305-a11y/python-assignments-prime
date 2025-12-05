# Q10. Let’s create a “Number Guessing Game”. 
# Given a secret number (already decided by you), write a program that asks the user to guess it and prints:

# • "Too high" if the guess is above the number
# • "Too low" if the guess is below the number
# • "Correct!" if the guess matches

secretnum = 7

guess = int(input("Guess the number: "))

if(secretnum > guess):
    print("Too low")

elif(secretnum < guess):
    print("Too high")

else:
    print("Correct!")