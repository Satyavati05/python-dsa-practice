
# Learn left/right pointers and when pointers move inward or forward.
# Practice palindrome check, reverse vowels or reverse string, valid palindrome (basic version).
# Compare a simple nested-loop solution with a two-pointer solution.
# For every solution, state the invariant: what do the pointers represent?
# Checkpoint: explain why the pointers move and prove that no needed candidate is skipped.

"""

A pointer is simply a variable that stores an index or position in a string or array.

There are two common ways to use pointers: 

Pattern A: Pointers move inward
- left starts at index 0.
- right starts at the last index.
- They move towards each other.
Used for:
- Palindrome checking
- Reversing a string
- Reversing vowels

Pattern B: Pointers move forward
Both pointers move from left to right, sometimes at different speeds or for different purposes.
Used for:
- Removing duplicates from sorted arrays
- Moving zeroes
- Merging sorted arrays

In palindrome check... the approach is
For "madam":
- Compare the first and last characters.
- If they match, move both pointers inward.
- Continue until the pointers meet or cross.
- If any pair doesn't match, it isn't a palindrome.

"""
# palindrome check..A palindrome reads the same forward and backward.
def check_palindrome(str):
    left = 0
    right = len(str)-1
    while left<right:# compare the indexes
        if str[left]!=str[right]:
            return False
        left +=1 
        right-=1
    return True
print(check_palindrome("madam"))


#  reverse vowels or reverse string,
def revString(str):
    ch = list(str)
    left = 0
    right = len(str)-1
    while left<right:
        ch[left],ch[right] = ch[right],ch[left] #swap the character
        left+=1 # left going forward
        right-=1 # right going backward
    return "".join(ch)
print(revString("Satyavati"))


# valid palindrome (basic version)
# Given a string s, check whether it is a palindrome. Ignore spaces and differences between uppercase and lowercase letters.
def is_palindrome(str):
    str = str.lower()
    str = str.replace(" ", "")

    left = 0
    right = len(str)-1
    str.lower()
    while left<right:
        if str[left] != str[right]:
            return False
        left +=1
        right -=1

    return True
print(is_palindrome("MADAM"))
print(is_palindrome("hello")) 

# Simple nested-loop approach
# One way to check a palindrome is to compare the string with its reverse. But imagine we want to check matching characters using loops.We can compare every character with every possible character to find its matching position from the opposite end.
# Outer loop selects a character.Inner loop searches for its corresponding opposite position.We compare characters when their indexes add up to n - 1.
def nestedPalindrome(str):
    n = len(str)
    for i in range(n):
        for j in range(n):
            if i+j == n-1:
                if str[i] != str[j]:
                    return False
    return True
print(nestedPalindrome("Satya"))# O(n²), because there are two nested loops.
print(nestedPalindrome("level"))

# Two-pointer approach. Instead of searching for matching positions, we already know where the comparison should happen.
def twoPointerPalindrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False

        left += 1
        right -= 1

    return True
print(twoPointerPalindrome("121"))
print(twoPointerPalindrome("nath"))

"""
An invariant is something that remains true throughout an algorithm.

In a two-pointer problem, it means explaining:
In a two-pointer problem, it means explaining:
- What does the left pointer represent?
- What does the right pointer represent?
- What have we already checked or accomplished as the pointers move?
Think of it as explaining the responsibility of each pointer.

For Palindrome
The invariant is:
Every character pair outside the current range between left and right has already been checked and found equal.

In simpler words:
- left represents the character we're checking from the beginning.
- right represents the character we're checking from the end.
- Everything we've already crossed has matched.

For reversing "hello":
- left points to the position where the character from the right should go.
- right points to the position where the character from the left should go.
- After swapping, the characters outside the current range are already in their correct reversed positions.
"""