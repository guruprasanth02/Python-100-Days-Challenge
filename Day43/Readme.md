# 🌟 Day 43: 2D Lists and Bingo Card Challenge 🎲

### 🎊 Today’s Highlights:

* **Exploring 2D Lists:** We delved into two-dimensional lists, learning how to organize data in rows and columns, much like a table. This is ideal for structuring multiple related data points, like records in a database.
* **Working with Data in Rows and Columns:** We accessed specific rows and columns using index numbers, which helped us manipulate data in a structured way. This is crucial for real-life applications where data comes in a tabular format.
* **Editing Data in 2D Lists:** We also practiced updating individual elements within the lists, allowing us to modify values as needed, which mimics how real-world data might be updated in a system.
* **Bingo Card Creation Challenge:** We applied our knowledge of 2D lists by creating a bingo card, learning how to generate random numbers, and properly organizing them in a 2D list format while ensuring the center square remains empty.

### 🔍 Key Concepts:

* **2D Lists:** A 2D list is a list of lists, where each sublist can hold multiple elements. The structure allows us to store and access data in both dimensions—rows and columns.
     * Example:
        ```python
        my2DList = [["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"]]

* **Accessing Data in 2D Lists:** To access a specific element, we use two indices: one for the row and one for the column.
     * Example: ```my2DList[0][1]``` retrieves the value ```21``` (the age of "Johnny").

* **Bingo Card Challenge:**
    * **Random Number Generation:** We created a list of numbers between 0 and 90, ensuring each number was unique.
    * **Placement in the Bingo Card:** We allocated numbers into a 5x5 2D list, ensuring numbers are sorted and placed sequentially in each row.
    * **Center Square:** The center square should always contain the word "BINGO!" instead of a number.

### 👉 Day 43 Challenge: Bingo Card Task Overview:
Write a program that:

1. Randomly generates a series of numbers between 0 and 90 (no duplicates).
2. Allocates each number to a place in a 5x5 bingo card (in numerical order).
3. Ensures the center square contains the word "BINGO!".
4. Outputs the bingo card to the screen in a table-like format.

### 🛠️ Common Errors Encountered:

* **Index Errors:** Attempting to access an element outside the bounds of the list (e.g., ```my2DList[0][3])``` results in an "index out of range" error. This can happen if you try to access a column that doesn’t exist in a given row.

    **Fix:** Always ensure you're referencing valid indices within the range of the list's size.

* **List Formatting Issues:** Forgetting to close the list or adding extra commas can cause syntax errors when creating or manipulating lists.

    **Fix:** Ensure that the syntax of the list is correct, especially when dealing with nested lists (2D).

* **Random Number Duplication:** Randomly generating numbers without ensuring they are unique can cause repeated numbers on the bingo card.
    **Fix:** Use a set or check for duplicates before adding numbers to the list.

### My Code:
```python
import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()
