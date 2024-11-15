# 🌟 Day 13: Grade Generator 🎓

### 🎊 Today’s Highlights:

* **User Input:** We asked the user for the name of the test, maximum score, and their score to generate the grade.
* **Percentage Calculation:** We learned how to calculate the percentage of the score and rounded it to 2 decimal places.
* **Conditionals:** We used if/elif statements to assign letter grades based on the percentage.
* **Emojis & Styling:** Added a fun visual element to display the grade with emojis or colors based on performance.

### 🔍 Key Concepts:

* **User Input:** Collecting the test name, maximum score, and user score from the user.
* **Mathematical Operations:** Calculating the percentage by dividing the user’s score by the maximum score and multiplying by 100.
* **Conditional Logic:** Using if/elif statements to categorize the percentage into different grade brackets (A+, A, B, C, D, U).
* **Rounded Percentage:** We rounded the percentage to two decimal places for neatness.
* **Emojis/Colors:** Added feedback using emojis (like 🎉 for high grades) and color formatting for visual impact.

### 👉 Day 13 Challenge: Grade Generator Task Overview:
Write a program that:

1. **Asks for the test name, maximum score, and the user’s score.**
2. **Calculates the percentage** and rounds it to 2 decimal places.
3. **Assigns a letter grade** based on the percentage using if/elif statements:

     * A+ for 90-100%
     * A for 80-89%
     * B for 70-79%
     * C for 60-69%
     * D for 50-59%
     * U for below 50%.
4. **Displays the percentage and letter grade** along with emojis to celebrate the grade.
5. **Uses colors** (e.g., red for low grades, green for high grades) to visually represent performance.

### My Code:

Input and Output

![code 13 input](https://github.com/user-attachments/assets/6ba941d5-4c51-4ba7-b084-5718d3c82f1b)

![code 13 output1](https://github.com/user-attachments/assets/81aad75f-451a-47b3-89ea-800a83fe2d7a)
![code 13 output2](https://github.com/user-attachments/assets/d6fda178-0fc6-4638-9417-fc3b7a156ea3)

### 🛠️ Common Errors Encountered:

* **Incorrect Data Types:** If the user enters non-numeric input for the scores, the program will crash.

   **Fix:** Add error handling for invalid inputs (e.g., try/except blocks or input validation).

* **Wrong Grade Categorization:** If the percentage is not calculated correctly, the grade could be wrong.

   **Fix:** Double-check the logic used to calculate the percentage and ensure the boundaries for letter grades are correct.

* **Rounding Issues:** The percentage might not display as expected if rounding isn't done properly.

   **Fix:** Use round(percentage, 2) to ensure the output is displayed with two decimal places.
