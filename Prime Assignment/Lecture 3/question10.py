# Q10. Ask the user for a string and print:

# -> All Unique Characters 
# -> The Count of Unique Characters

user = input("Enter a string: ")

s = set()

for ch in user:
    s.add(ch)

print(s)
print(len(s))
