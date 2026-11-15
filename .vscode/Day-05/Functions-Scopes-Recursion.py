# Define functions; parameters, arguments, return vs print, default arguments and local variables.
# Functions: A function is a block of code which only runs when it is called.
"""def my_function():
  print("Hello from a function")

my_function()   #calling a function
# example 
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
# When a function reaches a return statement, it stops executing and sends the result back
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Arguments are specified after the function name, inside the parentheses.
#  You can add as many arguments as you want, just separate them with a comma. 

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.
#By default, a function must be called with the correct number of arguments.
def my_function(name  = "friend"): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument
my_function()
my_function("Linus")

#keyword arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# list as an argument
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# dictionary as an argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
 # function returning a list
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
# function returning a tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

# *args and **kwargs allow functions to accept a unknown number of arguments.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# The *args parameter allows a function to accept any number of positional arguments.

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

 # Regular parameters must come before *args
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#A function that calculates the sum of any number of values:

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#Finding the maximum value:

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

#Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Accessing values from **kwargs:

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#Regular parameters must come before **kwargs:


def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Scope. A variable is only available from inside the region it is created. This is called scope.
# Local Scope. A variable created inside a function belongs to the local scope of that function,
#  and can only be used inside that function.
def myfunc():
  x = 300
  print(x)

myfunc()

# local variable accesside from function within a function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope. A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# global variable
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# nonlocal variable belong to the outer function
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# The LEGB Rule. Python follows the LEGB rule when looking up variable names, and searches for them in this order:
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

#Decorators let you add extra behavior to a function, without changing the function's code.

#A decorator is a function that takes another function as input and returns a new function. 

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# multiple decorator call
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Lambda Functions. A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.
# Syntax--- lambda arguments : expression
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]   #map()
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8] #filter()
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1]) # sorted
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"] # sort strings by length
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Recursion is when a function calls itself. 
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

# The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones.
#  The sequence starts with 0 and 1: 0, 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# calculate the sum of the list
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# Find the maximum value in a list:

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

#Generators are functions that can pause and resume their execution."""
def my_generator():
  yield 1 # The yield keyword is what makes a function a generator.
  yield 2
  yield 3

for value in my_generator():
  print(value)

# Generate the yield
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

# large sequences
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
