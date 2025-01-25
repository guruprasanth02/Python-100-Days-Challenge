# 🌟 Day 85: Login System with Sessions and Logout Feature 🔐

### 🎉 Today’s Highlights:

* **Sessions in Flask:** Implemented sessions to store login information, allowing us to track user state across pages.

* **Login and Logout Features:** Created login and logout pages to manage user authentication, including session management and redirection.

* **Restrict Access:** Added checks to prevent users from accessing pages without being logged in.

### 🔍 Key Concepts:

* **Session Management:** Utilized Flask's session feature to store user data (like username) persistently across multiple requests.

* **Redirection and URL Routing:** Used Flask's routing to manage login, logout, and restricted access to specific pages.

* **Security Considerations:** Made sure to clear the session when logging out to prevent unauthorized access.

### 💪 Day 85 Challenge:

* Extend the Login System:

    * Modify the login system to remember the user's login state across page reloads using sessions.
   
    * Add a "Logout" button on each page that clears session data and redirects to the login page.
    
    * Implement checks to ensure that users cannot access any page (except for login) unless they are logged in.

### 💪 Common Challenges & Fixes:

* **Session Not Retained After Reload:**

     * **Issue:** The session data wasn't persisting across requests.

     * **Fix:** Ensure Flask's ```session``` object is used correctly, with a properly configured secret key.

* **Redirect Logic:**

     * **Issue:** Users were able to access restricted pages without being logged in.

     * **Fix:** Added proper redirection logic to redirect users to the login page if they were not logged in.

* **Logout Button Not Clearing Session:**

     * **Issue:** Session was not being cleared properly on logout.

     * **Fix:** Used ```session.clear()``` to clear session data on logout.

### 🔹 My Code:
```python
from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionkey']

@app.route('/signup', methods=["POST"])
def createuser():
  if session.get("loggedIn"):
    return redirect("/welcome")
  keys =db.keys()
  form =request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name":form["name"], "password":form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route('/login', methods=["POST"])
def dologin():
  if session.get("loggedIn"):
    return redirect("/welcome")
  keys =db.keys()
  form =request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"]==db[form["username"]]["password"]:
      session["loggedIn"] = form["username"]
      return redirect("/welcome")
    else:
      return redirect("/login")  

@app.route('/welcome')
def welcome():
  page = f"""<h1>Hi there {db[session["loggedIn"]]["name"]}
 </h1>
 <button type="button" onclick="location.href='/logout'">Logout</button>"""
  return page

@app.route('/logout')
def logout():
  session.clear()
  return redirect("/")

@app.route("/login")
def login():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page=""
  f = open("login.html", "r")
  page =f.read()
  f.close()
  return page

@app.route("/signup")
def signup():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page=""
  f = open("signup.html", "r")
  page =f.read()
  f.close()
  return page

@app.route('/')
def index():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page = """<p><a href = "/signup">Sign up</a></p><p><a href = "/login">Log in</a></p>"""
  return page


app.run(host='0.0.0.0', port=81)
