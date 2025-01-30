# 🌟 Day 90: Web Scraping with JSON and Random User API 🌐✨

### 🎊 Today’s Highlights:

* **Introduction to JSON:** We explored how JSON (JavaScript Object Notation) is used to transfer data between websites and applications. By understanding how to parse and interpret JSON as a Python dictionary, we laid the foundation for web scraping.

* **Getting Data from APIs:** We learned how to send requests to websites that provide data in JSON format. For this, we used the **randomuser.me** API to generate random user profiles.

* **Formatting JSON:** We formatted and cleaned up the data to make it more readable using Python's ```json.dumps()``` method with an indentation level.

* **Extracting Specific Data:** We focused on extracting particular data, like a user's name, and displayed it.

* **Saving Images:** We also pulled down profile images from the API and saved them to our local machine.

* **Loops for Multiple Data:** We used loops to process multiple users, making our code more flexible for future projects.

### 🔍 Key Concepts:

* **JSON Parsing:** We learned how to parse JSON into Python dictionaries, which allows us to work with structured data from external APIs.

* **HTTP Requests:** Using the ```requests``` library, we sent GET requests to retrieve JSON data from external websites.

* **Saving Files Locally:** We saved the retrieved profile images as local files using Python’s file handling functions.

* **Loops:** We applied loops to process and display data for multiple users, making our code more scalable.

### 👉 Day 90 Challenge: Task Overview:

* **Goal:** Use the ```randomuser.me API``` to pull in data for 10 users.

* **Tasks:**

   * Save each user's medium-quality profile picture as a local file named ```{firstName}``` ```{lastName}.jpg```.
   
   * Ensure each picture is saved to a separate file.

### 🛠️ Common Errors Encountered:

* **No Data:** Sometimes the request to the API might fail or not return any data. This is typically checked by inspecting the HTTP status code. A status code of ```200``` means everything is fine.

* **JSON Format Errors:** The structure of the JSON can sometimes be confusing, and it’s easy to access the wrong part of the dictionary. Using print statements and ```json.dumps()``` helps to better understand the structure.

* **File Handling Errors:** When writing images, it's important to ensure the correct file mode is used (```"wb"``` for binary files).

* **Fixes:**

  * We added error handling to check for successful requests using the HTTP status code.

  * Carefully navigated the JSON structure to access the required fields like ```results```, ```name```, and ```picture```.

  * Used Python’s file handling functions to save images with appropriate names.

### My Code:
```python
import requests, json

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
#print(json.dumps(user, indent=2)) 

    for person in user['results']:
      filename = f"""{person["name"]["first"].lower()} {person["name"]["last"].lower()}.jpg""" 
      picture = requests.get(person["picture"]["medium"])
      f = open(filename, "wb")
      f.write(picture.content)
      f.close()
      print(f"saved {filename}")
