# Continue in For Loops

for i in range(2, 9):
    if i == 6:
        continue
    print(i)


for i in range(1, 11):
    if i == 5:
        continue
    print(i)


for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)


# Functions

def square(num):
    print(num ** 2)


square(2)
square(5)


def add(num1, num2):
    print(num1 + num2)


add(2, 3)
add(4, 1)


def subtract(a, b):
    return a - b


answer = subtract(10, 4)

print(answer)


# Check Age

def check_age(age):
    if age > 17:
        return "Adult"
    else:
        return "Minor"


result = check_age(21)

print(result)


# Check Number

def check_num(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


result = check_num(-2)

print(result)


# Calculator

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "%":
        return a % b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "cannot divide by zero"
        return a // b
    else:
        return "?"


print(calculator(10, 2, "/"))
print(calculator(10, 0, "/"))
print(calculator(10, 2, "%"))


# Lists

language = ["python", "java"]

language.append("c++")
language.append("JsvaScript")

print(language)


foods = ["Pizza", "Burger", "pasta", "Dosa"]

foods.remove("Burger")
foods.append("Biriyani")

print(foods)


nums = [5, 10, 15, 20]

for num in nums:
    print(num + 5)


# Sum of Odd Numbers

nums = [2, 5, 8, 11, 14, 17]

total = 0

for num in nums:
    if num % 2 == 1:
        total += num

print(total)


# Student Marks Analyzer

marks = [78, 45, 89, 32, 67, 91, 55]

total = 0
passed = 0
failed = 0

for mark in marks:
    total += mark

    if mark >= 40:
        passed += 1
    else:
        failed += 1

print("Total:", total)
print("Passed:", passed)
print("Failed:", failed)