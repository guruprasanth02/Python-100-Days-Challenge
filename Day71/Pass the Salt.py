import os, time, random
from replit import db

def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  
  db[username] = {"password": newPassword, "salt": salt}

  print("User added")

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return

  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[username]["password"]==newPassword:
    print("Logged in")
  else:
    print("Username or password incorrect")


while True:
  menu = input("1: New User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])
