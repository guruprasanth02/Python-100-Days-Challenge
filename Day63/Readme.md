# 🌟 Day 63: Become Your Own Librarian – Organizing Subroutines into Libraries 📚

### 🎊 Today’s Highlights:

* **The Power of Code Reusability:** Today, we focused on organizing our Python code into libraries, making it more modular and easier to manage. Instead of having all our code in a single file, we split it into separate files and imported them where necessary.
* **Splitting Code into Multiple Files:** We learned how to break down large programs into multiple files, keeping different sections of the program in separate files. This reduces clutter and makes the code more manageable.
* **Importing Code from Other Files:** We explored the process of importing code from one file to another using the ```import``` statement. We also learned how to control which functions run when importing.
* **Creating Libraries of Functions:** By the end of the day, we were curating our own libraries of subroutines, which we could import into new programs for reuse. This is a fundamental concept for professional programmers.

### 🔍 Key Concepts:

* **Code Modularity:** Breaking large programs into multiple smaller files makes the code more readable, maintainable, and reusable.
* **Subroutines:** Functions defined in separate files (libraries) that can be imported and called when needed.
* **The ```import``` Statement:** The ```import``` keyword allows you to bring code from other Python files into your current program. This can be done in different ways, such as ```import module_name```, ```import module_name as alias```, or ```from module_name import function_name```.
* **File Structure:** We worked with two Python files: ```main.py``` for the main program and ```test.py``` (or any other file) containing functions or code we want to import. We learned how to organize and import these correctly.
* **Calling Functions from Imported Files:** After importing, functions from the imported file can be called by referencing the file name and the function name (e.g., ```test.countdown()```).

### 👉 Day 63 Challenge: Build Your Own Library of Subroutines 📚

**Task Overview:**

  * Go through your previous Python programs and pick out some of the most useful subroutines (e.g., random number generators, dice rollers, pretty print functions, etc.).
  * Create a new file containing all your best subroutines and save it as a Python file (e.g., ```mylibrary.py```).
  * Import this library into your ```main.py``` and call a few functions to demonstrate that everything works as expected.

### 🛠️ Common Errors Encountered:

* **File Not Found:** Make sure the file you’re trying to import from exists in the same directory or the Python path.
* **Function Not Defined:** Ensure that the functions you want to use in your imported file are actually defined in that file. If you try to call a function that doesn’t exist, Python will raise a ```NameError```.
* **Incorrect Import Statement:** Double-check the syntax of your import statement. When importing an entire file, you only need to use ```import filename``` without the ```.py``` extension. For example, ```import test```.
* **Running Code Upon Import:** In Python, code runs immediately upon import. If you want to control when a function runs, define it inside a function and call it explicitly. Using ```if __name__ == '__main__':``` in the imported file will prevent code from running automatically when the file is imported.

### My Code:
Here’s a quick example of how to structure and use subroutines:

**CoolSubroutine.py** (Library of Functions)
```python
def newPrint(color):
  if color=="red":
    print("\033[31m", sep="", end="")
  elif color=="green":
    print("\033[32m", sep="", end="")
  elif color=="blue":
    print("\033[34m", sep="", end="")
  else:
    print("\033[0m", sep="", end="")
```

**main.py** (Main Program)
```python
import coolSubroutines as cs

cs.newPrint("red")

print("This should be red")
