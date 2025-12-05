# Q4. Given a tuple of integers, create:

#  ->  A tuple of all even numbers
#  ->  A tuple of all odd numbers

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even = ()
odd = ()

for num in t:
    if(num % 2 == 0):
        even += (num,)

    else:
        odd += (num,)

print(f"Even numbers : {even}")
print(f"odd numbers : {odd}")