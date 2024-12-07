# 🌟 Day 39: Hangman Game Challenge 🧩🎮

### 🎊 Today’s Highlights:

* **Random Word Selection:** We used random.choice() to pick a word randomly from a list of possible words.
* **User Input:** We prompted the user to guess letters one by one, checking their guesses against the chosen word.
* **Game Progress:** We displayed the word with blanks for unguessed letters and tracked the user's incorrect guesses.
* **Win/Loss Conditions:** The player wins by guessing the word correctly or loses if they make 6 incorrect guesses.

### 🔍 Key Concepts:

* **Random Word Selection:** Using random.choice(list) to randomly pick an item (in this case, a word) from a list, making each game unique.
* **String Manipulation:** Dynamically displaying the word with blanks for unguessed letters and updating the string as the player makes correct guesses.
* **User Interaction:** Continuously asking the user to guess letters and providing feedback on whether the guess is correct or not.
* **Tracking Incorrect Guesses:** Maintaining a counter for incorrect guesses and stopping the game after 6 incorrect guesses.
* **Game Flow:** Creating a loop where the user keeps guessing letters until they either guess the word or lose the game.

### 👉 Day 39 Challenge: Hangman Game Overview: Write a program that:

  1. Randomly selects a word from a predefined list.
  2. Prompts the user to guess a letter.
  3. Checks if the letter is in the word and updates the display accordingly.
  4. Keeps track of the number of incorrect guesses.
  5. Ends the game when the user guesses the word or exceeds 6 incorrect guesses.
  6. Prints a win message if the user guesses all letters or a loss message if they fail.

### My Code: 

Input and Output:

![code39 input1](https://github.com/user-attachments/assets/ed365a80-9ec7-4327-b09c-52c06710d89a)
![Code39 input2](https://github.com/user-attachments/assets/66184218-4894-4d0d-983a-af85b15ac29f)

![code39 output1](https://github.com/user-attachments/assets/6e934e54-7e76-494f-8416-c085ae035d8c)
![code39 otuput2](https://github.com/user-attachments/assets/6ef34a33-0748-47ec-ad98-48942a1dd101)

### 🛠️ Common Errors Encountered:

* **Incorrect String Updates:** Forgetting to update the displayed word correctly after each guess, leaving the word unchanged.

  **Fix:** Ensure that the display word updates with correctly guessed letters in the right places.

* **Not Handling Multiple Guesses Properly:** Allowing the user to guess the same letter multiple times without tracking it.

  **Fix:** Maintain a list of guessed letters and check if the letter has already been guessed.

* **Incorrect Incorrect Guesses Count:** Not properly counting the incorrect guesses or not limiting the total to 6 guesses.

  **Fix:** Use a variable to keep track of incorrect guesses and terminate the game once the limit is reached.

* **No Display of Hangman Art:** If you're aiming for extra points, missing the ASCII art for the hangman could make the game feel less interactive.

  **Fix:** Add ASCII art or text for each incorrect guess to visually represent the hangman drawing.


**Keep coding and have fun guessing! 🎉**




