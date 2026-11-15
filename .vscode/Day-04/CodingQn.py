#Character frequency — banana
"""word = "satyavati"
frequency = {}
for ch in word:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
    
print(frequency)


# Word counter — count words in a sentence
sentence = "Python is easy to learn"
words = sentence.split()
count =len(words)
print(count)

# Remove duplicates using a set
numbers = {2,4,5,2,6,8,9,4,8,8,1}
unique_numbers = set(numbers)
print(unique_numbers)


# Student marks dictionary — store and retrieve marks
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78
}

# 1. Print Priya's marks
print(students["Priya"])
# 2. Update Rahul's marks
students["Rahul"] = 90
# 3. Print the dictionary
print(students)

#Medium challenge: Find the first non-repeating character
# Problem:Given a string, find the first character that appears exactly once.

#s = "swiss" # w
s = "aabbcc"  # -1
frequency = {}
found = False
for ch in s:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
for ch in s:
    if frequency[ch] == 1:
        print(ch)
        found = True
        break
for ch in s:      # time  = O(n) and space = O(k)
    if not found:
        print(-1)

# Hashing work? 
# Think of a dictionary or set as a system that helps Python locate information quickly.

A = [1,2,3,4,5]
B = [3,4,5,6,7]
common = []
for a in A:
    for b in B:
        if a==b:
            common.append(a)
# Time:O(n*m)
print(common)

# hashing version
A = [1,2,3,4,5]
B = [3,4,5,6,7]
seen = set(A)
common = []
for num in B:
    if num in seen:   # Time= O(n+m)
        common.append(num)
print(common)

#Remember:
#Set: useful when you need to check whether something exists.
#Dictionary: useful when you need to store information associated with a key, such as frequencies."""
A = [10, 20, 30, 40, 50] # ex 1
B = [30, 40, 60, 70]
seen = set(A)
common = []
for num in B:
    if num in seen:
        common.append(num)
print(common)
# find duplicates in array
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
seen = set()
duplicates = []
for num in numbers:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print(duplicates)