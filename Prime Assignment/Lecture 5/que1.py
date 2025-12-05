# Q1. Create a problem that:

# 1. Opens a file "name.txt" in write mode
# 2. Write 5 times (one per line) entered by the user
# 3. Then opens the same file in read mode prints all names

with open("name.txt", "w") as f:
    name = input("Enter a name: ")

    for i in range(5):
        f.write(name + "\n")

with open("name.txt", "r") as f:
    data = f.readlines()

    for line in data:
        print(line)