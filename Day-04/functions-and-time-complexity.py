# Day 4 - Python + DSA


# =========================
# Python - Functions
# =========================

def square(num):
    return num * num


print(square(5))


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(10))


def largest(a, b):
    if a > b:
        return a
    else:
        return b


print(largest(20, 15))


def smallest(a, b):
    if a < b:
        return a
    else:
        return b


print(smallest(10, 25))


def count_numbers(nums):
    count = 0

    for num in nums:
        count += 1

    return count


print(count_numbers([10, 20, 30, 40]))


def sum_numbers(nums):
    total = 0

    for num in nums:
        total += num

    return total


print(sum_numbers([10, 20, 30, 40]))


def reverse_list(nums):
    reversed_nums = []

    i = len(nums) - 1

    while i >= 0:
        reversed_nums.append(nums[i])
        i -= 1

    return reversed_nums


print(reverse_list([10, 20, 30, 40]))


# =========================
# DSA Day 1 - Time Complexity
# =========================

marks = [78, 35, 92, 41, 27, 85, 60]


# O(1) - Constant Time

print(marks[0])


# O(n) - Linear Time

for mark in marks:
    print(mark)


# O(n^2) - Quadratic Time

for a in marks:
    for b in marks:
        print(a, b)


# O(n) - Multiple Separate Loops

for num in marks:
    print(num)

for num in marks:
    print(num)


# O(n) - Linear Search / Traversal

high = marks[0]

for num in marks:
    if num > high:
        high = num

print(high)