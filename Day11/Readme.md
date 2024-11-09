# 🌟 Day 11: How Many Seconds Are in a Year? ⏰

### 🎊 Today’s Highlights:

* **Break Down the Problem:** We learned how to break a large problem (calculating seconds in a year) into smaller, manageable parts.
* **User Input:** We used input() to ask the user if the year is a leap year.
* **Conditionals (if Statements):** Applied if statements to check if the year is a leap year, and adjusted the number of days in the year accordingly.
* **Mathematical Operations:** We used multiplication to calculate the number of seconds in a year by considering days, hours, minutes, and seconds.
* **Time Calculations:** This challenge gave us the chance to practice working with time-related calculations, such as seconds in a day and seconds in a year.

### 🔍 Key Concepts:

* **User Input:** Prompting the user to input whether the year is a leap year or not.
* **Conditionals:** Using if statements to adjust the calculation based on whether it’s a leap year (366 days) or a common year (365 days).
* **Basic Arithmetic Operations:** Multiplying the number of days by the number of hours, minutes, and seconds to get the total number of seconds.
* **Leap Year Logic:** Understanding leap years and applying the correct number of days (366 days for leap years, 365 days for common years).

### 👉 Day 11 Challenge: How Many Seconds Are in a Year? Task Overview:
Write a program that:

  1. Asks the user if the year is a leap year or not.
  2. Calculates the number of seconds in a year:
       * 1 year = 365 days (or 366 days if it’s a leap year).
       * Each day has 24 hours, each hour has 60 minutes, and each minute has 60 seconds.
  3. Outputs the total number of seconds in the year, depending on whether it's a leap year or not.

### My Code:

Input and Output

![code 11 input](https://github.com/user-attachments/assets/57bddf0b-1640-4acf-a655-c531dcd8d9d1)
![code 11 output](https://github.com/user-attachments/assets/5d3379c6-7653-48be-989f-fef0a6cb449e)
![code 11 output2](https://github.com/user-attachments/assets/6ef346e4-8b5b-4810-826a-12f5bcb439af)

### 🛠️ Common Errors Encountered:

* **Input Handling:** If the user enters anything other than "yes" or "no" (e.g., "y" or "true"), the program might misinterpret the input.

  **Fix:** Use .lower() to handle different variations of "yes" and "no" (e.g., "YES", "y", "yes", "no", "NO").

* **Incorrect Leap Year Logic:** If the leap year logic is incorrect, it might calculate the wrong number of days (e.g., 365 days in a leap year).

     **Fix:** Ensure the leap year condition is checked properly (e.g., if the user says "yes", the program should correctly set daysInYear to 366).

* **No Error Handling for Invalid Input:** If the user enters a non-yes/no response, the program may crash or give an unintended result.

     **Fix:** Add input validation to ensure the response is either "yes" or "no", and prompt the user again if the input is invalid.
