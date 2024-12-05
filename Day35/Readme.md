# 🌟 Day 35: To-Do List Manager Upgrade ✅📝

### 🎊 Today’s Highlights:

* **User-Driven Menu:** We learned how to create a menu-driven to-do list manager where the user can view, add, edit, or remove items from their to-do list, allowing more dynamic interaction.
* **No Duplicates:** We incorporated a check to ensure that duplicate items cannot be added to the list, preventing redundancy and keeping the list neat.
* **Confirmation Before Deletion:** We added an extra layer of security by asking the user to confirm before removing an item, avoiding accidental deletions.
* **Clear the List:** We gave the user the option to clear the entire list in a single line of code for convenience, making the list reset effortless.

### 🔍 Key Concepts:

* **Menu-Driven Programs:** A user-friendly interface that presents options and responds based on the user’s choice. This allows users to interact with the program dynamically and control the flow.
* **Conditionals for Item Removal:** Using if statements to check user input and confirm the deletion of a to-do item, ensuring it is intentional.
* **Checking for Duplicates:** Preventing the addition of duplicate items by checking if the item already exists in the list before allowing it to be added.
* **Erasing a List in One Line:** A quick and simple way to clear all items from the to-do list with a single line of code, enhancing the program's usability.

### 👉 Day 35 Challenge: To-Do List Manager Task Overview:

### Write a program that:

  * Displays a menu asking if the user wants to view, add, edit, or remove an item from their to-do list.
  * If adding an item, check if it’s already in the list to prevent duplicates.
  * Allow the user to edit the text of an existing item.
  * When removing an item, ask for confirmation before deleting it.
  * Provide an option to clear the entire to-do list in one line of code.

### My Code:

Input and Output:
![code35 input 1](https://github.com/user-attachments/assets/c661b41e-81fc-4b3b-8f13-117628df2af0)
![code35 input 2](https://github.com/user-attachments/assets/efe8800b-38d4-4b87-9fb7-28e941ffe41b)

![code35 output 1](https://github.com/user-attachments/assets/7de45e05-0b51-4a43-aa8e-0f0efb54c0d7)
![code35 output 2](https://github.com/user-attachments/assets/ef417a0d-5d5d-4266-970c-05f92cb58ed2)


### 🛠️ Common Errors Encountered:

* **Not Checking for Duplicates:** Forgetting to check whether an item already exists in the list before adding it. This results in duplicate items being added.
* 
  **Fix:** Always check if the item exists in the list before appending it. If it does, notify the user and skip adding it.
  
* **User Input Issues:** If the user enters an unexpected response (e.g., typing something other than 'yes' when confirming deletion), the program might behave unpredictably.

  **Fix:** Validate input properly by using conditionals and providing clear instructions for acceptable inputs.

* **Clearing the List Incorrectly:** Using an inefficient or complex method to clear the list instead of using the one-line code solution.

  **Fix:** Use the .clear() method to clear the entire list with a single line of code, as it's simple and effective.


**Keep coding and keep improving your to-do list management!** 📋🎯
