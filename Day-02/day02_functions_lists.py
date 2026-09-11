# DAY 2 — Python

## Topics Covered

* `continue` in `for` loops
* Functions with `def`
* Parameters
* `print()` vs `return`
* `if / elif / else` inside functions
* Simple calculator function
* Lists
* `append()`
* `remove()`
* Looping through lists
* Loop variable vs whole list
* Running totals and counters
* Student Marks Analyzer mini-project

## My Original Code

### 1. `continue` — Skip 6

```python
for i in range (2,9):

    if i==6:

        continue

    print(i)
```

### 2. `continue` — Skip 5

```python
for i in range (1,11):

    if i==5:

        continue

    print(i)
```

### 3. Print odd numbers using `continue`

```python
for i in range (1,20):

    if i%2==0:

        continue

    print(i)
```

### 4. Function — Square

```python
def square(num):

    print(num ** 2)

square(2)

square(5)
```

### 5. Function — Addition

```python
def add(num1,num2):

    print(num1 + num2)

add(2,3)

add(4,1)
```

### 6. Function with `return` — Subtraction

```python
def subtract(a,b):

    return(a-b)

answer = subtract(10,4)

print(answer)
```

### 7. Function — Check age

```python
def check_age(age):

    if age > 17:

        return "Adult"

    else:

        return "Minor"

result = check_age(21)

print(result)
```

### 8. Function — Check positive/negative/zero

```python
def check_num(num):

    if num > 0:

        return "positive"

    elif num < 0:

        return"negative"

    else:

        return "zero"

result= check_num(-2)

print(result)
```

### 9. Calculator function

```python
def calculator(a,b,operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    else:
        return "?"
result = calculator(5,6,"/")
print(result)
```

### 10. Improved calculator

```python
def calculator(a,b,operation):
    if operation == "+":
        return a+b
    elif operation == "%":
        return a%b
    elif operation == "*":
        return a*b
    elif operation == "/":
        if b == 0:
            return "cannot devide by zero"
        return a//b
    else:
        return "?"
print(calculator(10,2,"/"))
print(calculator(10,0,"/"))
print(calculator(10,2,"%"))
```

### 11. List — `append()`

```python
language=["python", "java"]

language.append("c++")

language.append("JsvaScript")

print(language)
```

### 12. List — `remove()` and `append()`

```python
foods=["Pizza","Burger", "pasta","Dosa"]

foods.remove("Burger")

foods.append("Biriyani")

print(foods)
```

### 13. Loop through a list

```python
nums=[5,10,15,20]

for num in nums:

    print(num+5)
```

### 14. Even numbers — first incorrect version

```python
nums=[3,8,11,14,17,20]

for num in nums:

    if num%2==0:

        print(nums)
```

**Mistake:** `nums` prints the entire list instead of the current `num`.

### 15. Even numbers — incorrect version

```python
nums=[4,7,10,13,16,19,22]

for num in nums:

    if num%2==0:

        return num = num + 1
```

### 16. Sum of even numbers — incorrect version

```python
nums=[4,7,10,13,16,19,22]

total=0

for num in nums:

    if num%2==0:

        return total += num 

print (total)
```

### 17. Sum of odd numbers — corrected

```python
nums=[2,5,8,11,14,17]

total=0

for num in nums:

    if num%2==1:

        total += num 

print (total)
```

## 18. Final Day 2 Mini-Project — Student Marks Analyzer

```python
marks=[78,45,89,32,67,91,55]

total=0

passed=0

failed=0

for mark in marks:

    total+= mark

    if mark >= 40:

        passed += 1

    else:

        failed+= 1

print("Total:",total)

print("Passed:", passed)

print("Failed:", failed)
```

**Day 2 completed successfully.**
