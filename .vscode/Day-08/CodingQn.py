"""3Sum...Two pointers + Sorting
 Given an integer array arr, find all unique triplets [arr[i], arr[j], arr[k]] such that:
1. i != j, j != k, and i != k.
2. arr[i] + arr[j] + arr[k] == 0.
3. The answer must not contain duplicate triplets.

The fundamental rule
Think of it this way:
- Negative sum: We need a bigger number → move left right.
- Positive sum: We need a smaller number → move right left.
- Zero sum: We found our triplet!
"""
def threeSum(arr):
    arr.sort()
    result = []
    for i in range(len(arr)):
        left = i+1
        right = len(arr)-1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                result.append([arr[i], arr[left], arr[right]])

                left += 1
                right -= 1

            elif total < 0:
                left +=1
            else:
                right -=1
        return result
arr = [1,-1,0,2,3,-4]
print(threeSum(arr)) # O(n2)

"""
Container With Most Water...Two Pointer
Problem statement
You are given an integer array height of length n.

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

Return the maximum amount of water the container can store.

ind two lines that can hold the maximum amount of water.

Formula:
\[
Area=(right-left)\times min(height[left],height[right])
\]

"""

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left # calculate the width

        min_height = min(height[left], height[right]) # calculate the min_height

        area = width * min_height # calculate the area

        max_area = max(max_area, area) # calculate the max_area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1


    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 10 ]
print(maxArea(height))


        