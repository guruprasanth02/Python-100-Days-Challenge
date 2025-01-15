# 🌟 Day 80: Login Form Integration with Flask 🎉

### 🎊 Today’s Highlights:

* **Flask Integration:** We connected a login form to Flask, allowing it to handle user input and direct users based on their credentials.

* **User Authentication:** By storing valid username and password combinations, we created a basic form of authentication for users trying to log in.

* **Conditional Pages:** For valid users, we displayed a welcoming "nice" page, and for incorrect login attempts, we sent them to a "naughty step" page as a way to prevent unauthorized access.

* **User Input Handling:** We worked with form data in Flask, utilizing the request object to process and validate inputs.

### 🔍 Key Concepts:

* **Flask Form Handling:** We used Flask’s ```request.form``` to retrieve and process form data submitted via POST requests.

* **Conditional Logic:** Implementing if statements in Flask routes helped us decide what page to render based on the user’s input (valid or invalid).

* **Security Considerations:** By validating user credentials, we practiced basic user authentication principles, improving security for web applications.

* **Error Handling:** We used logic to guide users to appropriate pages depending on their login attempts, which helps in managing incorrect inputs effectively.

### 👉 Day 80 Challenge: Login Form with Flask Task Overview:

* **Login Form:** Create a login form that accepts a username and password.

* **Valid User Check:** The form should authenticate the user against three valid username-password pairs.

* **Conditional Responses:** After submitting the form, redirect users to either a "nice" page for valid users or a "naughty step" page for invalid users.

### 🛠️ Common Errors Encountered:

* **Missing Method Specification:**

     **Problem:** Forgetting to specify the HTTP method in ```@app.route()``` can cause the app to fail or respond unexpectedly.

     **Fix:** Ensure that the route specifies ```methods=["POST"]``` for form submissions.

* **Form Input Name Mismatch:**

     **Problem:** The ```name``` attribute in HTML form inputs doesn’t match the expected keys in the Flask ```request.form``` dictionary.

     **Fix:** Double-check that the input field names in the HTML match those in the Flask route handling the form data.

* **Incorrect Redirect Logic:**

     **Problem:** Routing users incorrectly or not providing a clear feedback message on login attempts can confuse users.

     **Fix:** Ensure correct logic for valid and invalid logins, and provide user-friendly messages that clearly indicate the outcome of their submission.

### My Code:
```python
from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["guru"] = {"email": "guru@gmail.com", "password": "1234"}
logins["ben"] = {"email": "ben@gmail.com", "password": "ten10"}
logins["kevin"] = {"email": "kevin@gmail.com", "password": "in11"}

@app.route("/login", methods=["POST"])
def login():
  form = request.form
  isthere = False
  details = {}
  try:
    details = logins[form["username"]]
    isthere = True
  except:
    return "Username, email or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
     return "Username, email or password incorrect"

@app.route('/')
def index():
  page = """<form method = "post" action = "/login">
      <p>Username: <input type="text" name="username" required></p>
     <p>Email: <input type="email" name="email" required></p>
     <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Login</button>
  </form> """
  return page

app.run(host='0.0.0.0', port=81)
