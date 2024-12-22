# 🌟 Day 57: Factorial Finder Using Recursion 🔢🔄

### 🎊 Today’s Highlights:

* **Recursion in Action:** We explored how recursion works by writing a function that calculates the factorial of a number.
* **Factorial Calculation:** We learned that the factorial of a number is the product of all integers from 1 to that number. Using recursion, we can break this problem down by multiplying a number with the factorial of the number minus one, until we reach 1.
* **Base Case in Recursion:** We implemented a base case to stop the recursion once we reach 1, returning 1 to terminate the process.

### 🔍 Key Concepts:

* **Recursion:** Recursion allows a function to call itself with a reduced problem size until a base case is met, making it perfect for problems like factorial calculation.
* **Base Case:** This is the condition where the recursion stops. For the factorial problem, the base case is when the input number is 1, returning 1.
* **Recursive Function Structure:** The function calls itself with a decremented value, reducing the problem step by step until the base case is met.
* **Multiplication in Recursion:** The function multiplies the number by the factorial of the number minus one, building up the result as the recursion unwinds.

### 👉 Day 57 Challenge: Factorial Program Overview:

**Write a function to calculate the factorial of a number using recursion.**

The program should:

   1. Start with the given number.
   2. Multiply the number by the factorial of itself minus one.
   3. Return 1 when the number reaches 1 (base case).
   4. Output the calculated factorial.

**Example:**
```python
Input: 5
Output: The factorial of 5 is 120.
```

### 🛠️ Common Errors Encountered:

* **Missing Base Case:** If the base case (when the number reaches 1) is forgotten, the function will call itself indefinitely, causing a stack overflow error.

  * **Fix:** Ensure that the base case (if ```value <= 0```) is in place to terminate the recursion.

* **Incorrect Recursive Call:** If the function doesn't correctly reduce the input number in each recursive call, the recursion won't progress towards the base case.

  * **Fix:** Make sure the function calls itself with a reduced value, typically by subtracting 1 or more.

* **Incorrect Return Value:** If you forget to return the result in each recursive call, the factorial won't be calculated correctly.

  * **Fix:** Make sure the function returns the value after multiplying it with the recursive result.

### My Code:
```python
def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)

print(factorial(5))
