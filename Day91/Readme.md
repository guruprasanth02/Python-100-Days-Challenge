# 🌟 Day 91: Random Dad Jokes API 🎉

### Today’s Highlights:

* **Working with APIs:** We explored how to access and retrieve random dad jokes using the icanhazdadjoke API. This taught us the fundamentals of making requests to an external service and handling the response in JSON format.

* **Making Requests:** We used the ```requests``` library to get data from the API and learned the importance of using headers to specify the data format (JSON).

* **Processing JSON Data:** After receiving the joke data, we parsed it and extracted the joke text to display it in the console.

### 🔍 Key Concepts:

* **API Requests:** How to use the ```requests.get()``` method to make an API call and handle the response.

* **Headers in Requests:** We learned how the headers (```"Accept": "application/json"```) tell the server what kind of data format we want back.

* **JSON Parsing:** Once we received the response, we worked with the ```json()``` method to turn the raw response into a Python dictionary and extract the joke.

### 💪 Day 91 Challenge: Dad Jokes with a Twist

Task Overview:

  * Create a program that gives you a random dad joke using the icanhazdadjoke API.
  
  * After displaying the joke, ask the user if they would like to save it.
 
  * If the user chooses to save the joke, store it in a database (e.g., Replit DB).
  
  * Ask the user if they want to see all saved jokes and display them from the database.

### 🚨 Common Errors Encountered:

* **Incorrect Header Formatting:** If the ```"accept"``` header is incorrectly capitalized (e.g., ```"Accept"``` vs. ```"accept"```), the request may fail.

     * **Fix:** Ensure proper capitalization in the headers.

* **JSON Parsing Errors:** Sometimes the response might not be as expected, or an error can occur when trying to parse the JSON.

     * **Fix:** Use a try-except block to handle potential parsing errors.

* **Database Errors:** Trying to store or retrieve data from the Replit DB without proper setup.

     * **Fix:** Ensure the Replit DB is correctly initialized and the data is stored/retrieved as intended.

### 🚀 My Code:
```python
import requests, json, os, time
from replit import db

while (True):
  time.sleep(1)
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  joke = result.json()

  jk = joke["joke"]
  id = joke["id"]
  print(jk)

  answer = input("\n(s)ave joke, \n(l)oad jokes, \n(n)ew joke\n> ").lower()
  if answer == "n":
    continue
  elif answer == "s":
    db[id] = jk
    print("\nSaved\n")
    continue
  else:
    keys = db.keys()
    for key in keys:
      result = requests.get(f"https://icanhazdadjoke.com/j/{key}" , headers={"Accept":"application/json"})
      joke = result.json()
      print(joke["joke"])
      print("\n")
      time.sleep(1)
print(joke["joke"])
print(joke["joke"])
print(joke["joke"])
```


**Happy coding! 🚀 Let your creativity shine as you work through the challenge of saving and displaying dad jokes. Enjoy the fun of coding and working with APIs!** 😄
