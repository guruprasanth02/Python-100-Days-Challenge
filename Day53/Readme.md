# 🌟 Day 53: Video Game Inventory System Challenge 🎮📦

### 🎊 Today’s Highlights:

* **Inventory System:** Build an inventory system for an RPG game that allows users to manage items in their inventory.
* **File Management:** Save and load items from a file with auto-save and auto-load features.
* **User Interaction:** Provide a menu to allow users to add, view, and remove items, keeping track of duplicates.

### 🔍 Key Concepts:

* **File Operations:**

    * Use Python’s file handling (open, write, read) to store and load inventory items from a file.
    * Items are saved in "capitalize mode" (proper capitalization for each item).
    * Ensure that each change to the inventory is auto-saved and auto-loaded using try-except blocks for error handling.

* **User Menu:**

   * Implement a menu that lets the user:
        1. Add an item to the inventory.
        2. Remove an item from the inventory.
        3. View how many times an item appears in the inventory.

* **Duplicate Handling:**

   * Duplicates are allowed, so multiple entries of the same item should be handled correctly.

#### 👉 Day 53 Challenge: Video Game Inventory System Overview

**Write a program that:**

1. **Displays a menu with options:**

      * Add an item to the inventory.
      * Remove an item from the inventory.
      * View the inventory.

2. **Add an item:**

      * Prompt the user for an item name.
      * Add it to the inventory file (saved in capitalized form).

3. **Remove an item:**

      * Prompt the user for the item to remove.
      * If the item exists, remove it from the inventory file.

4. **View the inventory:**

      * Prompt the user for an item to view.
      * Display how many of that item the user has in their inventory. If the item doesn't exist, notify the user.

5. **Auto-save and Auto-load:**

      * The inventory is saved to a file automatically after any change (adding or removing items).
      * When the program starts, the inventory is loaded from the file. Use try-except to handle file errors (e.g., file not found).

### 📂 Input and Output:

![code53 input2](https://github.com/user-attachments/assets/f120faca-4a42-4a5f-8669-a0d89148518b)
![code53 input1](https://github.com/user-attachments/assets/f1dbff03-aa7e-4950-a04a-7759379510c6)
![code53 output1](https://github.com/user-attachments/assets/a9200f5c-bdbb-47e2-b7aa-af7648e21107)
![code53 ouput2](https://github.com/user-attachments/assets/de3692ce-4570-45c4-bf07-05f8630a9191)


### 🛠️ Common Errors Encountered:

* **File Not Found:**
  
  **Error:** The inventory file doesn’t exist.
  
  **Fix:** Use try-except to check for file existence and create it if necessary.

* **File Handling Errors:**
  
  **Error:** File handling mistakes like overwriting instead of appending.
  
  **Fix:** Use ```open('inventory.txt', 'a')``` for adding items instead of overwriting the file.

* **Item Counting Issues:**

  **Error:** Incorrectly counting the number of items in the inventory.

  **Fix:** Ensure the program reads the file correctly and counts the occurrences of each item.

* **Invalid Item Removal:**
  
  **Error:** Trying to remove an item that doesn't exist.
  
  **Fix:** Check if the item exists before attempting to remove it, and notify the user if it isn’t found.



**Keep working through the challenge and enjoy building your RPG inventory system!** 🚀
