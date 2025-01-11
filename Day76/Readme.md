# 🌟 Day 76: Flask Web Server with Multiple Pages and Endpoints 🌐✨

### 🎊 Today’s Highlights:

* **Flask Fundamentals:** We worked with Flask to create a basic web server and explore the core concepts of routing and serving dynamic content. Flask allows us to build websites that respond differently based on user interactions.
* **Multiple Pages:** We expanded our Flask app to handle multiple pages, enabling navigation between different routes such as a homepage and a portfolio page.
* **Static Files:** We also learned how to include static files like images in our Flask app by storing them in the ```static``` folder and linking them correctly in our HTML.
* **Dynamic Content:** Using f-strings, we integrated dynamic content like the current date into our pages, making the site interactive and responsive.

### 🔍 Key Concepts:

* **Flask Routes:** Each route in Flask represents a different page or endpoint. We can define what content each page should show.
* **Static Files:** These are files that don't change and are served directly, such as images, stylesheets, and JavaScript files.
* **f-Strings in Flask:** f-strings allow us to embed variables into strings easily, which is useful for dynamically generating HTML content in Python.
* **Linking Pages:** We learned to navigate between different pages by creating hyperlinks between routes.

### 👉 Day 76 Challenge: Flask Web Server with Two Endpoints

* **Task Overview:** The challenge is to build a Flask server with two endpoints: ```/portfolio``` and ```/linktree```. Each endpoint will serve its respective page, showcasing a portfolio and a linktree.

     * **/portfolio Page:** Create a page to showcase your portfolio (you can include details like your work, skills, and projects).

     * **/linktree Page:** Create a page to serve as a linktree, linking to your social media or other important links.

🛠️ Common Errors Encountered:

* **Missing Static Folder:** Make sure the ```static``` folder exists to serve images and files correctly.

* **Incorrect Routing:** Ensure routes are defined correctly for the different pages. Flask requires distinct functions to handle different URLs.

**Fixes:**

* **Static Folder Issue:** Created a folder named static for storing images and other assets.

* **Route Confusion:** Each page (like ```/portfolio``` and ```/linktree```) should have its own route function to ensure Flask knows what to display at each URL.


### My Code:
```python
from flask import Flask
import datetime 

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/home') 
def home():
  today = datetime.date.today()
  page = f"""html 
  # Format the html as an fString
  <html>

  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <h2>{today}</h2> #Drop the date variable inside curly braces.

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="static/images/picard.jpg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>

</body>

</html>

  """
