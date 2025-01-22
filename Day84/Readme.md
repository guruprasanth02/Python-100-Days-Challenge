# 🌟 Day 84: Building a Signup and Login System with Flask 🔐

### 🎊 Today’s Highlights: 

* We explored how to create a Flask web application with a **signup** and **login** system using **Replit DB** to store user data. This exercise is designed to let users create an account, log in, and dynamically interact with their profile.

* **Signup Form:** Users can create an account by providing their name, username, and password. This data will be stored in Replit DB.

* **Login Form:** After signing up, users can log in with their username and password to access their personalized page.

* **Data Persistence:** The user information is saved in a persistent database using Replit DB, ensuring that even if the application restarts, the user data remains intact.

### 🔍 Key Concepts:

* **Flask Routes:** We used Flask to create routes for signing up, logging in, and handling user data.

* **Replit DB:** Replit's database is used to persistently store user data (username and password).

* **HTML Forms:** Forms are used to take user input for both signup and login.

* **Redirects:** After a successful login, users are redirected to a welcome page.

### 👉 Day 84 Challenge: Build a Flask Web Application with Signup and Login System

**Task Overview:**

1. **Create a signup page** with fields for **name**, **username**, and **password**.

2. Store the user details in the **Replit DB**.

3. Once signed up, redirect users to the login page.

4. **Login:** Allow users to log in with their username and password.

5. Upon successful login, show a personalized greeting (e.g., "Hello, [Name]!").

### Common Errors Encountered:

* **KeyError:** If the user does not exist in the database, attempting to access the user’s details would result in a KeyError. This is handled in the code by checking if the username exists in the database before comparing the password.

* **Form Submission:** Ensure that the method is set correctly in the form tags (```method="POST"``` for submitting data).

* **Redirects:** Make sure the user is redirected to the correct page after signup or login.

### My Code:
```python
from flask import Flask, request, redirect
from replit import db

app = Flask(__name__)

@app.route('/signup', methods=["POST"])
def createuser():
  keys =db.keys()
  form =request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name":form["name"], "password":form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route('/login', methods=["POST"])
def dologin():
  keys =db.keys()
  form =request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"]==db[form["username"]]["password"]:
      return f"""Hello {db[form["username"]]["name"]}"""
    else:
      return redirect("/login")  

@app.route("/login")
def login():
  page=""
  f = open("login.html", "r")
  page =f.read()
  f.close()
  return page
  
@app.route("/signup")
def signup():
  page=""
  f = open("signup.html", "r")
  page =f.read()
  f.close()
  return page

@app.route('/')
def index():
  page = """<p><a href = "/signup">Sign up</a></p><p><a href = "/login">Log in</a></p>"""
  return page


app.run(host='0.0.0.0', port=81)

