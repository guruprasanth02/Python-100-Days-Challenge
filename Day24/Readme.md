# 🌟 **Day 24: Infinity Dice Challenge** 🎲  

### 🎊 **Today’s Highlights**:  
- **Parameters in Subroutines**: We learned how to use parameters (also known as arguments) to make subroutines more flexible by passing values to them, allowing us to change their behavior based on the input.
- **Multiple Arguments**: We can pass multiple parameters into a subroutine, which makes our code more powerful and reusable.
- **User Input**: We allowed users to input their own values, making the subroutine dynamic and interactive. In this case, we used user input to set the number of sides for the dice.
  
### 🔍 **Key Concepts**:  
- **Subroutines with Parameters**: A subroutine can accept parameters (arguments) that allow us to pass data into the function, making it reusable with different inputs.
- **Flexible Functions**: By using parameters, we created a subroutine that can roll a dice with any number of sides.
- **User Input**: We collected user input to determine the number of sides for the dice and whether to roll again.

### 👉 **Day 24 Challenge**: **Create an Infinity Dice**

- **Task Overview**:
  - Create a subroutine that simulates a dice roll with any number of sides, based on user input.
  - Prompt the user for the number of sides of the dice.
  - After rolling the dice, ask the user if they want to roll again. If they say "yes", the dice should roll again. If they say "no", the program ends.

### 🛠️ Common Errors Encountered:
* **Incorrect Argument Usage:** If you forget to pass the correct number of arguments to the subroutine, Python will throw an error.

  **Fix:** Make sure you pass the expected number of arguments when calling the subroutine.

* **Invalid User Input:** If the user doesn't enter a valid number for the sides of the dice or types anything other than "yes" or "no" for the roll again question, the program may crash or behave unexpectedly.

  **Fix:** Use try-except blocks to handle invalid inputs and validate the user’s response to ensure it's a number for the sides and a valid "yes" or "no" for rolling again.

* **Infinite Loop:** If the condition to stop the loop isn't set correctly, the program could roll the dice indefinitely.

  **Fix:** Make sure the loop breaks when the user inputs "no" for not wanting to roll again.


### **My Code**:  
```python
import random
print("Infinity Dice 🎲")

sides = int(input("How many sides?: "))
playGame = "yes"

def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")
  
