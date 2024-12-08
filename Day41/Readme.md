# 🌟 Day 41: Website Information Using Dictionary 🌐💻

#### 🎊 Today’s Highlights:

* **Dictionaries with Loops:** We worked with dictionaries to store key information about a website, such as its name, URL, description, and star rating.
* **User Input Collection:** We prompted the user to input details about the website using ```input()``` and stored these details in a dictionary.
* **Formatted Output:** After collecting the data, we looped through the dictionary to print both the keys and the corresponding values in a user-friendly way.
* **Using Split Function:** To make the input process more efficient, we explored using a single ```input()``` command to gather all the necessary details and used the ```split()``` function to separate them.

### 🔍 Key Concepts:

* **Dictionaries:** We utilized dictionaries to store structured data in key-value pairs. This made it easier to store related information about a website, such as its name, URL, description, and rating, and retrieve it via keys like "name" and "rating."
* **User Input Handling:** We used ```input()``` to collect the website’s details (name, URL, description, and rating) from the user, and stored them in a dictionary. This method allowed for dynamic data collection and helped customize the stored information.
* **Looping Through Dictionaries:** We looped through the dictionary using ```.items()``` to print both the keys and their respective values. This method ensured we could display all the information in a clean and readable format.
* **Using the ```split()``` Function:** We learned how to efficiently collect multiple pieces of information with a single input command and use split() to separate them, improving the overall flow of the program.

### 👉 Day 41 Challenge: Website Dictionary Task Overview:

* Create a dictionary that stores information about a website, including:
    * **Name:** The website’s name.
    * **URL:** The website’s URL.
    * **Description:** A short description of the website.
    * **Rating:** A star rating out of 5 (e.g., ```*****```).
* Use a loop to output the names of the keys, ask the user to type in the details, and store the input in the dictionary.
* Finally, output the entire dictionary (keys and values).

### 🛠️ Common Errors Encountered:

* **Missing or Incorrect Inputs:** If the user misses a field or inputs an incorrect value (e.g., entering a non-numeric rating), the program might fail or produce unexpected results.

   **Fix:** Ensure that the user provides all required information, possibly using validation checks (e.g., confirming the rating is a valid star count).

* **Incorrect Use of ```split()```:** Sometimes, users might not correctly split the inputs into the right format.

   **Fix:** Double-check how the input is split, and make sure the correct number of values are assigned to the dictionary.

* **Incorrect Key Handling in Loops:** If there’s confusion when looping through the dictionary and accessing values, errors like ```KeyError``` can occur.

   **Fix:** Ensure you use the correct loop format with ```.items()``` and handle key-value pairs properly.

### My Code:
```python
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
