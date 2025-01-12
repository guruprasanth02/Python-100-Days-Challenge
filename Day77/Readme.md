# 🌟 Day 77: Blog Template Challenge 📝

### 🎊 Today’s Highlights:

* **Template Creation:** We explored how to create a reusable template for blog entries. This involved setting placeholders for heading, date, and text within an HTML file, which could be dynamically populated in Flask routes.
* **Dynamic Content Injection:** We learned how to insert dynamic data (such as blog titles, dates, and content) into HTML templates using string manipulation techniques, enabling us to create multiple unique blog entries with a single template.
* **URL Redirection:** We also implemented URL redirects, enabling users to access different blog entries by appending simple, user-friendly paths to the main URL.

### 🔍 Key Concepts:

* **Flask Templating:** Using basic templating techniques with ```replace()``` to create dynamic content for a webpage.
* **String Manipulation:** Replacing placeholders in HTML files with dynamic values (e.g., blog titles, dates, and content).
* **Redirecting URLs:** Using Flask’s ```redirect()``` function to map simple paths to long URLs, effectively shortening the URL structure.

### 👉 Day 77 Challenge: Setting up a Blog Template

**Task Overview:**

   * **Template Structure:** Create an HTML template that has space for a heading, a space for today's date, and a space for the text.
   * **Blog Entries:** Write two different blog entries and serve them on two different endpoints. Both blog entries should use the same template, with content dynamically injected.
   * **URL Redirection:** Implement shortened URLs for each blog entry, making it easy to access each one with a simple path.

**Example:**
```html
Copy code
<!-- template/blog_entry.html -->
<body>
  <h1>{heading}</h1>
  <p><strong>{date}</strong></p>
  <p>{text}</p>
</body>
```

### 🛠️ Key Errors You May Encounter:

1. **Incorrect File Handling:** Remember to always use ```with open()``` to ensure files are properly closed after reading. This prevents file access issues.

2. **String Replacement Issues:** When replacing placeholders in the template, ensure the correct syntax is used (i.e., the variable names must match the placeholders in the HTML).

3. **Redirection Syntax:** The ```redirect()``` function requires the URL in a string format. Make sure the URL is valid and correctly placed within the function.

### My Code:
```python
from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  page = ""
  return page

@app.route('/blog/hello')
def hr():
  return redirect("/hello")

@app.route('/blog/bye')
def hr():
  return redirect("/bye")
  
@app.route('/hello')
def index():
  title = "Hello World"
  date = "Febuary 6th"
  text = "Here is my first blog entry."
  page = ""
  f = open("template/blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)
 
  return page

@app.route('/bye')
def index():
  title = "Bye World"
  date = "October 6th"
  text = "Here is my last blog entry."
  page = ""
  f = open("template/blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)

  return page
  
app.run(host='0.0.0.0', port=81)
