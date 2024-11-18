# 🌟 Day 15: Animal Sound Guessing Game 🐶🐱🐮

### 🎊 Today’s Highlights:

* **While Loops:** We learned how to create loops that repeat code until a condition is met, using the while loop.
* **User Input Handling:** We used input() to ask users which animal sound they want to hear, and validated their choices.
* **Dynamic Responses:** The game responds with different animal sounds based on user input, making the experience interactive and fun.
* **Exiting the Game:** We provided the option for the user to exit the loop based on their choice, adding interactivity.

### 🔍 Key Concepts:

* **While Loops:** A loop that runs as long as the condition is True. We used this to repeatedly ask the user for animal sounds until they decided to exit.
* **User Interaction:** We gathered input from the user and used it to generate dynamic responses. The input could be anything, so we had to consider a variety of animal sounds.
* **Exiting the Loop:** The loop continues until the user types “yes” when asked if they want to exit, demonstrating a simple way to control loop execution based on user input.

### 👉 Day 15 Challenge: Animal Sound Guessing Game Task Overview:
Write a program that:

   1. Loops and repeatedly asks the user to input an animal.
   2. Responds with a sound related to the animal. If the animal is not recognized, provide a default response like “Ummm, I don’t know that animal.”
   3. After each animal sound, ask the user if they want to exit the game. If they type “yes,” the loop will stop; if they type anything else, the loop continues.


### My Code:

Input and Output:

![code 15 input 1](https://github.com/user-attachments/assets/1b9949ba-eddf-405a-bbc9-cc30a5872c8d)

![code 15 output 1](https://github.com/user-attachments/assets/8c632178-a191-47c1-9f81-805a347308b5)

### 🛠️ Common Errors Encountered:

* **Infinite Loop:** The loop runs forever if the exit condition is not set correctly. To fix this, ensure that the exit_game variable is updated within the loop and the condition checks for "yes".

    **Fix:** Use exit_game = input("Do you want to exit?: ").lower() to allow the user to exit by typing “yes” or continue by typing something else.

* **Case Sensitivity:** If the user enters animal names in different cases (like "COW" instead of "cow"), the program might not match correctly.

    **Fix:** We used .lower() to convert all input to lowercase, making comparisons case-insensitive.

* **Unrecognized Animal Names:** If the user enters an animal that the program doesn’t know, the program should handle it gracefully.

    **Fix:** Provide a default response for unknown animals like "Ummm... the [animal] goes awooga."









**Keep coding and have fun with the animals!** 🐶🐱🐮
