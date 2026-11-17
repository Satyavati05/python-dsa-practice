"""
Review traversal, running sum, min/max, in-place updates and two-pointer intuition.
• Solve: running sum, maximum element, move zeroes, remove duplicates from sorted array.
• Try two-sum with brute force first; record its time complexity.
• Revisit Days 1-6. Rebuild 2 programs without notes.
Milestone: 8-12 beginner problems attempted so far; list concepts that still feel unclear.

"""

# Array Traversal
num = [10,20,30,60]
for n in range(2):  #Used for counting, searching, summing and comparisons.Time complexity: O(n).
    print(num)     #Extra space: O(1).

# Running Sum
num  = [1,2,3,4,5]
total = 0
for n in num:
    total+=n
print(total)

# min/max
numbers = [12, 5, 18, 3, 25]
largest  = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(largest)
print(smallest)
    
    

# in-place updates
list = ["Annu", 4, "Doda"]
list[0] = "Yogini"
list[1] = 3
print(list)


# Two Pointer Function
numbers = [4,3,2,1]

left = 0
right = len(numbers)-1

while left < right:
    print(numbers[left], numbers[right])
    left += 1
    right -= 1


# Solve Running Sum; Record it's Time Complexity
# Think about it: Start with an empty result list.Start total = 0.
# Traverse the original list.Add each element to total.Append the updated total to the result.
arr = [1, 2, 3, 4, 5]
result = []
total = 0
for num in arr:
    total+=num
    result.append(total)  # Complexity: Time O(n), extra space O(n).
print(result)


# Solve maximum element
def find_maximum(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest
#Time complexity: O(n). Extra space: O(1)
print(find_maximum([12, 5, 18, 3, 25, 9]))

# Solve move zeroes .  two pointer pattern
# Given an array, move all zeroes to the end while keeping the order of non-zero elements unchanged.
# The right approach: Two pointers
#For this problem, we'll use a slightly different version of two pointers.
#i will scan every element,position will remember where the next non-zero element should be placed.
def move_zeroes(arr):
    position = 0
     # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[position] = arr[i]
            position +=1
#Fill remaining positions with zeroes
    while position < len(arr):
        arr[position] = 0
        position += 1 # Time complexity: O(n), Extra space: O(1)
    return arr
print(move_zeroes([0, 1, 0, 3, 0, 12]))


# Solve remove duplicates from sorted array
"""arr = [1, 1, 2, 2, 3, 4, 4, 5]
unique_arr = set(arr)
print(unique_arr)"""
# Also done by two pointer approach..e'll use two pointers:
# i checks each element,position tracks where the next unique element should be placed.
arr = [1, 1, 2, 2, 3, 4, 4, 5]

position = 0

for i in range(1, len(arr)):
    if arr[i] != arr[position]:
        position += 1
        arr[position] = arr[i]  # O(n) time and O(1) extra space.

print(arr[:position + 1])

# Try two-sum with brute force first; record its time complexity.
# given an array of integers and a target number. 
# Find two different elements whose sum equals the target.
def twoSum(int, target):
    
    for i in range(len(int)):
        for j in range(i+1,len(int)):
            if int[i] + int[j]  == target:
                return [i,j]
                
    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6)) # time complexity = O(n2), space = O(1)


# Revisit Days 1–6, Rebuild 2 programs without notes.
#Program 1 - First non-repeating character.
# Given a string, return the first character that appears only once.
word = "Geography"
frequency = {}
found = False
for ch in word:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch] = 1
for ch in word:
    if ch == frequency:
        print(ch)
        found = True
        break
for ch in word:      # time  = O(n) and space = O(k)
    if not found:
        print(-1)



#Program 2 — Binary Search
#Find the index of the target in a sorted array. Return -1 if it isn't found.
