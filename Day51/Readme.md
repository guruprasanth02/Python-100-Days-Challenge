# 🌟 Day 51: Diary System with Auto-Save and Auto-Load 🗓🔓

### 🎉 Today’s Highlights:

* **File Handling in Python:** We explored how to save and load data from files to persist data between program runs.

* **2D Lists:** Utilized 2D lists to store and manage diary events.

* **Auto-Save:** Implemented a feature to automatically save changes to a file after every update.

* **Auto-Load:** Ensured previously saved data is loaded at the start of the program to prevent data loss.

### 🔍 Key Concepts:

1. **File I/O:**

      * Used the ```open()``` function to read and write data to a file.

      * Implemented different file modes (‘r’ for reading, ‘w’ for writing).

2. **Persistence:**

      * Saved the current state of the ```myEvents``` list to a file after every modification.

      * Loaded pre-existing data from the file when the program starts.

3. **Data Serialization:**

      * Used ```str()``` to convert the 2D list into a format suitable for writing to a file.

      * Leveraged ```eval()``` to reconstruct the list from the saved string.

### 🛠️ Common Errors Encountered:

1. **No Such File Error:**

      * When attempting to load data from a file that doesn’t exist.

      * **Fix:** Add a check to create the file if it doesn’t exist.
        ```python
          import os

          if not os.path.exists("calendar.txt"):
              with open("calendar.txt", "w") as f:
                  f.write("[]")  # Initialize an empty list

2. **Data Loss on Restart:**

      * The ```myEvents``` list was overwritten with an empty list on every program run.

      * **Fix:** Load data from the file into myEvents before starting the loop.

3. Incorrect List Modifications:

      * Errors occurred when trying to remove an event that didn’t exist.

      * **Fix:** Added checks to ensure the event exists before attempting removal.

### 💡 Day 51 Challenge:

Upgrade your **Day 45 To-Do List** program with auto-save and auto-load functionality. Follow these steps:

   1. Save the to-do list to a file after every modification.

   2. Load the saved to-do list at the start of the program.

   3. Handle errors gracefully, such as missing files or invalid input.

### 🔗 Code Snippet:
```python
# | Name | Date | Priority
import os, time
todo = []
f = open("to.do", "r")
todo = eval(f.read())
f.close()

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")
  f = open("to.do", "w")
  f.write(str(todo))
  f.close()
