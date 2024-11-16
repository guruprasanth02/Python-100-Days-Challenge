# 🌟 Day 14: Rock, Paper, Scissors Game 🪨📄✂️

### 🎊 Today’s Highlights:

* **User Input Handling:** We learned how to take user input securely using getpass so that players can't see each other's choices.
* **Conditional Logic:** We used if/elif/else statements to determine the winner based on the players' choices.
* **Error Handling:** We ensured that players' inputs were validated and could handle incorrect or misspelled entries.
* **Fun Game Design:** Added a fun touch to the game by incorporating emojis and comments to enhance the user experience.

### 🔍 Key Concepts:

* **Secure Input:** We used the getpass function for secure input so that each player’s choice remains hidden.
* **Conditionals & Nested Logic:** We applied nested if/else statements to check the conditions for each player’s choice and determine the winner.
* **Input Validation:** We ensured the players’ inputs are valid (R, P, or S) and prompted them to re-enter their choices if they typed incorrectly.
* **Game Output:** Displayed the result of the game, including who won, who lost, or if there was a tie, with some cool emojis to make it more engaging.

### 👉 Day 14 Challenge: Rock, Paper, Scissors Game Task Overview:
Write a program that:

  1. Prompts two players to choose either Rock (R), Paper (P), or Scissors (S) using secure input.
  2. Validates their input and allows them to re-enter their choices if an invalid input is given.
  3. Compares both players’ choices using conditional logic to determine the winner:

        * Rock beats Scissors 🪨✂️
        * Scissors beats Paper ✂️📄
        * Paper beats Rock 📄🪨
          
  5. Displays the result with an appropriate message: who won, who lost, or if it’s a tie.
  6. Adds fun emojis to enhance the game experience!

### 💻 My Code:

![code 14 input1](https://github.com/user-attachments/assets/160277bf-dc5b-4a6d-92bf-8eff120c92ef)![code 14 input 2](https://github.com/user-attachments/assets/8ed7dd14-4717-4e73-9585-d7d28602310a)
![code 14 output 1](https://github.com/user-attachments/assets/dc83b732-a509-4f08-803a-4d110ccf2cb5)


### 🛠️ Common Errors Encountered:

* **Invalid Input:** If the player enters a choice other than R, P, or S, the program would need to ask for the input again.
  
   **Fix:** We added a validate_input function to re-prompt players until they enter a valid choice.

* **Case Sensitivity Issues:** If the user enters lowercase letters (e.g., "r" instead of "R"), it could cause errors.

   **Fix:** We used .upper() to convert input to uppercase, ensuring consistency.

* **Logic Mistakes in Comparing Choices:** If the conditional logic isn't correctly comparing the players' choices, it can give incorrect results.

   **Fix:** We carefully structured the conditional logic to ensure the correct outcomes for each choice.

* **Not Displaying Correct Result:** The game result might not display if there’s an issue in determining the winner.

    **Fix:** We ensured that the result is correctly calculated based on the players’ choices.

Keep coding and have fun! 🪨📄✂️
