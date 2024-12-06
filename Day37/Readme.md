# 🌟 Day 37: Star Wars Name Generator 👽🌌

### 🎊 Today’s Highlights:

* **String Slicing:** We explored how to slice strings in Python to extract specific portions of text. This includes extracting parts of names and manipulating strings to create a fun, personalized result.
* **User Input Handling:** We learned how to gather multiple pieces of user input and process them using string slicing and formatting methods.
* **f-Strings & String Manipulation:** By slicing and formatting strings, we can combine different pieces of text to generate creative outputs like Star Wars names!
* **Combining Inputs for Creative Outputs:** Using the inputs for names and places, we created a unique Star Wars name based on slicing and combining parts of the given information.

### 🔍 Key Concepts:

* **String Slicing:** The main focus of today was slicing strings using indices. We learned how to extract specific parts of a string by specifying the start and end index, as well as how to leave indices blank to use default values.
* **User Input and String Handling:** We combined user input with string slicing to generate custom outputs.
* **f-Strings:** We used f-strings to concatenate and format the sliced strings into the final Star Wars names.
* **String Methods:** We used methods like ```.lower()``` and ```.upper()``` to ensure the output was properly formatted (e.g., ensuring capital letters for names).

### 👉 Day 37 Challenge: Star Wars Name Generator Task Overview: Create a program that:

1. **Ask for user input:**
    * The user’s first name, last name, mother’s maiden name, and city of birth.
2. **Generate a Star Wars first name:**
    * Slice the first 3 letters of the first name and last name, then combine them.
3. **Generate a Star Wars last name:**
    * Slice the first two letters of the maiden name and the last 3 letters of the city, then combine them.
4. **Format the names properly:**
    * Ensure the Star Wars name is properly capitalized using string methods.
5. **Print the final Star Wars name.**

### 🛠️ Common Errors Encountered:

* **Slicing Out of Range:** Make sure to slice within the range of the string’s length. For instance, trying to slice more characters than the string has can lead to errors or unexpected results.

    * **Fix:** Always ensure the indices used for slicing are within the bounds of the string’s length.

* **Improper String Handling:** Sometimes user inputs might contain extra spaces, so forgetting to use ```.strip()``` can result in errors when slicing or comparing strings.

    * **Fix:** Always use ```.strip()``` to remove any extra spaces from the input to ensure proper handling of user data.

* **Incorrect Capitalization:** If f-strings or string methods like ```.upper()``` or ```.lower()``` are not used, the names might not look as expected (e.g., "david" instead of "David").

    * **Fix:** Use ```.capitalize()```, ```.upper()```, or ```.lower()``` to control capitalization as needed for a cleaner output.
 
### My Code:
```python

print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")
