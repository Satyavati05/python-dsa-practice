# Student Result Calculator

"""def calculate_total(marks):
    return sum(marks)   # calculate total

def calculate_average(total, subjects):
    return total / subjects  # calculate average

def check_result(average):
    if average >= 40:  # calculate result
        return "Pass"
    else:
        return "Fail"

def student_result(marks):  # main function
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    return total, average, result


marks = [75, 80, 65, 90, 70]

total, average, result = student_result(marks)

print("Total:", total)
print("Average:", average)
print("Result:", result)

# Employee Salary Calculator
def calculate_bonus(salary):
    bonus = salary * 0.10
    return bonus
    
def calculate_final_salary(salary,bonus):
    final_salary = salary + bonus
    return final_salary


def salary_details(salary):
    bonus = calculate_bonus(salary)
    final_salary = calculate_final_salary(salary, bonus)

    return bonus, final_salary

bonus, final_salary = salary_details(50000)

print("Bonus:", bonus)
print("Final Salary:", final_salary)

 # 1st coding problem: Factorial using recursion
def fact(n):
    if n == 0 or n ==1:  # base case
        return 1
    return n*fact(n-1)
print(fact(7))   # recursive call

# Sum of first n natural numbers
def sum_n(n):
    if n == 0:  # base case
        return 0
    return n + sum_n(n - 1)
print(sum_n(5))   # recursive call """

###DSA PRACTICE
#Function-based: Find the largest element
def largest_number(num):
    largest = num[0]
    for n in num:
        if largest < n:
            largest = n
    return largest
# Complexity:
# Time: O(n) — visits each element.
# Auxiliary space: O(1) — uses only one extra variable.
numbers = [12, 45, 7, 89, 23]
print(largest_number(numbers))


# Function based: Count even numbers
def count_even(numbers):
    count = 0
    for n in numbers:
        if n%2 == 0:
            count+=1  #Complexity: O(n) time and O(1) auxiliary space.
    return count
numbers = [12, 45, 7, 8, 23]
print(count_even(numbers))

# Simple recursion: Sum of natural numbers
def sum_natural(num):
    if num == 0:  # base case
        return 0
    return num + sum_natural(num-1)  # recursive call

print(sum_natural(5))
    
    

