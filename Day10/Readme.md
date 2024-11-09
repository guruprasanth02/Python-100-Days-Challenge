# 🌟 Day 10: Let's Split the Bill! 💸

### 🎊 Today’s Highlights:

* **User Input:** We used the input() function to ask the user for the bill amount, tip percentage, and number of people splitting the bill.
* **Mathematical Operations:** Applied basic arithmetic (addition, division, multiplication) to calculate each person’s share of the bill, with the added complexity of tips.
* **Rounding:** Utilized Python’s round() function to limit the decimal places for each person’s share.
* **Conditional Logic:** Ensured proper calculations by asking for inputs in the correct order and performing necessary mathematical operations.

### 🔍 Key Concepts:

* **User Input:** Prompting the user for the bill amount, tip percentage, and number of people.
* **Basic Math Operators:** Using +, /, *, and % to perform essential calculations like dividing the total bill and adding a tip.
* **Rounding:** The round() function was used to display the share of the bill with only two decimal places, ensuring the result is more user-friendly.
* **Floating Point Numbers:** Working with float data types for the bill amount and dividing by an integer number of people to ensure correct results with decimals.

### 👉 Day 10 Challenge: Bill Splitting with a Tip Task Overview:
Create a program that:

   1. Asks the user to input the total bill amount.
   2. Prompts for the tip percentage they would like to leave.
   3. Calculates the total bill including the tip.
   4. Splits the total bill among a given number of people.
   5. Outputs the amount each person owes, rounded to 2 decimal places.

     
### My Code:
Input and Output

![code 10 1 input](https://github.com/user-attachments/assets/3f7615a3-11ac-4d2d-9cb3-ddff14a3552a)
![code 10 1 output](https://github.com/user-attachments/assets/972bbb19-23ad-4256-a327-2a029574657c)

### 🛠️ Common Errors Encountered:

* **Incorrect Input Types:** If the user enters non-numeric values (e.g., strings instead of numbers), the program could crash.
  
     **Fix:** Use try-except blocks to handle incorrect inputs and prompt the user again.

* **Tip Calculation Error:** If the tip percentage is entered as a whole number (like "15" for 15%) instead of a decimal fraction (like "0.15"), the final tip calculation might be incorrect.

     **Fix:** Ensure that the tip percentage is converted correctly into a decimal (i.e., divide by 100).

* **Division by Zero:** If the user accidentally inputs "0" as the number of people splitting the bill, the program will throw an error.

     **Fix:** Add a check to ensure that the number of people is greater than zero.

* **Improper Rounding:** If the rounding isn’t applied correctly, users could see an excessive number of decimals.
  
     **Fix:** Use round() to restrict the result to two decimal places.

