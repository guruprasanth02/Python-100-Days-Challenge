# 🌟 Day 44: Bingo Game with Enhanced Features 🎲

### 🎉 Today’s Highlights:

* **Dynamic Input Handling:** We repeatedly asked the user for the next bingo number and validated their input.

* **2D List Manipulation:** We worked with a 2D list (bingo card) to track and update numbers as they were called.

* **Win Detection:** Added logic to check if all numbers on the bingo card were marked off (replaced with 'X'), indicating a win.

### 🔍 Key Concepts:

* **Nested Loops:** Used nested loops to check each number on the bingo card against the user’s input.

* **State Updates:** Replaced numbers on the bingo card with 'X' when they were called, updating the list dynamically.

* **Input Validation:** Ensured user inputs were valid (e.g., numbers within the bingo card’s range).

* **Win Condition:** Iterated through the bingo card to detect if all cells contained 'X', signaling the game was won.

### 🔧 Implementation Steps:

1. Initialize the Bingo Card:

     * Created a 2D list representing the bingo card with predefined numbers.

     * Displayed the card using a pretty print function for readability.

2. User Input Loop:

      * Asked the user to input the next bingo number in a continuous loop.

      * Validated the input to ensure it matched a number on the bingo card.

3. Mark the Number:

      * Located the input number on the bingo card.

      * Replaced the number with an 'X' to indicate it was marked.

4. Check for Win:

      * After each input, checked the entire bingo card to see if all cells were 'X'.

      * If all numbers were marked, declared the user as the winner and ended the loop.

5. Output the Updated Card:

      * Displayed the bingo card after every number was called, showing marked-off numbers.


### 💪 Day 44 Challenge:

* Modify the program to:

     * Randomly generate a bingo card with unique numbers.

     * Allow multiple players to compete.

     * Add a scoring system to rank players based on the number of turns taken to win.

### 💪 Common Challenges & Fixes:

1. **Number Not Found on Card:**

      * Issue: The user entered a number that wasn’t on the bingo card.

      * Fix: Added a check to notify the user if the input number wasn’t valid and prompted them to try again.

2. **Premature Win Declaration:**

      * Issue: Win logic wasn’t properly verifying the entire card.

      * Fix: Improved the nested loop logic to ensure all cells were checked for 'X'.

3. **Unreadable Card Output:**

      * Issue: The bingo card looked cluttered when printed.

      * Fix: Utilized f-strings with formatted spacing to display the card in a neat table format.

### 🔹 My Code:
```python
import random, os, time

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()

def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  
  numbers.sort()
  
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")


