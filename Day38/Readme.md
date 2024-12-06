# 🌟 Day 38: Strings and Loops 🔄💻

### 🎊 Today’s Highlights:

* **String Slicing and Loops:** We explored how we can loop through each character of a string just like we did with lists. This allows us to perform actions on individual characters within the string.
* **For Loop with Strings:** By using a for loop, we can iterate over a string and perform specific actions on each character, one by one.
* **Using Conditional Statements Inside Loops:** We incorporated if statements within the loop to perform tasks like changing the output color of certain characters based on specific conditions.
* **List to Specify Search Items:** We used a list of characters (like vowels) to check if each character from the string matches any item in the list, allowing us to take actions on those specific characters.

### 🔍 Key Concepts:

* **For Loops with Strings:** We can loop through each character of a string by treating it like a list. This allows us to access individual characters and perform operations on them.
* **String Methods and Conditional Statements:** Using ```if``` statements, we checked conditions on each character (like checking if the letter is a vowel or a specific character).
* **Color Coding with Escape Sequences:** We learned how to use special escape codes to change the output color of text in the console. For example, \033[33m sets the color to yellow, and ```\033[0m``` resets it to default.
* **Using Lists for Multiple Conditions:** We stored certain characters (like vowels) in a list, allowing us to check if a character belongs to that list and then apply an action.

### 👉 Day 38 Challenge: Code the Rainbow! Task Overview:

* **Ask the user for input:** Prompt the user to input any sentence.
* **Rainbow Color Effect:** Use a loop to go through the string. Whenever a character 'r', 'b', 'g', 'p', or 'y' is encountered, change the color of the output text:
   *  'r' for red, 'b' for blue, 'g' for green, 'p' for purple, 'y' for yellow.
* **Color Change Logic:** When the color changes (e.g., encountering a new character like 'r', 'b', 'g', etc.), update the color for the rest of the string.
* **Space Handling:** Reset the color to default whenever a space character is encountered.
* **Print the output:** Print the sentence with the appropriate colors applied based on the conditions.

### 🛠️ Common Errors Encountered:

* **Incorrect Color Handling:** If the escape codes for colors are not used correctly, the colors may not display properly, or the text may appear without the expected color changes.

   **Fix:** Make sure the correct escape sequence for colors is applied and reset properly after each character is processed.

* **Looping Through Strings:** Forgetting to loop through each character in the string can lead to issues where the program only prints the first character or the whole string at once, missing out on the intended effects.

   **Fix:** Ensure that the loop goes through each character of the string by using the ```for letter in myString:``` pattern.

* **Handling Spaces:** Spaces might cause issues if not reset properly, causing the color to stay set after a space is encountered.

    **Fix:** Use the escape code ```\033[0m``` to reset the color back to default whenever a space is encountered.

### My Code:
```python
def colorChange(color):
  if color=="r":
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[34m", end="")
  elif color=="y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")

sentence = input("What sentence do you want rainbow-izing?: ")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()
