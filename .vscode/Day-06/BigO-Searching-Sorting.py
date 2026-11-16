""" # Big-O, searching & sorting basics...
# Learn time vs space complexity; O(1), O(log n), O(n), O(n log n), O(n²) at an intuitive level.
# Time complexity tells us how the amount of work an algorithm does grows when the input size increases.

## O(1) — Constant time. You access one element directly.
#  The list could have 4 or 4 million elements; the operation count stays constant.
numbers = [10, 20, 30, 40, 50]
print(numbers[0])

## O(n) — Linear time
# If there are 5 elements, approximately 5 iterations. If there are 100 elements, approximately 100 iterations.
for num in numbers:
    print(num)

## O(n²) — Quadratic time
#The inner loop runs for every iteration of the outer loop.
# For n = 5, there are 25 iterations. For n = 100, there are 10,000.

for i in range(5):
    for j in range(5):
        print(i,j)

## O(log n) — Logarithmic time

# Imagine searching for a number in a sorted list. 
# Instead of checking every element, you repeatedly divide the search area into half.
# Example..we have 16 elements. Four halvings: log₂(16) = 4. That's why binary search is O(log n).


## O(n log n) — Linearithmic time

# This is common in efficient sorting algorithms such as merge sort. 
# The algorithm divides data into smaller parts and processes all elements across approximately log n levels.

## Space complexity measures how the extra memory used by an algorithm grows.
def print_numbers(numbers):
    for n in numbers:
        print(n) 


      #  or

def copy_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n)
    return result

# Searching means finding whether a particular value exists in a collection, and possibly finding its index."""
# Linear search checks elements one by one, from beginning to end.
# Binary search is faster for large datasets, but it requires the list to be sorted.

"""How it works:
Go through the array value by value from the start.
Compare each value to check if it is equal to the value we are looking for.
If the value is found, return the index of that value.
If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
"""

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
  print("Found!") # check a value if it exists
else:
  print("Not found!")

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:  # index of a value in a list
      return i
  return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)  # time complexity for Linear Search is: O(n)
else:
  print("Not found")

""" 
To implement the Linear Search algorithm we need:

An array with values to search through.
A target value to search for.
A loop that goes through the array from start to end.
An if-statement that compares the current value with the target value, and returns the current index if the target value is found.
After the loop, return -1, because at this point we know the target value has not been found.s
"""

# The Binary Search algorithm searches through a sorted array and returns the index of the value it searches for.
"""
How it works:

Check the value in the center of the array.
If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
If the value is found, return the target value index. If the target value is not found, return -1.

To implement the Binary Search algorithm we need:

An array with values to search through.
A target value to search for.
A loop that runs as long as left index is less than, or equal to, the right index.
An if-statement that compares the middle value with the target value, and returns the index if the target value is found.
An if-statement that checks if the target value is less than, or larger than, the middle value, and updates the "left" or "right" variables to narrow down the search area.
After the loop, return -1, because at this point we know the target value has not been found.

"""
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1
# binary search algorithm
  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1
# Time complexity for Binary Search is: O(log2n)
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")
### Understand built-in sorting and the basic idea of bubble/selection sort (conceptual, not memorisation)
## Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
"""
How it works:
Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.

To implement the Bubble Sort algorithm in Python, we need:
An array with values to sort.
An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.
"""
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
#time complexity for Bubble Sort is: O(n2)
print(mylist)

# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
"""
How it works:
Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.

To implement the Selection Sort algorithm in Python, we need:
An array with values to sort.
An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
An outer loop that controls how many times the inner loop must run. For an array with 
n values, this outer loop must run 
n-1 times.
"""

mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  min_value = mylist.pop(min_index)
  mylist.insert(i, min_value)
# time complexity: = O(n2)
print(mylist)

## The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

"""
Divide: The algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only consists of one element.
Conquer: The algorithm merges the small pieces of the array back together by putting the lowest values first, resulting in a sorted array.
The breaking down and building up of the array to sort the array is done recursively.

How it works:
Divide the unsorted array into two sub-arrays, half the size of the original.
Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
Merge two sub-arrays together by always putting the lowest value first.
Keep merging until there are no sub-arrays left.

To implement the Merge Sort algorithm we need:
An array with values that needs to be sorted.
A function that takes an array, splits it in two, and calls itself with each half of that array so that the arrays are split again and again recursively, until a sub-array only consist of one value.
Another function that merges the sub-arrays back together in a sorted way.
"""
# Merge Sort algorithm
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)


#MERGE SORT WITHOUT RECURSION
def merge(left, right):
  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

def mergeSort(arr):
  step = 1 # Starting with sub-arrays of length 1
  length = len(arr)

  while step < length:
    for i in range(0, length, 2 * step):
      left = arr[i:i + step]
      right = arr[i + step:i + 2 * step]

      merged = merge(left, right)

      # Place the merged array back into the original array
      for j, val in enumerate(merged):
        arr[i + j] = val

    step *= 2 # Double the sub-array length for the next iteration

  return arr

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print(mysortedlist)

# The time complexity for Merge Sort is: O(n⋅logn)
