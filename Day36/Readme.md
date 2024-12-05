# 🌟 Day 36: Name List Manager 👥✍️

### 🎊 Today’s Highlights:

  * **User Input Handling:** We learned how to handle user input for first and last names, ensuring any extra spaces are stripped away.
  * **Capitalization:** We used string methods like ```.capitalize()``` to ensure the first letter of each name is capitalized, creating a cleaner and more consistent format.
  * **Unique Entries:** We ensured that the program prevents duplicates by checking for existing names before adding them to the list.
  * **Dynamic Output:** After adding a new name, the program prints the updated list, showing the most recent changes instantly.

### 🔍 Key Concepts:

  * **String Methods:** We used ```.strip()``` to remove unnecessary spaces, and ```.capitalize()``` to ensure the first letter of each name is capitalized, which ensures uniform formatting of names.
  * **Duplicate Prevention:** By checking if a name already exists in the list using ```if name not in list```, we avoid adding duplicates.
  * **f-Strings:** We used f-strings to format and combine the first and last names, ensuring they appear as a single, neatly formatted string.
  * **List Updates:** After each new entry, we printed the updated list to provide real-time feedback on the changes.

### 👉 Day 36 Challenge: Name List Manager Task Overview:

### Create a program that:

   * Asks the user for a first name and last name (separately).
   * Strips any leading or trailing spaces from the names.
   * Capitalizes the first letter of each name.
   * Combines the first and last names using an f-string.
   * Prevents duplicate names from being added to the list.
   * Prints the updated list each time a new name is added.

### 🛠️ Common Errors Encountered:

 * **Not Stripping Spaces:** Forgetting to use ```.strip()``` can result in extra spaces around names, which might cause inconsistencies.

   * **Fix:** Always use ```.strip()``` to remove any extra spaces from input before processing.

 * **Capitalization Issues:** If ```.capitalize()``` isn't used correctly, the name might not be capitalized as expected.

   **Fix:** Ensure you capitalize the first letter of the name properly and handle case insensitivity appropriately.

 * **Duplicate Names:** Forgetting to check if a name already exists in the list before adding it can lead to duplicate entries.

   * **Fix:** Use an if statement to check for duplicates (i.e., ```if name not in list```) before appending it.


### My code:
```python
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
```


