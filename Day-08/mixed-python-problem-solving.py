
# Day 8 - Mixed Python Problem Solving

# =========================
# Lists + Loops + Conditions
# =========================

nums = [12, 5, 8, 15, 20, 3, 10]

for num in nums:
    if num > 10:
        print(num)


# =========================
# Counting Numbers Greater Than 10
# =========================

nums = [12, 5, 8, 15, 20, 3, 10, 25, 7]

count = 0

for num in nums:
    if num > 10:
        count += 1

print(count)


# =========================
# Finding the Largest Number
# =========================

nums = [12, 45, 7, 23, 89, 34]

high = nums[0]

for num in nums:
    if num >= high:
        high = num

print(high)


# =========================
# Finding the Smallest Number
# =========================

nums = [12, 45, 7, 23, 89, 34]

low = nums[0]

for num in nums:
    if num < low:
        low = num

print(low)


# =========================
# Counting Even and Odd Numbers
# =========================

nums = [12, 5, 8, 15, 20, 3, 10, 7]

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("even:", even)
print("odd:", odd)


# =========================
# Sum of Even Numbers
# =========================

nums = [12, 5, 8, 15, 20, 3, 10, 7]

total = 0
even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
        total += num
    else:
        odd += 1

print("even:", even)
print("odd:", odd)
print("total:", total)


# =========================
# Sum and Average
# =========================

nums = [12, 5, 8, 15, 20, 3, 10, 7]

total = 0
even = 0
odd = 0
count = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    total += num

count = even + odd
avg = total / count

print("even:", even)
print("odd:", odd)
print("total:", total)
print("average:", avg)


# =========================
# Positive, Negative, and Zero
# =========================

nums = [10, -5, 0, 8, -2, 15, 0, -7]

total = 0
even = 0
odd = 0
count = 0
positive = 0
negative = 0
zero = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    total += num

    if num == 0:
        zero += 1
    elif num > 0:
        positive += 1
    else:
        negative += 1

count = even + odd
avg = total / count

print("even:", even)
print("odd:", odd)
print("total:", total)
print("average:", avg)
print("positive:", positive)
print("negative:", negative)
print("zero:", zero)


# =========================
# Second Largest Number
# =========================

nums = [10, 25, 8, 40, 15, 30]

high = nums[0]
sec_high = nums[0]

for num in nums:
    if num > high:
        sec_high = high
        high = num
    elif num > sec_high:
        sec_high = num

print(sec_high)


# =========================
# Smallest, Second Smallest, Third Smallest
# =========================

nums = [15, 10, 8, 40, 1, 30]

low = float("inf")
sec_low = float("inf")
third_low = float("inf")

for num in nums:
    if num < low:
        third_low = sec_low
        sec_low = low
        low = num
    elif num < sec_low:
        third_low = sec_low
        sec_low = num
    elif num < third_low:
        third_low = num

print(low)
print(sec_low)
print(third_low)


# =========================
# Removing Duplicates from a List
# =========================

nums = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)


# =========================
# Dictionary Frequency Counting
# =========================

nums = [10, 20, 10, 30, 20, 40, 10, 30]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)