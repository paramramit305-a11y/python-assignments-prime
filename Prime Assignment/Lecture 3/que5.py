# Q5. Create a dictionary where:

# -> Keys = students names 

# -> Values = marks(integer)

# Write a manu-based program where user passes a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the dictionary:

# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student 
# 4. D - Display all students and marks


dict = {
    "Amit": 100,
    "Asif" : 90,
    "sohib": 80,
    "ritu" : 95
}

user = input("Enter keys (A, B, C or D): ")

if user == "A":
    name = input("user's name : ")
    marks = int(input("user's marks : "))
    dict[name] = marks
    print(dict)

elif user == "B":
    name = input("Enter name :")
    if name in dict:
        newmarks = int(input("Enter marks: "))
        dict[name] = newmarks
        print(dict)

    else:
        print("Name Not found")

elif user == "C":
    name = input("enter name: ")
    if name in dict:
        print(dict[name])

    else:
        print("Not found!")

else:
    print(dict)