# 🌟 Day 58: Debugging with Breakpoints and Game Logic 🔍🎮

### 🎊 Today’s Highlights:

* **Introduction to Debugging:** We learned how to use the debugger to pause and inspect code execution, allowing us to troubleshoot more efficiently. The debugger helps track variable values, step through code, and set breakpoints.
* **Using Breakpoints:** We set breakpoints to pause execution and observe the state of variables or the flow of the program. This technique is invaluable for pinpointing errors or understanding complex code.
* **Debugging a Game:** We applied our debugging skills to a simple number guessing game, where we used breakpoints to inspect the program flow and identify issues.

### 🔍 Key Concepts:

* **Breakpoints:** A breakpoint is a pause in your program, allowing you to inspect variables, step through code, or skip over certain sections.
* **Step Through Code:** The ability to run the program step by step to better understand its behavior and detect bugs.
* **Debugging a Program:** Using tools to pause execution, inspect variables, and step through code to find logical or syntactical errors.

### 👉 Day 58 Challenge: Debugging the Guessing Game:

**Task Overview:** 

   * We were given a simple number guessing game with a few bugs. The task was to use the debugger to identify and fix the issues.

**Key Errors:**

   * Menu Input Type: The ```input()``` function returns a string, but the code compares the menu variable with integers. We need to fix this comparison to properly handle inputs.
   * Attempts Counter: The attempts counter doesn't reset between rounds. This should be addressed to ensure that the attempt count reflects only the current round.

### 🛠️ Common Errors Encountered:

* **Input Type Mismatch:** The ```input()``` function returns a string by default. When comparing it with integers (like ```1```), a mismatch occurs. We need to convert the input to an integer.

  * **Fix:** Use ```int(input())``` to properly capture numerical input.

* **Attempts Counter Reset:** The counter for attempts is accumulating values across multiple rounds, causing an incorrect total.

  * **Fix:** Reset the attempts variable at the start of each game round.

### My Code:
```python
import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  number = random.randint(1,100)
  while True:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = int(input("1: Guess the random number game\n2: Total Score\n3: Exit\n> "))
  if menu == 1:
    totalAttempts+= game()
  elif menu == 2:
    print(f"You've had {totalAttempts} attempts")
  else:
    break
