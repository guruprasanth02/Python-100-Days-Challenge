# 🌟 Day 42: MokéBeast - The Non-Copyright Generic Beast Battle Game 👾

### 🎊 Today’s Highlights:

* **Dictionaries in Action:** We utilized dictionaries to store various attributes of our MokéBeast, allowing for easy access to information like the beast's name, type, special move, HP, and MP.
* **User Input Collection:** We prompted the user to input the details for a single MokéBeast in one go using the ```input()``` function and the ```split()``` method, simplifying data entry.
* **Formatted Output:** After collecting the inputs, we displayed the MokéBeast’s details in a well-structured and color-coded format based on the beast's type, adding a touch of interactivity with text color.

### 🔍 Key Concepts:

* **Dictionaries:** We explored how dictionaries can store multiple pieces of information (e.g., name, type, special move) and how to access them efficiently via keys (e.g., ```"name"```, ```"type"```).
* **User Input Handling with Split:** By using ```input()``` to get all values in a single line and splitting the input into a list, we simplified data collection for the program.
* **Conditional Formatting:** Based on the type of the MokéBeast, we conditionally changed the text color (e.g., red for fire, blue for water, etc.) to make the game’s output more engaging.
* **Formatted Printing:** Using f-strings, we formatted and printed the MokéBeast details in a user-friendly manner, making it easy to understand and visually appealing.

### 👉 Day 42 Challenge: MokéBeast Task Overview:

* Write a program that:
   *  Asks the user to input a MokéBeast's name, type, special move, starting HP, and starting MP in a single input command.
   *  Store this information in a dictionary.
   *  Outputs the beast’s details in a color-coded format based on its type (Fire, Water, Earth, Air, or Spirit).

### 🛠️ Common Errors Encountered:

* **Incorrect Input Format:** If the user does not input all the expected fields or separates them incorrectly (e.g., missing the special move or HP), the dictionary may not have complete data, which can lead to errors when trying to output the details.

    **Fix:** Use the ```split()``` method to ensure the user inputs all required fields in the correct order, and check that each input value is provided.

* **Mismatch in Text Color for Types:** If you don't properly associate the correct color with each beast type, the text output could look inconsistent.

    **Fix:** Double-check the conditional statements for color formatting to ensure the correct colors are applied to the correct beast types.

* **Incomplete Output Due to Missing Keys:** If the user does not enter valid values for one of the dictionary keys (like HP or MP), accessing these missing keys may cause errors.

    **Fix:** Use default values or checks to ensure all expected dictionary keys are populated before outputting the data.

### 📝 My Code:
```python
mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

for name, value in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")
