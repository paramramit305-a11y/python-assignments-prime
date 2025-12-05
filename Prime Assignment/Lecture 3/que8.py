# Q8. Write a program to check whether two lists share no common elements.

# share no common elements list1 =[1,2,3,4]      list2 =[5,6,7,8]

# share common elements list1 =[1,2,3] list2 =[3,4]

# [Hint - use sets]


list1 = (1, 2, 3, 4, 5)
list2 = (6, 7, 10, 8, 9)

found = False

for values in list1:
    if values in list2:
        found = True
        print(f"Common elements found : {values}")
        

if not found:
    print("No common elements.!")