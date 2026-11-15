# Strings: indexing, slicing, len(), membership, immutability, common methods
"""a = "Hello"
print(a)

a = "Hello, World!"  #  strings are arrays
print(a[1])

for x in "banana":   # looping through a string
  print(x)

a = "Hello, World!" # length
print(len(a)) 

# 1. Indexing: Python uses zero-based indexing. That means the first character is at index 0, not 1.
word = "PYTHON"
print(word[0])   # P
print(word[2])   # T
print(word[5])   # N
print(word[-1])  # N (last character)
print(word[-2])  # O (second last) 

#2.Slicing: Slicing extracts a portion of a string.
b = "Hello, World!"
print(b[2:5])
print(b[:5]) # from the start
print(b[2:]) # to the end
print(b[-5:-2]) # negative indexing

# 3. Membership: The 'in' keyword checks if a substring exists within a string.
word = "programming"

print(len(word))        # 11
print("gram" in word)   # True
print("java" not in word) # True 


a = "Hello, World!"  # modify strings
print(a.upper()) # lowercase
print(a.lower()) # uppercase
print(a.strip()) # Remove outer whitespace
print(a.replace("H", "J")) #replace characters
print(a.split(","))   # split into a text

# 4. Immutability: Strings cannot be changed after they are created.
#  Any operation that modifies a string will create a new string.
word = "HELLO"
# word[0] = "Y"  # TypeError
word = "Y" + word[1:]
print(word)  # YELLO 

# 5. Common Methods: 
lower(). Converts all uppercase characters to lowercase.
upper(). Converts all lowercase characters to uppercase.
capitalize(). Converts only the first character to uppercase and makes the rest lowercase.
title(). Capitalizes the first character of every word in the string.
swapcase(). Reverses the case of every letter, turning uppercase into lowercase and vice versa.
casefold(). Converts text into an aggressive lowercase format designed for caseless string matching across different languages.
find(sub). Returns the lowest index where the substring sub is found, or -1 if it does not exist.
rfind(sub). Returns the highest index where sub is found, searching from right to left.
index(sub). Works just like find(), but raises a ValueError instead of returning -1 if the substring is missing.
count(sub). Returns the total number of non-overlapping times sub appears in the string.
startswith(prefix). Returns True if the string begins with the specified prefix.
endswith(suffix). Returns True if the string ends with the specified suffix.
strip(chars). Removes leading and trailing whitespace, or any specified characters, from both ends of a string.
lstrip() / rstrip(). Removes whitespace or specified characters strictly from the left (start) or right (end) side.
split(sep). Breaks a string into a list of substrings using the specified delimiter, defaulting to any whitespace.
splitlines(). Splits a multi-line string at line breaks and returns a list of lines.
join(iterable). Concatenates an iterable of strings into a single string, placing the caller string as a separator between each element.
replace(old, new). Returns a copy of the string where all occurrences of old are swapped with new.

isalpha()	Alphabetic letters (a–z, A–Z) with at least one character present.
isdigit()	Digits (0–9), including superscripts and subscripts.
isnumeric()	Numeric characters, including digits, fractions, and Roman numerals.
isalnum()	Alphanumeric characters (letters or numbers, no spaces or symbols).
isspace()	Whitespace characters such as spaces, tabs, or newlines.
islower() / isupper()	Cased characters that are all lowercase or all uppercase.

format(*args, **kwargs). Replaces curly-brace {} placeholders in a string with formatted values.
center(width, fillchar). Centers the string within a field of the given width, padding with spaces or a custom fillchar.
ljust(width) / rjust(width). Left-aligns or right-aligns the string within a specified character width.
zfill(width). Pads a numeric string on the left with zeros (0) until it reaches the specified width.


#  Lists:Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets.
# indexing, slicing, append(), extend(), insert(), pop(), remove(), sort(), sorted().
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # range of index
print(type(thislist))
print(thislist[-1])  # negative indexing
print(thislist[-4:-1]) # nagative index change

thislist.append("grapes")
print(thislist)  # add an item to the end of the list
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"] #extend() method adds the elements of a list (or any iterable), to the end of the current list.
thislist.extend(tropical)
print(thislist)
thislist.remove("banana") #remove 
print(thislist)
thislist.pop(1) #pop() method removes the specified index, (or the last item if index is not specified)
print(thislist)
#The del keyword also removes the specified index
 # The clear() method empties the list.
del thislist[0]
print(thislist)"""

numbers = [5, 2, 8, 1] #sort .Sorts the original list

result = numbers.sort()
print(numbers)  # [1, 2, 5, 8]
print(result)   # None

numbers = [5, 2, 8, 1]  #sorted(). Returns a new sorted list without modifying the original list
result = sorted(numbers)
print(numbers)  # [5, 2, 8, 1]
print(result)   # [1, 2, 5, 8]

