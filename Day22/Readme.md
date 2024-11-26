# 🌟 Day 22: Totally Random One-Million-to-One Guessing Game 🎮✨

### 🎊 Today’s Highlights:

* **Random Number Generation:** We learned how to use the random library to generate a completely random number each time the game is played.
* **User Guessing:** The game prompts the user to guess a randomly generated number between 1 and 1,000,000.
* **Guessing Feedback:** We provided feedback to the user about whether their guess was too high or too low.
* **Winning Condition:** The game stops once the user guesses the correct number and shows how many guesses it took to get there.

### 🔍 Key Concepts:

* **Random Number Generation:** By using the random.randint() function, we can generate random integers within a specified range.
* **Loops and Logic:** We implemented a loop to repeatedly ask the user for guesses until the correct number is found.
* **User Input and Feedback:** The program gives feedback on whether the user's guess is too high or too low, helping them adjust their next guess.
* **Counting Guesses:** We kept track of the number of guesses it took for the user to correctly guess the number, adding a layer of tracking and interactivity.

👉 Day 22 Challenge:

**Task Overview:** Write a program that:

   * Generates a random number between 1 and 1,000,000.
   * Prompts the user to guess the number.
   * After each guess, informs the user if their guess is too high, too low, or correct.
   * Once the user guesses correctly, the program displays how many guesses it took to find the number.

### 💻 My Code:

Input and Output:
![code22 input1](https://github.com/user-attachments/assets/f7715879-6bac-47cb-8e72-1c523f4f600c)
![code22 output1](https://github.com/user-attachments/assets/e1f9661c-912d-4f87-b2fc-1f7873ce160f)

### 🛠️ Common Errors Encountered:

* **NameError (randint not defined):**
  
  **Problem:** If you forget to import the random library, you might encounter a NameError when using randint().
  
  **Fix:** Ensure you import the random library with import random at the top of your script.

* **TypeError (input type mismatch):**
  
  **Problem:** When the user inputs a non-numeric value, the program will raise a TypeError.
  
  **Fix:** We use int(input(...)) to ensure the input is converted to an integer.

* **Infinite Loop (forgot to update guess):**
  
  **Problem:** If the guess variable isn't updated within the loop, the game could get stuck.
  
  **Fix:** Ensure that the guess is updated by using int(input(...)) each time the loop runs.

* **Unclear Output Format:**
 
  **Problem:** If the output message isn't clear, users may not know how many guesses they took or if they've won.
  
  **Fix:** Use a clear and concise message to show the number of guesses once the user guesses correctly.

**Keep coding and enjoy playing the Totally Random One-Million-to-One Guessing Game!** 🎮✨
