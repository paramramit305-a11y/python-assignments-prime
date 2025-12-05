# Count Vowels in a word (A E I O U).   [ Using for]

word = "artificial"

count = 0

for ch in word:
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        count+=1

print("count =",count)