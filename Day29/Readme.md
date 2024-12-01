# 🌟 Day 29: Colorful Text Subroutine Challenge 🎨

## 🎊 Today’s Highlights:
- **Color Manipulation with `end` and `sep`**: We explored how to modify the appearance of text by using `end` and `sep` arguments in the `print()` function.
- **Control Cursor Visibility**: We learned how to hide and show the terminal cursor while displaying text, making our program more dynamic.
- **Text Formatting**: Using escape sequences to apply colors to text, we managed to print text in multiple colors and fixed spacing issues.
- **Subroutine Creation**: We applied our new skills to create a subroutine that prints text in a specific color and ensures proper formatting.

## 🔍 Key Concepts:
- **`end` and `sep` Parameters in `print()`**: These parameters allow us to control how text is printed, such as removing the default newline (`end`) or adjusting how elements are separated (`sep`).
- **Escape Sequences for Colors**: We used ANSI escape codes to change text colors and reset them, making the output more visually appealing.
- **Hiding and Showing the Cursor**: We learned how to manipulate the terminal cursor, hiding it during output for a cleaner display and showing it back when needed.

## 👉 Day 29 Challenge: Write a Subroutine That Prints Text in Color
### Task Overview:
- **Subroutine Creation**: Write a subroutine that takes text as input, prints it in a specified color, and resets the color after printing.
- **Control Spacing**: Use the `end` and `sep` parameters to prevent random symbols or spaces from appearing between different sections of text.
- **Color Codes**: Use ANSI escape codes to change the color of the text output.

### Key Features:
- **Color Control**: The subroutine will use escape sequences to print text in different colors, making it stand out.
- **Formatting**: Using `end` and `sep`, we ensure the text is printed without extra spaces or symbols between the different color segments.
- **Flexible Input**: The subroutine can accept any text and print it in the desired color without modifying the main program logic.

### 🛠️ Common Errors Encountered:
- **Incorrect Use of `end` and `sep`**: If these parameters are used incorrectly, it can result in unexpected spaces or symbols in the printed output.
  
  **Fix**: Ensure that the `end` parameter is used to control line breaks, and the `sep` parameter controls the spacing between arguments in `print()`.

- **Color Reset Issues**: Sometimes, the color might not reset after printing, causing subsequent text to inherit the color.

  **Fix**: Always reset the color with `\033[0m` after printing colored text to avoid affecting the following text.

- **Cursor Visibility**: If the cursor is not properly managed, it can be distracting or cause issues in the terminal display.

  **Fix**: Use the escape sequence `\033[?25l` to hide the cursor and `\033[?25h` to show it.

### My Code:

```python
def newPrint(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue")
