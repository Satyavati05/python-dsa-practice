# Reverse a string
word = "python"
print(word[::-1])  # nohtyp


# Reverse a list
my_list = [1, 2, 3, 4, 5]
print(my_list[::-1])  # [5, 4, 3, 2, 1]

# Count vowels
word = "hello"
vowels = "aeiou"
count = sum(1 for char in word if char in vowels)
print(count)  # 2

#or
word = "education"
count = 0

for char in word:
    if char in "aeiou":
        count += 1

print(count)  # 5

# Find the largest and 2nd largest distinct values
numbers = [5, 2, 8, 1, 9, 3]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
print(unique_numbers[0])  # 9
print(unique_numbers[1])  # 8


# Remove duplicates
numbers = [1, 2, 2, 3, 1, 4]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)  # [1, 2, 3, 4]