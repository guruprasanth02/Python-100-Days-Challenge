# 🌟 Day 66: Simple GUI Calculator ⚙️

### 🎉 Today’s Highlights:

* **Building GUIs with tkinter:** We explored the basics of creating graphical user interfaces using the ```tkinter``` library, which allows us to add interactivity and visual elements to our Python programs.

* **Event Handling:** We used ```command``` parameters to associate button clicks with functions, enabling us to respond to user actions dynamically.

* **Layouts and Positioning:** We practiced arranging elements using both the ```pack``` and ```grid``` methods, learning how to structure GUI components effectively.

* **Arithmetic Operations:** We implemented basic calculator functionalities like addition, subtraction, multiplication, and division.

### 🔍 Key Concepts:

1. **tkinter Basics:**

      * ```Label```, ```Button```, and ```Entry``` widgets were used to display text, capture input, and allow user interaction.

      * The ```command``` parameter in buttons helped link button presses to specific functions.

2. **Grid Layout:**

      * We positioned elements systematically using the ```grid(row, column)``` method.

      * The grid system makes it easier to create structured layouts for applications.

3. **Event-Driven Programming:**

      * The calculator responds to user inputs and executes appropriate arithmetic operations based on button clicks.

### 💪 Day 66 Challenge: GUI Calculator

**Task Overview:**

Create a GUI-based calculator that:

   * Displays buttons for numbers (0-9) and basic operations (+, -, *, /).

   * Allows users to enter calculations interactively by pressing buttons.

   * Computes and displays the result when the equals button is pressed.

**Expected Features:**

   * A display area for the user to view input and results.

   * Buttons for digits 0-9.

   * Buttons for operations: addition, subtraction, multiplication, and division.

   * An "equals" button to compute and display the result.

### 🚨 Common Errors Encountered:

1. **Invalid Syntax or Runtime Errors:**

     * Using ```eval()``` without validating input can lead to crashes if the user enters invalid expressions.

     * Fix: Wrap ```eval()``` in a ```try-except``` block to handle errors gracefully.

2. **Unresponsive Buttons:**

     * Forgetting to include ```command``` in button definitions or incorrect function references can make buttons non-functional.

     * Fix: Always verify that the correct function is associated with each button.

3. **Layout Issues:**

     * Forgetting to configure grid rows and columns can lead to uneven button sizes or alignment problems.

     * Fix: Use ```window.grid_rowconfigure()``` and ```window.grid_columnconfigure()``` for uniform spacing.

### 🚀 My Code:
```python
import tkinter as tk

# Function to handle button clicks
def on_click(value):
    if value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)

# Main window setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# Display setup
display = tk.Entry(window, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

# Button labels and positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons
for text, row, col in buttons:
    tk.Button(
        window, text=text, font=("Arial", 18), command=lambda t=text: on_click(t)
    ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid layout
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()

```

**Happy coding! 🚀 Let your creativity shine as you build your GUI calculator. Experiment, learn, and enjoy!** 😄

