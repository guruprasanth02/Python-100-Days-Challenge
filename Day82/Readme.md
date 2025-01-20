
# 🌟 Day 82: Going Bilingual – Creating Multi-Language Pages with Flask 🌍

### 🎊 Today’s Highlights:

* **Introduction to GET and URL Parameters:** We explored the GET method, which allows us to retrieve data from the URL, as opposed to POST, where the data is sent to the server. This is useful for passing simple data, like search queries or settings, which you can share in URLs.

* **Personalization Based on URL Parameters:** By using ```request.args``` in Flask, we can access and utilize data passed through the URL for dynamic, personalized content.

* **Handling Multiple Languages:** We applied GET parameters to create a bilingual page, allowing users to choose their preferred language by modifying the URL.

### 🔍 Key Concepts:

* **GET Method:** The GET method is used to request data from the server and pass it in the URL. This is visible in the URL and can be shared or bookmarked.

* **request.args:** A dictionary-like object that allows access to data sent via the URL, such as query parameters.

* **Dynamic Content:** Based on the data from the URL, we can conditionally display content, such as personal messages or different language pages.

* **Language Handling with Flask:** We can easily create bilingual pages by checking URL parameters and dynamically rendering content in the requested language.

### 👉 Day 82 Challenge: Create a Bilingual Page 🌍

**Task Overview:**

 * Create a web page that can display content in two languages based on the URL parameter.
 
 * If the user accesses the page with ```/english```, the page should show English content.

 * If they access the page with ```/otherLanguage```, it should show the translated page.

### 🛠️ Common Errors Encountered:

* **Missing URL Parameters:** If the URL doesn’t include the expected language parameter, the app may return an error. Ensure a default or error handling mechanism is in place.

* **Incorrect Handling of ```request.args```:** Make sure to access the correct parameter in the ```request.args``` object and handle cases where parameters may be missing or empty.

* **Routing Errors:** When handling different languages or page routes, ensure that the routes are defined correctly to match the expected URL structure.


### My Code:
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/language', methods=["GET"])
def lang():
   data = request.args
   if data == {}:
    return "Nothing here"
   if data["lang"] == "eng":
      return "Hello, and welcome to our wonderful website!"
   elif data["lang"] == "ta":
      return "வணக்கம், எங்கள் அற்புதமான வலைத்தளத்திற்கு வரவேற்கிறோம்!"
  
@app.route('/')
def index():
  return "Hello from Flask"

app.run(host='0.0.0.0', port=81)
