# Ask the user for a temperature in Celsius (stringinput). Convert it to float,then calculate and print temperature in Fahrenheit.
# Conversionformula:
# 
# FahrenheitTemp=(CelsiusTemp∗(9/5))+32.

a = float(input("Tempereture In Celsius : "))

f = a *(9/5) + 32

print("Tempereture In Fehrenheit is :", f)
