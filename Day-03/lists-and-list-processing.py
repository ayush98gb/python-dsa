# Lists and Basic Calculations

marks = [78, 35, 92, 41, 27, 85, 60]

total = 0
avg = 0
high = marks[0]
low = marks[0]
passed = []
failed = []

for mark in marks:
    total += mark

    if high < mark:
        high = mark

    if low > mark:
        low = mark

    if mark >= 40:
        passed.append(mark)
    else:
        failed.append(mark)

avg = total / len(marks)

print("total:", total)
print("avg:", avg)
print("highest:", high)
print("lowest:", low)
print("passed:", passed)
print("failed:", failed)


# Counting Values

nums = [3, 8, 12, 7, 10]

count = 0

for num in nums:
    if num > 7:
        count += 1

print(count)


# Total of Values Greater Than 7

nums = [4, 9, 6, 11, 8]

total = 0

for num in nums:
    if num > 7:
        total += num

print(total)


# Total and Count of Values Greater Than or Equal to 10

nums = [5, 12, 7, 18, 3, 10]

total = 0
count = 0

for num in nums:
    if num >= 10:
        total += num
        count += 1

print("Total:", total)
print("Count:", count)


# Finding Highest Value

marks = [67, 82, 45, 91, 73, 88]

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print(highest)


# Finding Lowest Value

marks = [67, 82, 45, 91, 73, 88]

lowest = marks[0]

for mark in marks:
    if mark < lowest:
        lowest = mark

print("Lowest=", lowest)


# Total and Average

marks = [60, 70, 80, 90, 100]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print(total)
print(average)


# Above and Below Average

marks = [78, 45, 89, 32, 67, 91, 55]

total = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / len(marks)

above_avg = 0
below_avg = 0

for mark in marks:
    if mark > average:
        above_avg += 1

    if mark < average:
        below_avg += 1

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Above avg:", above_avg)
print("Below avg:", below_avg)


# List Indexing

nums = [10, 20, 30, 40, 50]

print(nums[2])
print(nums[-1])


# Name List Indexing

names = ["Aman", "Rahul", "Priya", "Neha", "Arjun"]

print(names[1])
print(names[-2])


# Changing List Values

scores = [45, 67, 32, 89, 56]

scores[2] = 72
scores[-1] = 96

print(scores)


# Appending Items

fruits = ["apple", "banana", "mango"]

fruits.append("orange")
fruits.append("grapes")

print(fruits)


# Filtering a List

marks = [78, 32, 65, 91, 27, 54, 88]

passed = []

for mark in marks:
    if mark >= 40:
        passed.append(mark)

print(passed)


# Passed and Failed Lists

marks = [78, 32, 65, 91, 27, 54, 88]

passed = []
failed = []

for mark in marks:
    if mark >= 40:
        passed.append(mark)
    else:
        failed.append(mark)

print(passed)
print(failed)


# Even and Odd Lists

nums = [3, 8, 11, 14, 17, 20, 25, 28]

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)


# Accessing List Items Using Indexes

names = ["Aman", "Rahul", "Priya"]

for i in range(len(names)):
    print(i, names[i])


# Modifying List Items Using Indexes

scores = [50, 60, 70, 80]

for i in range(len(scores)):
    scores[i] = scores[i] + 5

print(scores)


# Increasing Prices by 10 Percent

prices = [100, 250, 400, 150]

for i in range(len(prices)):
    prices[i] = prices[i] + (prices[i] * 10 / 100)

print(prices)


# While Loop with a List

names = ["Aman", "Priya", "Rahul", "Neha"]

i = 0

while i < len(names):
    print(names[i])
    i += 1


# Total Using While Loop

nums = [5, 10, 15, 20, 25]

i = 0
total = 0

while i < len(nums):
    total += nums[i]
    i += 1

print(total)


# Filtering with While Loop

marks = [25, 67, 31, 80, 42, 19]

i = 0

while i < len(marks):
    if marks[i] >= 40:
        print(marks[i])
    i += 1