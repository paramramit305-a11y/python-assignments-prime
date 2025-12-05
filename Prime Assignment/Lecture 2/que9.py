# Q9. Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

# Hint —

# We only check prime for 2 or numbers greater than 2.
# 2 is the smallest prime number.

# A non-prime number n will always get divided by at least one number in range [2, n-1].

# Example:

# For number 9, we’ll check in range (2, 8) and it’ll get divided by 3 → so 9 is non-prime → return False.

# For number 7, we’ll check in range (2, 6) and it won’t get divided by any → so 7 is prime → return True.


n = int(input("Enter a number: "))

def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,n):
        if(n % i== 0):
            return False
        
    return True

print(is_prime(n))