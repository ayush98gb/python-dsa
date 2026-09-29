
# Day 7 - Python

# =========================
# Tuples
# =========================

nums = (10, 20, 30, 40)

print(nums[2])


# =========================
# Sets - Remove Duplicates
# =========================

nums = [10, 20, 10, 30, 20, 40, 30]

unique = set(nums)

print(unique)
print(len(unique))


# =========================
# Sets - Intersection
# =========================

python = {"Ayush", "Rahul", "Ravi"}
dsa = {"Ayush", "Ravi", "Aman"}

print(python & dsa)


# =========================
# Sets - Difference
# =========================

print(python - dsa)


# =========================
# Lists - Remove Duplicates Without Using set()
# =========================

nums = [5, 2, 8, 5, 2, 9, 8, 5]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)


# =========================
# Lists - Common Elements
# =========================

a = [10, 20, 30, 40, 50]
b = [30, 40, 50, 60, 70]

x = []

for num in a:
    if num in b:
        x.append(num)

print(x)


# =========================
# Dictionaries - Frequency Counting
# =========================

nums = [10, 20, 10, 30, 40, 20, 50, 30]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)