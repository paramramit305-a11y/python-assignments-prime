# Q1. Ask the user for a string and check whether it is palindrome or not.
# A Palindrome is a string which is same when we read it forward & backward.
# Eg. - "madam", "racecar" etc.

# [Hint] - A palindrome string  is equal to the reversed version of the string.We can use a loop to reverse the string manually.]

text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

if(text == rev):
    print("it is palindrome!!")

else:
    print("Not palindrome!!")