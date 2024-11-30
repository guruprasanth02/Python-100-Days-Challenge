# 🌟 Day 27: Character Builder for Your First Video Game 🎮  

### 🎊 Today’s Highlights:  
- **Character Creation**: We built a subroutine to generate a character's name and type, making the character-building process dynamic and interactive.
- **Health and Strength Stats**: We used random dice rolls to generate character stats for health and strength. By multiplying multiple dice rolls, we were able to simulate the randomness of RPG stats.
- **Menu and Presentation**: We enhanced the user experience with a clear, well-presented menu that includes timed delays using `time.sleep()` and `os.system("clear")` for a smooth, immersive flow.
- **Looping for Repeated Character Creation**: The program allows the user to generate multiple characters without restarting, making the experience feel like part of an ongoing adventure.

### 🔍 Key Concepts:
- **Subroutines for Character Data**: We created functions to generate the character's name, type, health, and strength based on random dice rolls.
- **Random Dice Rolls**: Using random dice rolls to generate stats ensures that each character is unique, adding to the fun and unpredictability of the game.
- **Using `time.sleep()`**: Pausing the execution for a moment to give the user time to appreciate the generated character data.
- **Using `os.system("clear")`**: Clearing the screen between actions keeps the interface clean and user-friendly.

### 👉 **Day 27 Challenge**: Build Your Character  

Task Overview:
- **Subroutine for Name and Type**: Create a function that asks for the character's name and type, and returns the generated data.
- **Subroutine for Health Stats**: Generate the character's health by multiplying multiple random dice rolls together.
- **Subroutine for Strength Stats**: Similarly, generate the character's strength using a set of random dice rolls.
- **Interactive Menu**: Present the results in a clean, appealing way with timed pauses and the ability to create another character.

🛠️ Common Errors Encountered:
- **Incorrect Input Handling**: The program may fail if the user enters unexpected input, so it's important to validate their responses for the character's name and type.

  Fix: Ensure you have checks for valid names and types and handle cases where input may be missing or incorrect.

- **Dice Roll Formula Mistakes**: If the dice rolls aren't multiplied correctly, the character stats may not be generated properly.

  Fix: Double-check the formulas for health and strength generation to make sure the correct number of rolls and multiplications are used.

- **Menu Disappearing Too Quickly**: Without `time.sleep()`, the user may not have enough time to view the generated stats before the screen clears.

  Fix: Use `time.sleep()` to pause for a moment and ensure the user can read the information before the screen is refreshed.

### My Code:
```python
import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

while True:
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")
