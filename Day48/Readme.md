# ✨ Day 88: File Writing and High Score Table 📂🏆

### 🎉 Today’s Highlights:

1. **Understanding File Operations:**

      * Learned how to open, write, and append data to files using Python.

      * Explored the differences between file modes such as ```w``` (write) and ```a+``` (append and create if not existing).

2. **File Handling Commands:**

      * **Opening Files:** Using ```open("filename", "mode")``` to create or access files.

      * **Writing to Files:** The ```.write()``` method for saving data.

      * **Appending to Files:** Using ```a+``` mode to add data to the end of the file without overwriting.

      * **Closing Files:** Ensuring data is saved with the ```.close()``` method.

3. **String Formatting:**

      * Added new lines using ```\n``` for better readability in saved files.

      * Utilized f-strings to dynamically format text written to files.

3. **Error Fixing:**

      * Debugged common issues like file I/O errors and improper file handling.

### 🔍 Key Concepts:

* **Temporary vs. Permanent Storage:**
Variables and data structures use temporary RAM, which clears after program execution. File writing enables long-term storage in secondary memory.

* **File Modes:**

     * ```w````: Overwrites the file or creates a new one if it doesn’t exist.

     * ```a+```: Appends data to the file or creates a new one if it doesn’t exist.

* **Error Handling:**

     * Preventing crashes when a file doesn’t exist by using appropriate file modes.

     * Debugging issues like unclosed files or missing ```.close()``` calls.

### 🌟 Day 88 Challenge: High Score Table

**Task Overview:**

  1. Prompt the user for their initials and score.

  2. Save this information in a file called ```high.score```.

  3. Ensure the file uses append mode to avoid overwriting existing scores.

  4. Format each entry as ```initials score``` on a new line.

  5. Add a loop to allow multiple entries, stopping when the user chooses.

  6. Use a single input and the ```split()``` function for extra points.

### 🎡 Common Errors Encountered:

* **File Not Found Error:**

     * Fixed by using ```a+``` mode to create the file if it doesn’t exist.

* **Data Overwrite Issue:**

     * Resolved by switching from ```w``` mode to a+ mode.

* **Improper Formatting:**

     * Corrected by adding ```\n``` for new lines and using f-strings.

### 🔢 My Code Examples:
```python
import os, time

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  time.sleep(1)
  os.system("clear")
