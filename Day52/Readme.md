# 🌟 Day 52: Pizza Shop Program 🍕💰

### 🎊 Today’s Highlights:

* **User Input Handling:** We prompted the user to input quantities and sizes of pizzas, ensuring only valid numerical inputs are accepted.
* **Try-Except Block:** Introduced ```try...except``` for handling errors, preventing the program from crashing if users enter invalid inputs (like typing "three" instead of "3").
* **Cost Calculation:**After receiving valid input, we multiplied the quantity and size to calculate the pizza cost, storing the information in a 2D list.
* **Auto-save and Auto-load:** We utilized auto-save and auto-load functionality to persist data about users’ pizza orders for future retrieval.

### 🔍 Key Concepts:

* **Handling Invalid Input:** We focused on managing user input errors, particularly preventing crashes when the user enters non-numeric values (e.g., "three" instead of "3"). This is achieved using a ```try...except``` block.
* **2D List Usage:** We introduced a 2D list to store pizza orders along with user names. This allowed us to store multiple orders in a structured manner.
* **Try-Except Error Handling:** We applied ```try...except``` to ensure that errors related to invalid input are gracefully handled without crashing the program. This is especially useful when working with external data or user input that could be unpredictable.

### 👉 Day 52 Challenge:

**Task Overview:**

Create a pizza ordering program that:

   1. Asks the user for the number of pizzas and their size.
   2. Calculates the total cost by multiplying the quantity by the size of the pizza.
   3. Asks for the user's name and stores the data in a 2D list.
   4. Handles invalid inputs using ```try...except```. If the user enters non-numeric input for the number of pizzas, prompt them to try again.

### 🛠️ Common Errors Encountered:

* **Non-numeric Input:** The user might type a word like "three" instead of "3", which would cause the program to crash. This can be avoided by using ```try...except``` blocks to catch ```ValueError``` and prompt the user to enter a valid number.

**Fix:** Always validate input using ```try...except``` to catch errors and ask the user to re-enter the input if necessary.

* **Incorrect Variable Assignments:** When calculating the cost of the pizza, we must ensure that both the quantity and the size are correctly used in the calculation.

**Fix:** Make sure the variable names are consistent and that the calculation is done correctly (e.g., multiplying quantity and size).

* **Handling Missing Data:** Ensure that all input fields, including the user's name, are properly collected.

**Fix:** Check if the input for the user's name is non-empty and valid before proceeding with further steps.

### My Code:
```python
import os, time
pizza = []

try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza list, using a blank list")

def viewPizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
for row in pizza:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
time.sleep(2)

def addPizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  toppings = input("Toppings: ")
  size = input("Size (s/m/l): ").lower() 
  while True:
    try:
      qty = int(input("Quantity: "))
      break
    except:
      print("Error: Quanity must be a whole number")
  cost = 0
  if size=="s":
    cost = 5.99
  elif size=="m":
    cost = 9.99
  else:
   cost = 14.99
  total = cost * qty
  total = round(total, 2)
  row = [name, toppings, size, qty, total]
  pizza.append(row)

while True:
  time.sleep(1)
  os.system("clear")
  print("Rominos Pizza")
  print()
  menu = input("1: Add Pizza\n2: View Pizzas\n> ")
  if menu == "1":
    addPizza()
  else:
    viewPizza()
f = open("pizza.txt", "w")
f.write(str(pizza))
f.close()
