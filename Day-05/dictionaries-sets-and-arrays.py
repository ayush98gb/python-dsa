# Python - Dictionaries and Sets


# Create dictionary

students = {
    "Ayush": "python",
    "Rahul": "java",
    "Ravi": "python",
    "Aman": "cloud",
    "Neha": "java",
    "Priya": "dsa"
}


# Access dictionary values

print(students["Ayush"])


# Add and update dictionary values

students["Kiran"] = "dbms"
students["Ayush"] = "dsa"

print(students)


# Dictionary - Count Frequency

nums = [10, 20, 10]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)


# Calculate total, average, highest, highest subject, passed and failed

marks = {
    "python": 78,
    "dsa": 32,
    "dbms": 65,
    "os": 28,
    "network": 81
}

total = 0
count = 0
high = 0
high_sub = ""
passed = 0
failed = 0

for subject, mark in marks.items():
    if mark > 0:
        total += mark
        count += 1

    if mark > high:
        high = mark
        high_sub = subject

    if mark >= 40:
        passed += 1
    else:
        failed += 1

avg = total / count

print("Total:", total)
print("Average:", avg)
print("Highest:", high)
print("Highest subject:", high_sub)
print("Passed:", passed)
print("Failed:", failed)


# Sets

ayush = {"python", "dsa", "dbms", "cloud"}
rahul = {"python", "java", "dbms", "network"}


# Intersection

common = ayush & rahul


# Union

all_courses = ayush | rahul


# Difference

only_ayush = ayush - rahul
only_rahul = rahul - ayush

print("Common:", common)
print("All:", all_courses)
print("Only Ayush:", only_ayush)
print("Only Rahul:", only_rahul)


# Sets - Remove Duplicates

nums = [2, 5, 2, 8, 5, 10, 12, 2]

unique = set()

for num in nums:
    unique.add(num)

print(unique)


# Dictionary + Set - Unique Courses

students = {
    "Ayush": "python",
    "Rahul": "java",
    "Ravi": "python",
    "Aman": "cloud",
    "Neha": "java",
    "Priya": "dsa"
}

courses = set()

for name, course in students.items():
    courses.add(course)

print(courses)


# =========================
# DSA Day 2 - Arrays
# =========================


# Arrays - Linear Search

nums = [8, 3, 15, 6, 12, 20]

target = 15

found = False

for i in range(len(nums)):
    if nums[i] == target:
        print("found at index:", i)
        found = True
        break

if found == False:
    print("not found")


# Arrays - Find Largest

nums = [23, 8, 41, 16, 35, 12]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print(largest)


# Arrays - Find Smallest

nums = [32, 17, 45, 6, 28, 11]

low = nums[0]

for num in nums:
    if num < low:
        low = num

print(low)


# Arrays - Find Largest and Smallest

nums = [42, 15, 67, 3, 29, 81, 11]

high = nums[0]
low = nums[0]

for num in nums:
    if num > high:
        high = num

    if num < low:
        low = num

print(high)
print(low)


# Arrays - Count Occurrences

nums = [2, 5, 2, 8, 2, 9, 5, 2]

target = 2

count = 0

for num in nums:
    if num == target:
        count += 1

print(count)


# Arrays - Sum

nums = [5, 10, 15, 20, 25]

total = 0

for num in nums:
    total += num

print(total)


# Arrays - Reverse Using Two Pointers

nums = [10, 20, 30, 40, 50, 60]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1

print(nums)