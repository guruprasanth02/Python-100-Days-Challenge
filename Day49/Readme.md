# ✨ Day 49: File Reading and High Score Analysis 📃🏆

### 🎉 Today’s Highlights:

1. **Reading Data from Files:**

     * Learned how to read data stored in files using Python.

     * Explored various methods like ```.read()```, ```.readline()```, and ```.readlines()``` to access file contents.

2. **Splitting Data:**

     * Utilized ```.split()``` to break file content into manageable parts (e.g., converting text into a list).

     * Applied ```.strip()``` to clean up extra spaces and newline characters.

3. **Looping Through File Data:**

     * Used loops to read and process file content line by line efficiently.

4. **Debugging Common Errors:**

     * Resolved issues like infinite loops, blank outputs, and unclosed files.

### 🔍 Key Concepts:

* **File Reading Modes:**

     * ```r```: Opens the file in read-only mode.

* **Reading Methods:**

     * ```.read()```: Reads the entire file content as a single string.

     * ```.readline()```: Reads one line at a time, useful for sequential processing.

     * ```.readlines()```: Reads all lines into a list for easier manipulation.

* **File Iteration:**

     * Used ```while``` and ```for``` loops to iterate through file contents dynamically.

### 🌟 Day 49 Challenge: High Score Analysis

**Task Overview:**

  1. Read the contents of the ```high.score``` file.

  2. Process the data to find the user with the highest score.

  3. Output the initials and score of the top performer.

**Steps to Solve:**

  1. Open the file in read mode ```(r)```.

  2. Read all lines and split each line into initials and score.

  3. Convert the score to an integer for comparison.

  4. Identify the highest score and corresponding initials.

Print the result.

### 🌸 Common Errors Encountered:

* **File Not Found Error:**

    * Ensure the ```high.score``` file exists in the working directory.

* **Blank Line Issue:**

    * Resolved by checking if a line is empty before processing it.

* **ValueError (Splitting Issues):**

    * Fixed by ensuring each line contains both initials and score.

### 🔢 My Code Examples:
```python
import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)
