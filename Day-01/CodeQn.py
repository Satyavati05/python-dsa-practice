"""
# minicalculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)

# temperature converter

celsius = float(input("Enter temp in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit is : ", fahrenheit)

# swap two numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
a, b = b, a
print(a, b)

#calculate average
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average of three numbers is: ", average)"""

# fibonacci numbers
prev2 = 1
prev1 = 2
for i in range(3):
    print(prev2)
    next_num = prev1 + prev2
    prev2 = prev1
    prev1 = next_num