# 🌟 Day 33: To-Do List Manager with Editing Functionality 📋

### 🎊 Today’s Highlights:

* **List Management:** We enhanced our list functionality by adding the ability to edit and remove items.
* **User Interactions:** The program allows the user to interact with the list dynamically (add, view, edit).
* **Dynamic Updates:** After editing or removing items, the list is updated and displayed for the user to see the changes.
* **Customizable Lists:** The user can manage a list of tasks, ideas, or anything that requires frequent updates.

### 🔍 Key Concepts:

* **Lists:** Storing and managing data collections.
* **User Input:** Using input() to gather data from the user and make decisions.
* **List Modification:** Modifying the list by adding and removing elements based on user commands.
* **F-Strings:** Using f-strings to display updated information neatly and clearly.

### 👉 Day 33 Challenge: To-Do List Manager with Editing

### Task Overview:

   1. Create a List: Start by creating a list to hold tasks or items.
   2. View the List: Display the list to the user with a numbered format.
   3. Edit the List: Allow users to remove tasks or edit them by selecting a task number.
   4. Dynamic Interaction: The list can be viewed, updated, and edited repeatedly until the user exits the program.


### 🛠️ Common Errors and Fixes:

 **Error 1: Index Out of Range**
   * Problem: The user enters a task number that doesn’t exist (i.e., higher than the list size).
   * Fix: We validate the number before removing the task. If the number is out of range, we ask the user to try again.
     
**Error 2: Invalid Input**
   * Problem: The user may input something that isn’t a number when trying to edit (e.g., entering a string).
   * Fix: We catch the ValueError using a try block to ensure the input is valid and prompt the user again.


 ### My Code:
```python
import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
