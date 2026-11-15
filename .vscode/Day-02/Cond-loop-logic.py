#Conditional---if/elif/else
"""number = 15
if number > 0:
  print("The number is positive")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

is_logged_in = True  #Variables in Conditions
if is_logged_in:
  print("Welcome back!")

a = 25
b = 11
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif b < a:
  print("a is less than b")

num  = 12
if num%2 == 0:
    print("The number is even")

else:
    print("The number is odd")

light = "white"
if light == "yellow":
    print("slow down")
elif light == "green":
    print("go")
elif light == "red":
    print("stop")
else:
    print("invalid for traffic light")
#Short hand if...else
a = 2
b = 330
print("A") if a > b else print("B")

# logical operators....and/or/not
 
a = 100
b = 90
c = 200
if a > b and c > a:
  print("Both the conditions is True")


a = 100
b = 90
c = 80
if a > b or c > a:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Example
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
# nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass statement is a null operation - nothing happens when it executes. 
# It serves as a placeholder.

value = 4

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")
# Instead of writing many if..else statements, you can use the match statement.
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

    # The value _ will always match,
    #  so it is important to place it as the last case to make it behave as a default case.

    # loop----while,for


i = 1
while i < 6:
  print(i)
  if i == 3:
    break  # the break statement we can stop the loop even if the while condition is true
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # the continue statement we can stop the current iteration, and continue with the next:S
  print(i)

else: # the else statement we can run a block of code once when the condition no longer is true
  print("i is no longer less than 6")  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
for x in range(4,9): # range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
  print(x)
else:
  print("The for loop is over")"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:  # nested loop
  for y in fruits:
    print(x, y) 
  