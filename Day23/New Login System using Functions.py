def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "Replit4ev#r":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue

print("REPLIT LOGIN SYSTEM")
login()
