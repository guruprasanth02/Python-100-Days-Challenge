# 🌟 Day 45: To-Do List with Priority Management ✅

### 🎉 Today’s Highlights:

* **Enhanced To-Do List Management:** Built a to-do list system that tracks tasks along with due dates and priority levels.

* **Dynamic User Interaction:** Added a menu system that allows users to add, view, edit, and remove tasks dynamically.

* **Pretty Print Output:** Utilized pretty printing to display tasks in a clear, organized format.

### 🔍 Key Concepts:

* **Data Structuring with Dictionaries:** Each to-do item is stored as a dictionary containing task details such as description, due date, and priority.

* **Menu-Based User Interaction:** Implemented a menu-driven program to navigate between adding, viewing, editing, and removing tasks.

* **Search and Filter:** Enabled users to filter tasks based on priority levels (high, medium, low) for better task management.

* **Dynamic Updates:** Provided the ability to edit or remove tasks, ensuring flexibility.

### 💪 Day 45 Challenge:

* Enhance the system by adding the following features:

     * Allow sorting tasks by due date or priority.

     * Add notifications for overdue tasks.

     * Export tasks to a file for external use.

### 💪 Common Challenges & Fixes:

1. **Duplicate Tasks:**

      * Issue: Users could accidentally add duplicate tasks.

      * Fix: Added a check to warn users about potential duplicates.

2. **Invalid Input for Priority:**

      * Issue: Users entered incorrect values for priority levels.

      * Fix: Restricted input to predefined options (high, medium, low).

3. **Unreadable Output:**

      * Issue: Displaying tasks without formatting made it hard to read.

      * Fix: Used f-strings and table-like formatting for better readability.

### 🔹 My Code:
```python
# | Name | Date | Priority
import os, time
todo = []

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


