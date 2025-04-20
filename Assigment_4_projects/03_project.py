#Fahrenheit to Celsius Conversion

# User se Fahrenheit mein temperature lena
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Fahrenheit ko Celsius mein convert karna
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Result print karna
print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")
