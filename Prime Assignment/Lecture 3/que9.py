# Q9. Given a list, print all elements that appear more than once in the list.

# [Hint - use sets]

l = [1, 1, 2, 2, 3 , 7 , 4, 5]
s = {1, 2, 3, 4, 5, 7}

count = 0

for elements in s:
    if(l.count(elements) > 1):
        print(elements)