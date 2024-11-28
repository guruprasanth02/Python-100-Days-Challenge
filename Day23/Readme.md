# 🌟 **Day 23: Replit Login System Challenge** 🔐  

### 🎊 **Today’s Highlights**:  

- **Subroutines**: We learned how to define and call subroutines (functions) in Python to avoid repeating code and to make our programs more organized.
- **Loops**: Used loops to repeatedly ask for user input, ensuring the login system keeps asking for the username and password until the correct one is entered.
- **Conditional Statements**: Incorporated `if` statements to check if the entered username and password match the correct values.
  
### 🔍 **Key Concepts**: 

- **Subroutines**: Defined a subroutine using `def`, gave it a name, and called it with parentheses `()`. This allowed for code reuse and clean program structure.
- **Loops**: Utilized loops to repeatedly ask the user for input until the correct username and password are entered.
- **Conditional Logic**: Used `if` and `else` statements to check if the entered credentials match the expected values.

###  👉 **Day 23 Challenge**: **Create a Replit Login System**

- **Task Overview**:
  - Create a subroutine for asking the user for their username and password.
  - Use a loop to prompt the user for input until they enter the correct login information.
  - Print a success message when the correct credentials are entered.


### 🛠️ **Common Errors Encountered**:
- **Indentation Errors**: Ensure that subroutine definitions and loops are properly indented.
  
  **Fix**: Make sure to use consistent indentation (usually 4 spaces or a tab) and check that the subroutine and loop structures are correctly formatted.

- **Incorrect Function Call**: The subroutine must be called with the exact name and parentheses.

  **Fix**: Ensure you're calling the subroutine correctly by using the exact name and adding `()`.

- **Infinite Loop**: If the condition to break out of the loop is not met, the program could run indefinitely.

  **Fix**: Ensure that the loop has a correct exit condition when the credentials match.

- **Variable Scope Issues**: Sometimes variables inside a subroutine might not be accessible outside it.

  **Fix**: Be careful with where you define and use variables to avoid scoping issues, and ensure variables are passed between subroutines when necessary.
  
  
### **My Code**:  
```python
def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "Replit4ev#r":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue

print("REPLIT LOGIN SYSTEM")
login()

