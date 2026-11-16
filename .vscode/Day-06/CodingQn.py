## Practice: compare one loop vs nested loops; implement linear search and binary search.

# linear search which returns index of target
def linear_search(numbers,target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
numbers = [12, 5, 8, 20, 15]
target = 20
print(linear_search(numbers, target))

# binary search 
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

numbers = [10, 20, 30, 40, 50, 60, 70]
target = 30
print(binary_search(numbers, target))

# one loop vs nested loops practice
# One loop — O(n)
numbers = [50,40,30,20,10]
for n in range(2):
    print(numbers)

# Nested loops — O(n²)

numbers = [10,20,30,40,50]
for i in numbers:
    for j in numbers:
        print(i,j)
