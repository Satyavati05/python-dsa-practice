# tuple immutability; set uniqueness and membership; dict key/value access and updates.
# 1 — Tuple is a collection of values, just like a list, but you cannot change its elements after creation.
# Constructor: tuple, set, dictionay
"""student = ("Aman", 22, "MCA")

print(student[0])  # Aman
print(student[1])  # 22

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])   # indexing 

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"   #change tuple values
x = tuple(y)

print(x) 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")  #convert tuple into a list
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("papaya",)
thistuple += y  #add tuple to a tuple
print(thistuple)
y = list(thistuple)
y.remove("apple") # remove
thistuple = tuple(y)
print(thistuple)
#the del keyword can delete the tuple completely

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits # unpack the tuples
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits #Python will assign values to the variable until the number of values left matches the number of variables left.
print(green)
print(tropic)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
# join the tuples
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 # multiply the tuple

print(mytuple)
# tuple methods

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

# Set: A set is a collection which is unordered, unchangeable*, and unindexed.
thisset = {"apple", "banana", "cherry", "cherry"}
thisset.add("orange") # add()
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # update()
print(thisset)  # True and 1 has same value and False and 0 has same value
print("banana" in thisset)
print("banana" not in thisset)
# remove(), discard(), pop(), clear(), del
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# union and | are same
set3 = set1.union(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#intersection and & are same
set3 = set1.intersection(set2)
print(set3)
#difference and - are same
set3 = set1.difference(set2)
print(set3)
# frozen sets ..Being immutable means you cannot add or remove elements.

copy()Returns a shallow copy	
difference()	- Returns a new frozenset with the difference	
intersection()	& Returns a new frozenset with the intersection	
isdisjoint()	Returns True if there is NO intersection between two frozensets	
issubset()	<= / < Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / > Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^ Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union

# Dictionary..Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#  Practice in, get(), keys(), values(), items(), frequency counting
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1995,  # duplicate value overwite the prev value
   "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))  #datatype
print(len(thisdict))   # length
x = thisdict.keys() # get list of keys, .get()
x = thisdict.values() # get list of values
x = thisdict.items() #return each item
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change

car["color"] = "white"
print(x) #after the change  ,we have all keys present here
# change the value of a specific item by referring to its key name
car["year"] = 2018
print(car)
car.update({"year": 2020}) #update the value
print(car)
# remove ke liye .popitem(), clear(), del
for x in car:
  print(car[x])   #loop printing values one by one

for x in car.values(): # printing values 
   print(x)
for x in car.keys():  # printing keys
  print(x)
for x in car.items(): # printing both keys and values
  print(x)
car = car.copy()  # copy the dictionary
print(car)
# nested dictionary 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child2"]["name"]) # access the elements

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# dictionary methods
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary #yes"""
