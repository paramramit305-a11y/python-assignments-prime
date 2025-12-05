# Q5. Write a program that tries to open "data.txt" in read mode. if the file does not exist, catch the exception and print "File not found!".

try:
    with open("data.txt", "r") as f:
        data = f.read()
        print(data)
        
except Exception :
    print("File Not Found")