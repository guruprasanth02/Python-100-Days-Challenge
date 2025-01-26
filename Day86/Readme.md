# 🌟 Day 86: Building a Fully Functional Blog Engine 📝💻

### 🎊 Today’s Highlights:

* **Blog Engine Creation:** We built a simple blog engine that allows a user to log in and manage posts.

* **Login Functionality:** We created a login page that only allows one user (you) to access the admin dashboard and add new posts.

* **Replit DB Integration:** We integrated Replit’s database to store and retrieve blog posts, enabling us to add new posts and display them on the main blog page.

* **Two Views:**

    * If logged in, you can see a list of existing posts and add new posts via a form.
    
    * If not logged in, the blog posts are displayed in a continuous feed with a login button at the top.

### 🔍 Key Concepts:

* **Login System:** A basic login system that grants access to the admin dashboard where posts can be added or managed.

* **Database Integration:** Storing and retrieving data with Replit DB to persist blog posts between sessions.

* **Conditional Rendering:** Depending on whether you're logged in or not, the layout and available features change.

* **User Authentication:** Simple authentication is used to secure the admin features from public access.

### 👉 Day 86 Challenge: Blog Engine Overview:

* Create a **login page** for user authentication (just for one user).

* Once logged in, users should be able to:

    * View a list of existing blog posts (stored in Replit DB).
    
    * Add new posts through a text input and submit them to the blog.

* If not logged in, users should see:

    * A feed of the blog posts (most recent first).

    * A button to log in.

### 🛠️ Common Errors Encountered:

* **Not Saving Posts:** If posts aren't being stored correctly, it could be an issue with how the data is being written to or read from Replit DB.

     * **Fix:** Ensure the data is being properly serialized (converted to a suitable format) before saving to the database.

* **Login Loop:** A common issue when a session isn’t being correctly tracked, causing users to be redirected back to the login page even if logged in.

     * **Fix:** Use session or token-based authentication to maintain the login state across page reloads.

* **UI/Layout Issues:** If the blog page doesn’t render correctly or the login form is out of place.

     * **Fix:** Double-check the HTML and CSS for correct structure and styling.

### My Code Example:
```python
from flask import Flask, redirect, session, request
from replit import db
import os
app = Flask(__name__,static_url_path= '/static')
app.secret_key = os.environ["secretkey"]

def getBlogs():
  entry = ""
  f = open("entry.html", "r")
  entry = f.read()
  f.close()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content
  
@app.route('/')
def index():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("blog.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/loginForm')
def loginForm():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("login.html", "r")
  page = f.read()
  page = page.replace("{content}", getBlogs())
  f.close()
  return page

@app.route('/login', methods=["POST"])
def login():
  if session.get("user"):
    return redirect("/edit")
  form = request.form
  if form["username"] == db["user"]["username"] and form["password"] == db["user"]["password"]:
    session["user"] = True
    return redirect("/edit")
  else:
    return redirect("/loginForm")

@app.route("/edit")
def edit():
  if not session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("edit.html", "r")
  page = f.read()
  page = page.replace("{content}", getBlogs())
  f.close()
  return page

@app.route("/add", methods=["POST"])
def add():
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "body": form["body"]}
  db[form["date"]] = entry
  return redirect("/edit")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")
  
app.run(host='0.0.0.0', port=81)
