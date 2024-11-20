# 🌟 Day 17: Rock, Paper, Scissors Game with Scoring and Loops ✋✌️🗡️

### 🎊 Today’s Highlights:

* **While True Loops:** We expanded our knowledge of while True loops to create a game that can run indefinitely until certain conditions are met.
* **Multiple Rounds:** Using loops, we built a system that lets players compete for multiple rounds in a Rock, Paper, Scissors game.
* **Game Scoring:** We tracked the scores for both players and added logic to keep count of the number of rounds won.
* **Break & Exit for Game End:** We used break to exit the loop when one player reaches 3 wins, and exit() to end the game completely after declaring the winner.
* **Continue to Restart Rounds:** We applied continue to restart a round if neither player won, ensuring the game doesn't break unexpectedly.

### 🔍 Key Concepts:

* **While True Loops with Conditional Exit:** We used while True to keep the game running, and added checks to exit the loop when one player reaches 3 wins.
* **Scoring and Player Tracking:** We implemented a scoring system that kept track of the number of rounds each player won.
* **Flow Control with Break and Exit:** By using break, we were able to stop the loop when the game had a winner, and exit() completely ended the program when it was time to wrap up.
* **Game Logic with Continue:** continue allowed us to quickly return to the start of the loop for a new round if there was no winner.

### 👉 Day 17 Challenge: Rock, Paper, Scissors with Scoring Task Overview:

* Build on your previous Rock, Paper, Scissors game from Day 14.
* Modify the game to play multiple rounds and keep track of the score for both players.
* The game ends when one player wins 3 rounds, using break and exit to stop the game.
* Use continue to restart a round when necessary.

### My Code:

Input and Output:

![CODE17 INPUT 2](https://github.com/user-attachments/assets/afe69426-96fe-437b-8909-748c8fcdcc72)
![CODE17 input 3](https://github.com/user-attachments/assets/34269a1d-1a14-4c69-ace0-40a79a50f4e2)

![code17 output 2](https://github.com/user-attachments/assets/43ca0104-878a-4902-ae6d-1b1dd2d58fc8)
![code17 output 3](https://github.com/user-attachments/assets/da64fc2d-4053-4e5c-aa05-76b3bff1c2e0)

### 🛠️ Common Errors Encountered:

* **Invalid Input Handling:** If the player enters a choice that’s not 'rock', 'paper', or 'scissors', the game will display an error and prompt for input again.

     **Fix:** Use continue to restart the round if the player enters an invalid option.

* **Incorrect Scoring Logic:** If the player’s score isn’t updated correctly after each round, it can cause inaccurate game results.

     **Fix:** Make sure that player_score and computer_score are updated based on the outcome of each round.

* **Game Logic Errors:** If the game doesn’t check for a winner (i.e., no end condition is set), the loop might continue indefinitely.

     **Fix:** Use break and exit() correctly to stop the game once one player wins 3 rounds.

**Keep coding and enjoy building your own competitive game!** ✋✌️🗡️
