# Take a decimal number as input (like 45.78) and output its:
# • integer part- 45
# • fractionalpart- .78

x = float(input("Enter a decimal number :"))

int_part = int(x)
frac_part = x - int_part

print("Integer Part :",int_part)
print("Fractional Part :",frac_part)