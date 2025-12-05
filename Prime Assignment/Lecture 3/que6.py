# Q6. Given a list of words:

#  Words = ["apple", "banana", "kiwi", "cherry", "mango"]

#  Create a dictionary that maps each word to its length.

# Example :

#    {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]

dict = {
    "apple" : len(words[0]),
    "banana": len(words[1]),
    "kiwi":len(words[2]),
    "cherry": len(words[3]),
    "mango": len(words[4])
}

print(dict)