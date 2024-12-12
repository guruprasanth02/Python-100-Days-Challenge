# ✨ Day 46: Mokébeast Mokédex with 2D Dictionaries 🐮⚡

### 🎉 Today’s Highlights:

* **2D Dictionaries in Action:** Utilized nested dictionaries to store and organize Mokébeast details efficiently.

* **Dynamic Data Input:** Built a program to continuously gather user input for new Mokébeasts.

* **Pretty Print Output:** Created a structured display of all Mokébeast information using a custom prettyPrint() function.

### 🔍 Key Concepts:

* **Nested Dictionaries:** Learned how to store related data about a Mokébeast (e.g., name, element, special move, HP, MP) within a sub-dictionary, and organize these sub-dictionaries in a larger dictionary.

* **Dynamic Updates:** Added Mokébeasts to the Mokédex through user input, allowing the dictionary to grow dynamically.

* **Custom Pretty Print:** Wrote a reusable prettyPrint() function to neatly format and display the contents of a 2D dictionary.

* **Accessing Nested Data:** Used multiple keys to retrieve specific data from a nested dictionary (e.g., HP or special move of a particular Mokébeast).

### 🔧 Implementation Steps:

1. **Mokébeast Input Loop:**

      * Continuously prompted the user for Mokébeast details, including name, element, special move, HP, and MP.

      * Allowed users to stop adding new Mokébeasts by typing "n" when prompted.

2. **Storing Data:**

      * Stored each Mokébeast’s details as a sub-dictionary, with the beast’s name as the key in the main dictionary.

3. **Pretty Print Function:**

      * Iterated over the Mokédex to display each Mokébeast and its details in a clean, organized format.

4. **Accessing Specific Data:**

      * Demonstrated how to retrieve individual values, such as a specific Mokébeast’s HP or special move, using nested keys.

💪 Day 46 Challenge:

* **Advanced Mokédex Features:**

     * Add sorting by HP, MP, or element.

     * Allow users to edit existing Mokébeast details.

     * Include a search feature to find Mokébeasts by name or element.

     * Export the Mokédex to a file for future reference.

* **Example Output Enhancements:**

     * Add colored text for different elements (e.g., blue for Water, red for Fire).

### 🛠️ Common Challenges & Fixes:

1. **Key Errors:**

     * Issue: Accessing a nonexistent key resulted in a runtime error.

     * Fix: Added error-checking to ensure keys exist before accessing their values.

2. **Inconsistent Data Entry:**

     * Issue: User input varied in format (e.g., uppercase vs. lowercase elements).

     * Fix: Normalized input by converting it to lowercase or capitalized format.

3. **Messy Output:**

     * Issue: Directly printing the dictionary produced an unreadable output.

     * Fix: Designed a custom prettyPrint() function for a clean display.

### 🔹 My Code:
```python
import os, time

mokedex = {}

def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()
