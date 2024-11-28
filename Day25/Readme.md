# 🌟 **Day 25: Health Stats Generator for a Video Game** ⚔️  

### 🎊 **Today’s Highlights**:  
- **Return Command in Subroutines**: We explored how subroutines can send information back to the main program using the `return` command. This allows functions to generate values that can be used elsewhere in the program.
- **Multiple Subroutines**: We combined multiple subroutines to create a dynamic character health stats generator. The first subroutine rolls a dice with any number of sides, and the second combines dice rolls to generate health stats.
- **Loops**: We used loops to give the user the option to generate health stats for multiple characters.
- **Interactive User Input**: We allowed the user to input the character's name and generated personalized health stats based on dice rolls.

### 🔍 **Key Concepts**:  
- **`return` Command**: The `return` statement in a subroutine is used to send a value back to the caller. This enables us to reuse calculated values in other parts of the program.
- **Subroutine Communication**: Functions can communicate with the main part of the program by returning values that can be assigned to variables.
- **Looping for Multiple Inputs**: We used a `while` loop to allow the user to generate health stats for multiple characters without restarting the program.

### 👉 **Day 25 Challenge**: **Create a Health Stats Generator**  

- **Task Overview**:
  - Create a subroutine to roll a dice with any number of sides and return the result.
  - Create another subroutine to roll a six-sided and an eight-sided dice, multiply the results, and return that as the character's health.
  - Add a loop that prompts the user to enter a character’s name and then generates the character’s health stats.
  - Allow the user to generate health stats for more than one character.

### 🛠️ Common Errors Encountered:
* **Missing return in Subroutines:** If the subroutine doesn't return a value, the program may not work as expected.

  **Fix:** Make sure to include a return statement to send values back to the calling code.

* **Incorrect Function Calls:** Forgetting to call a subroutine or passing incorrect parameters can lead to errors.

  **Fix:** Ensure you're calling the function properly and passing the correct arguments.

* **Infinite Loops:** If the loop doesn’t break or isn’t set up correctly, it can cause the program to run forever.

  **Fix:** Add a clear condition to exit the loop after generating stats for the user, e.g., by checking if the user inputs "no" when asked if they want to generate more stats.

* **Random Function Misuse:** Using random functions improperly or not importing random correctly can result in errors.

  **Fix:** Ensure you are importing the random library and calling its functions properly (e.g., random.randint()).


### **My Code**:  
```python
import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️CHARACTER STATS GENERATOR!⚔️")


haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")

