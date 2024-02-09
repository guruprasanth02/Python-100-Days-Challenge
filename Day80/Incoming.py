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
