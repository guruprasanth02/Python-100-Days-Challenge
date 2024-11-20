# 🌟 Day 18: Guess the Number Game 🎮🔢

### 🎊 Today’s Highlights:

* **While Loops for Repetition:** We learned how to use a while loop to repeatedly ask the user to guess a number until they guess it correctly.
* **User Feedback with Conditions:** We implemented conditional logic to provide feedback to the user, such as “too low” or “too high,” depending on their guess.
* **Tracking Attempts:** We added a counter to keep track of how many attempts the user took to guess the number correctly, adding a competitive element to the game.
* **Early Exit for Negative Numbers:** As an extra challenge, we added functionality to immediately exit the game if the user enters a negative number.
  
### 👉 Day 18 Challenge: Guess the Number Game Task Overview:

* Pick a random number between 0 and 1,000,000.
* Use a while loop to repeatedly ask the user to guess the number.
* Provide feedback after each guess, telling them if their guess is too low or too high.
* If the user guesses correctly, tell them they are a winner and display how many attempts it took.
* Extra Challenge: If the user enters a negative number, immediately exit the game.

### My Code:

Input and Output:
![code18 input](https://github.com/user-attachments/assets/e2e8118e-a177-4cc7-8bbd-0bc31179b913)
![code18 output2](https://github.com/user-attachments/assets/eab8d339-6eaf-4a30-ba2f-28c65260156e)
![code18 output 1](https://github.com/user-attachments/assets/f6cd0e6a-d7ac-4e55-92c7-e83c5853662b)


### 🛠️ Common Errors Encountered:

* **Entering Invalid Data:** If the user types something that isn’t a number (e.g., letters or symbols), it can cause an error.

    **Fix:** Use try and except to handle errors and prompt the user for a valid number.

* **Negative Number Handling:** If the user enters a negative number, the program should exit gracefully.

     **Fix:** Check for negative inputs early in the loop and use exit() to stop the game immediately if a negative number is entered.

* **Infinite Loop:** If the loop doesn’t correctly break when the user guesses correctly, the game will continue indefinitely.

     **Fix:** Ensure that the loop is exited using break once the correct number is guessed.

Keep coding and keep having fun with your number guessing skills! 🎮🔢
