# 🌟 Day 31: Classic User Interface with String Manipulation 🎮

## 🎊 Today’s Highlights:
- **User Interface Design:** We created two user interfaces using string manipulation, focusing on how to format and align text for a visually appealing design.
- **String Formatting Mastery:** The challenge emphasized using print statements and f-strings to create clean and dynamic outputs.
- **Subroutine Creation:** To handle color changes (as seen in Day 29), we created a subroutine that allows for easy manipulation of text formatting and color changes.
- **Alignment Skills:** The second interface was particularly tricky due to its requirement for proper text alignment, helping us improve our understanding of how to manage and present text in a structured way.

## 🔍 Key Concepts:
- **String Manipulation:** The ability to create intricate and visually engaging user interfaces with only basic string operations.
- **f-Strings and Alignment:** Understanding how to use f-strings for inserting variables into strings and applying alignment techniques (left, center, right).
- **Subroutines for Efficiency:** By creating reusable subroutines, we ensured that tasks like changing text color were handled efficiently and flexibly.
  
## 👉 Day 31 Challenge: Classic User Interface Creation

### Task Overview:
- **Interface Creation:** Using string manipulation, create two user interfaces as shown below.
  - **Interface 1:** A simple design using print and f-strings.
  - **Interface 2:** A more complex design involving alignment, where text must be properly aligned to make the output visually appealing.
  
- **No Input Statements:** This challenge is focused entirely on string formatting and print statements. You won’t need input from the user.

- **Optional Subroutine:** Consider creating a subroutine for color-changing text (similar to Day 29) to make the UI more dynamic.

## 🛠️ Common Errors Encountered:
- **Improper Alignment:** If the text alignment isn't managed correctly, the interface can look messy. Use the appropriate string alignment techniques (`<`, `>`, `^`) to ensure the text is well-arranged.
  
  **Fix:** Use f-strings with alignment (e.g., `{variable: <20}`, `{variable: >20}`, `{variable: ^20}`) to align text within the user interface.
  
- **String Formatting Issues:** Sometimes, misplacing curly braces or forgetting to escape characters can result in errors.

  **Fix:** Double-check the placement of curly braces, especially when using f-strings, to ensure they are correctly formatted.

- **Overcomplicating the Task:** With string manipulation, it's easy to try too many things at once. Focus on breaking down the problem into smaller, manageable parts.
  
  **Fix:** Keep your code clean and simple by creating subroutines for repetitive tasks (like color changes) to avoid redundancy.

## **My Code:**

```python
def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

print(f"        {title:^35}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")


print()
print()
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text = "networking site"
print(f"{colorChange('yellow')}{text:>35}")
text = "Honest."
print(f"{colorChange('red')}{text:^35}")
text = "Username: "
username = input(f"{colorChange('white')}{text:^35}")
text = "Password: "
username = input(f"{colorChange('white')}{text:^35}")
