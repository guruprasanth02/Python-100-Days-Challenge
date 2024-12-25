# 🌟 Day 59: Palindrome Checker Using Recursion, Slicing, and Loops 🔄🔠

### 🎊 Today’s Highlights:

* **Introduction to Palindromes:** We learned about palindromes, which are words that read the same forward and backward. Examples include "racecar," "madam," and "radar."
* **Building a Palindrome Checker:** We applied our knowledge of recursion, string slicing, and loops to write a program that checks if a word is a palindrome.
* **Recursion and Slicing:** We avoided using Python’s built-in ```reverse()``` function and instead focused on solving the problem using fundamental concepts like recursion and string manipulation.

### 🔍 Key Concepts:

* **Palindrome:** A word that is the same when read forwards and backwards. Examples include "level" or "radar."
* **Recursion:** A technique where a function calls itself to solve smaller instances of the problem. In this case, we used recursion to check if characters match when traversing from the outside inward.
* **String Slicing:** This allows you to extract a portion of a string. We used slicing to check the characters at the start and end of the string.
* **Loops:** We used loops to iterate through the string or to compare parts of the string to determine if it is a palindrome.

### 👉 Day 59 Challenge: Palindrome Checker Program:

**Task Overview:**

  * Write a program that prompts the user to input a word.
  * The program checks if the word is a palindrome using recursion, string slicing, or looping techniques.
  * It outputs a message confirming whether the word is a palindrome or not.

**Example:**

  * **Input:** ```Racecar```
  * **Output:** ```Racecar is a palindrome. Yay!```

### 🛠️ Common Errors Encountered:

* **Case Sensitivity:** A common issue when checking for palindromes is that words like "Racecar" and "racecar" are the same, but their capitalization may cause incorrect results.

  * **Fix:** Convert the input to lowercase to ensure case insensitivity by using ```word.lower()``` before performing the palindrome check.

* **String Indexing Mistakes:** Improper use of string slicing or recursion can lead to incorrect comparisons. It’s important to compare the correct characters (e.g., first with last).

  * **Fix:** Ensure that in recursion or loops, the correct characters are being checked by slicing the string from both ends.

### My Code:
```python
def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

print(palindrome("malayalam"))
