# 🌟 Day 47: Top Trumps Game Simulation 🃏🔥

### 🎊 Today’s Highlights:

* **Stat-Based Gameplay:** Created a fun and interactive Top Trumps-style game where users compare stats of objects in a category to determine the winner.

* **Dynamic 2D Dictionary:** Designed a 2D dictionary to store stats for each card, ensuring flexibility and efficient data management.

* **User Interaction:** Implemented a menu-driven program allowing users to pick cards, choose stats, and determine winners.

* **Score Tracking:** Added functionality to keep track of points scored in a two-player format.

### 🔍 Key Concepts:

* **Nested Dictionaries:** Stored each card’s stats (e.g., intelligence, handsomeness, coding skill) as a sub-dictionary within a main dictionary, with the card’s name as the key.

* **Infinite Loops for Gameplay:** Used a loop to continuously allow players to pick cards, choose stats, and play until they decide to quit.

* **Dynamic Gameplay:** Enabled users to add their own cards and stats, making the game customizable.

* **Score Tracking:** Maintained scores for each player to determine the overall winner at the end.

### 💪 Day 47 Challenge:

1. **Enhance Gameplay:**

      * Allow sorting of cards based on a stat before choosing.

      * Add categories with multiple cards for variety.

2. **Advanced Features:**

      * Include a *“play against AI”* mode.

      * Add a timer to make decisions for a more competitive experience.

3. **Visual Enhancements:**

      * Display card stats in a table format.

      * Add ASCII art for a more engaging user experience.


## 🔹 My Code:

![code47 input 1](https://github.com/user-attachments/assets/c9dfb7f1-4757-48af-b259-796220b7bf9b)
![code47 input 2](https://github.com/user-attachments/assets/1c12f434-537a-42d7-93b3-fede16f3df16)
![code47 output](https://github.com/user-attachments/assets/19f56b91-7eb5-4078-94ce-53eaa0f39ccb)
![code47 output 1](https://github.com/user-attachments/assets/e615d4f6-5b08-415f-8227-14f9c635c30d)


### 🛠 Common Challenges & Fixes:

1. **Stat Mismatch:**

     * Issue: Selecting a stat not present in both cards caused errors.

     * Fix: Validated user input to ensure the selected stat exists for both cards.

2. **Unclear Winner:**

      * Issue: When stats were equal, the program didn’t handle ties properly.

      * Fix: Added a condition to handle ties and display a tie message.

4. **Adding New Cards:**

      * Issue: Users could accidentally add incomplete or malformed cards.

      * Fix: Added input validation to ensure all required stats are provided before saving a new card.

**Unleash your creativity and take your Top Trumps game to the next level!** 🃏🚀
