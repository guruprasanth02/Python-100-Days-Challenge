# 🌟 Day 93: Spotify Music Search App Challenge 🎶

![code93 input](https://github.com/user-attachments/assets/ea83d33f-d4d7-43d0-9b72-082ff7670987)

### 🎊 Today’s Highlights:

* **Connecting to Spotify API:** Learn how to authenticate and connect to Spotify’s music data.

* **Search Implementation:** Implement a search function to retrieve songs by artist.

* **Dynamic User Interaction:** Customize the search query based on user input and show relevant song results.

* **Music Preview:** Embed a 30-second preview of each song found.

### 🔍 Key Concepts:

* **API Authentication:** Learn to authenticate via client credentials and obtain an access token.

* **API Requests:** Use the token to interact with Spotify’s public API to search for tracks.

* **Dynamic Query Construction:** Build a query that allows users to input an artist and retrieve results based on that input.

* **JSON Data Handling:** Parse and display the relevant song details from the API response.

### 👉 Day 93 Challenge: Spotify Music Search Web App

Create a simple Flask app that interacts with Spotify’s API to fetch song results for a given artist. The app should:

  1. **Authenticate:** Connect to Spotify using client credentials and obtain an access token.

  2. **User Input:** Allow the user to enter an artist’s name and click a “Go” button to search for songs.

  3. **Search Query:** Construct a dynamic query to search Spotify’s database for songs by the entered artist.

  4. **Display Results:** Show 10 songs from the artist along with an embedded mp3 preview of each song.

### 📂 Output:

Output:

![code93 output](https://github.com/user-attachments/assets/11a79aed-3001-42f9-90b4-1790a3bf01e6)

### 🛠️ Common Errors Encountered:

* **Authentication Failure:**

    * **Error:** Incorrect client ID or secret, leading to authentication failure.
    
    * **Fix:** Ensure the correct credentials are stored and passed during the authentication process.

*  **Invalid Search Query:**

     * **Error:** Improper formatting of the search query (e.g., missing parameters or incorrect encoding).

     * **Fix:** Double-check the query string format and ensure correct URL encoding.

* **API Response Handling:**

     * **Error:** API responses may not be properly parsed or handled.

     * **Fix:** Always verify the structure of the response and handle potential errors like missing data.



**Keep building and enjoy discovering music from your favorite artists!** 🎧🚀
