import os

while True:
  username = input("Username: ")
  password = input("Password: ")
  if username == os.environ['adminusername'] and password == os.environ['adminpassword']:
    print("Welcome Admin")
    break
  elif username ==  os.environ['username'] and password == os.environ['password']:
    print("Welcome Normy")
    break
else:
  print("Try again")
