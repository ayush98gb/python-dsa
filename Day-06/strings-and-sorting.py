# Day 6 - Python + DSA


# =========================
# Python - Strings
# =========================


# String Indexing


word = "MIKASA"

print(word[0])
print(word[2])
print(word[4])


# Looping Through Strings

word = "MIKASA"

for x in word:
    print(x)


# Count Character

word = "BANANA"
target = "A"
count = 0

for x in word:
    if x == target:
        count += 1

print(count)


# Count Vowels and Consonants

word = "MIKASA"
vowels = "AEIOU"

vowels_count = 0
consonants_count = 0

for x in word:
    if x in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print("vowels:", vowels_count)
print("consonants:", consonants_count)


# Reverse a String

word = "MIKASA"
reverse = ""

for x in word:
    reverse = x + reverse

print(reverse)


# Case-Insensitive Character Counting

word = "BANaNa"
target = "a"
count = 0

for x in word:
    if target.lower() == x.lower():
        count += 1

print(count)


# Count Words

sentence = "i love learning python"

words = 1

for x in sentence:
    if x == " ":
        words += 1

print(words)


# Python sort()

nums = [5, 2, 8, 1]

nums.sort()

print(nums)


# Python sorted()

nums = [5, 2, 8, 1]

new_nums = sorted(nums)

print(nums)
print(new_nums)


# =========================
# DSA - Strings
# =========================


# Linear Search in String

word = "MIKASA"
target = "S"

for i in range(len(word)):
    if word[i] == target:
        print("found at index:", i)


# Find All Occurrences

word = "BANANA"
target = "A"

for i in range(len(word)):
    if word[i] == target:
        print("found at index:", i)


# Search and Handle Not Found

word = "BANANA"
target = "z"
count = 0

for i in range(len(word)):
    if word[i] == target:
        print("found at index:", i)
        count += 1

if count == 0:
    print("not found")


# Palindrome Check

word = "PYTHON"
reverse = ""

for x in word:
    reverse = x + reverse

print(reverse)

if reverse == word:
    print("palindrome")
else:
    print("non palindrome")


# =========================
# DSA Day 4 - Sorting Algorithms
# =========================


# Bubble Sort - Ascending

nums = [7, 3, 9, 2, 5]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


# Bubble Sort - Descending

nums = [7, 3, 9, 2, 5]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


# Selection Sort

nums = [7, 4, 9, 2, 5]

for i in range(len(nums)):
    min_index = i

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]

print(nums)


# Insertion Sort

nums = [7, 3, 9, 2, 5]

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

print(nums)


# Selection Sort + Linear Search

nums = [12, 5, 8, 3, 15, 7]
target = 8

for i in range(len(nums)):
    min_index = i

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]

for i in range(len(nums)):
    if nums[i] == target:
        print("Index:", i)

print("Sorted:", nums)