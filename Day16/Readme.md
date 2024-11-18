# 🌟 Day 16: Name the Lyrics Game 🎤🎶

### 🎊 Today’s Highlights:

* **While True Loops:** We learned how to create a while True loop, which is a special type of loop that runs indefinitely until we tell it to stop using a break statement.
* **User Interaction:** We added interactive elements where the user has to guess missing lyrics from a song, encouraging engagement and fun.
* **Game Flow Control:** We used break to end the loop when the player guesses the correct lyric, demonstrating how to exit loops dynamically based on conditions.
* **Error Handling:** We ensured the game responds correctly to incorrect guesses by prompting the player to try again.

### 🔍 Key Concepts:

* **while True Loops:** A loop that continues to run forever until explicitly stopped by a break statement. This is useful when you don't know how many iterations will be needed in advance.
* **User Input Handling:** We prompted the user to guess the missing lyrics in the song, checking their answers using conditionals.
* **Flow Control with break:** The loop continues asking for input until the user guesses the correct lyric. The break statement stops the loop once the correct answer is provided.
* **Tracking Attempts:** The game provides feedback on how many attempts the user took to guess the correct lyric, which enhances the competitive element.

### 👉 Day 16 Challenge: Name the Lyrics Game Task Overview:
Write a program that:

   1. Displays part of a song lyric with a missing word (e.g., "Never going to ______ you up").
   2. Prompts the user to guess the missing word.
   3. If the guess is incorrect, prompt the user to try again until they guess the correct lyric.
   4. Keep track of how many attempts it takes to get the correct answer.
   5. Once the user guesses correctly, congratulate them and display the number of attempts.

### My Code:

Input and Output:

![code 16 input 2](https://github.com/user-attachments/assets/d0c96cfb-6c31-46b5-8a41-7215c7d181cf)
![code 16 output 2](https://github.com/user-attachments/assets/dba655a8-ae80-46f9-a04c-6a033db83d13)

### 🛠️ Common Errors Encountered:

* **Infinite Loop:** If you forget the break statement or don’t properly check the condition to stop the loop, the program will run indefinitely.

    **Fix:** Ensure the correct condition is checked within the loop, and use break to stop the loop when the correct lyric is guessed.

* **Incorrect Variable Comparisons:** If you don’t compare the user’s guess correctly (e.g., guess == "give"), the program may not respond as expected.

    **Fix:** Ensure that the condition checks for the correct input. Also, remember that .lower() can help handle case insensitivity (e.g., "Give" vs. "give").

* **Failure to Track Attempts:** If you don’t keep track of the number of attempts, the game won't know how many guesses the user made.

    **Fix:** Use a counter variable (like attempts) to track the number of guesses and display it when the user guesses correctly.




**Keep coding and keep rocking those lyrics!** 🎤🎶
