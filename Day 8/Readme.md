# 🌟 Day 8: Affirmations (or Insults) Generator! 💬

### 🎊 Today’s Highlights:

* **Custom Affirmations:** We built a fun and personalized affirmation generator that gives users a custom message each day of the week, based on their name, favorite things, and the day of the week!
* **Input and Output:** Used input() to collect user data and output() to display personalized messages.
* **String Concatenation:** Combined strings to create unique, customized affirmations.
* **Conditional Logic:** Applied if statements (including nested ifs) to tailor messages based on the user's inputs and ensure the output changes depending on the day of the week.
* **Case-Insensitive Matching:** Implemented logic to ensure that input names are treated the same regardless of capitalization.
  
### 🔍 Key Concepts:

* **If Statements:** We used if statements to check different conditions, such as the current day of the week or the user's name.
* **Nested If Statements:** For more complex logic, we nested if statements to check multiple conditions before giving a final output.
* **String Concatenation:** We concatenated strings with dynamic user inputs to create personalized messages.
* **Case-Insensitive Comparisons:** We ensured that the program didn’t differentiate between uppercase and lowercase input by using the .lower() method to standardize the user’s inputs.
  
### 👉 Day 8 Challenge: Affirmations Generator Project

Task Overview:

Create a program that:

1. Asks the user for their name, the current day of the week, and a few of their favorite things.
2. Generates a unique affirmation or funny insult for each user based on their inputs.
3. The output should include concatenation of strings to combine the user’s data into a fun, personalized message.
4. Use if statements to handle different days of the week, names, and preferences.

**Example Flow:**

1. What is your name? > "Alice"
2. What day is it today? > "Tuesday"
3. What is something you love? > "chocolate"
4. The program will then output a message like:
   * "Alice, on this beautiful Tuesday, you are as sweet as chocolate! Keep shining!"
     
If the user prefers something funny or lighthearted instead of affirmations, generate a playful insult (keeping it friendly, of course).

### My Code:

Input and Output

![code 8 input](https://github.com/user-attachments/assets/ca5f3e18-6309-4366-994a-492a4f08d1df)

![code 8 output1](https://github.com/user-attachments/assets/c3b00763-2202-40f3-9751-5216c3f94b1a)
![code 8 output2](https://github.com/user-attachments/assets/9292e141-17fd-4a02-ae66-dc324c88652a)
![code 8 output3](https://github.com/user-attachments/assets/964b4961-ed90-482e-82c7-fa5417438cbf)

### 🛠️ Common Errors Encountered:

* **Case Sensitivity:** When checking the user’s name, we needed to handle cases where the user types it in different capitalizations (e.g., "alice" vs "Alice"). We fixed this with .lower() to standardize input.
* **Incorrect String Concatenation:** Ensure that strings are properly concatenated using + or f-strings, especially when combining dynamic user inputs with static text.
* **Typo in Day Names:** If the user enters a day in an unexpected format (e.g., "TUESDAY" vs "Tuesday"), the .lower() method ensures we handle this correctly.
