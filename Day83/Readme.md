# 🌟 Day 83: Adding Custom Themes to Your Blogging Engine 🎨

### 🎊 Today’s Highlights:

* **Custom Themes Implementation:** We learned how to dynamically change the look and feel of a web page by passing a theme name via the URL.

* **GET Requests for Theme Switching:** By passing a ```theme``` variable in the URL, we can swap between different visual styles for the website.

* **Flask Template Customization:** We used Flask's ability to render different HTML templates based on URL parameters to give the user a personalized experience with custom themes.

* **Creating Multiple Themes:** We added at least two distinct themes, each with different color schemes, to demonstrate the versatility of dynamic theming.

### 🔍 Key Concepts:

* **GET Requests with URL Parameters:** We accessed URL parameters to adjust the behavior and appearance of the website dynamically.

* **Dynamic Template Rendering:** Flask allows us to change how content is rendered by passing in variables, which helps create personalized, theme-based user experiences.

* **CSS Styling Based on Parameters:** We modified the HTML structure and applied custom CSS depending on the selected theme.

### 👉 Day 83 Challenge: Add Custom Themes to Your Blog 🎨

**Task Overview:**

* Modify the blogging engine from Day 77 to support dynamic theme switching based on the URL parameter ```theme```.

* When the user visits the page with ```/theme/<theme_name>```, it should apply a specific theme to the page.

* If no theme is provided, a default theme should be applied.

### 🛠️ Common Errors Encountered:

* **Incorrect Theme Logic:** Be careful to check if the theme parameter exists in the URL and provide a default if it’s missing.

* **CSS Issues:** Ensure that the CSS for each theme is properly linked and that different themes don’t conflict with each other.

* **Template Rendering:** Verify that Flask’s ```render_template``` is correctly applying the passed parameters for theme changes.

### My Code:
```python
from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  page = ""
  return page

@app.route('/blog/hello')
def hr():
  return redirect("/hello")

@app.route('/blog/bye')
def br():
  return redirect("/bye")

@app.route('/hello', methods = ["GET"])
def hello():
  data = request.args
  template = "default"
  if data != {}:
      template = data["template"]
  title = "Hello World"
  date = "Febuary 6th"
  text = "Here is my first blog entry."
  page = ""
  with open("template/blog.html", "r") as f:
      page = f.read()
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)
  page = page.replace("{template}", template)

  return page

@app.route('/bye', methods = ["GET"])
def bye():
  data = request.args
  template = "fancy"
  if data != {}:
      template = data["template"]
  title = "Bye World"
  date = "October 6th"
  text = "Here is my last blog entry."
  page = ""
  with open("template/blog.html", "r") as f:
      page = f.read()
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)
  page = page.replace("{template}", template)

  return page

app.run(host='0.0.0.0', port=81)
