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
