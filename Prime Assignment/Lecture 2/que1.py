# Write a program that takes 'salary' as input. Using conditional statements,calculate the 'final tax rate' based on these 

# •If salary < 30,000 → 5% 

# •If salary is 30,000–70,000 → 15%

# •If salary > 70,000 → 25%

salary = int(input("Enter Salary:"))

if (salary < 30000):
    print("5% Tax Rate")

elif(salary >= 30000 and salary <= 70000):
    print("15% Tax Rate")

elif(salary > 70000):
    print("25% Tax Rate")