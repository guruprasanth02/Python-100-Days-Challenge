import requests, json, os, time
from replit import db

while (True):
  time.sleep(1)
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  joke = result.json()

  jk = joke["joke"]
  id = joke["id"]
  print(jk)

  answer = input("\n(s)ave joke, \n(l)oad jokes, \n(n)ew joke\n> ").lower()
  if answer == "n":
    continue
  elif answer == "s":
    db[id] = jk
    print("\nSaved\n")
    continue
  else:
    keys = db.keys()
    for key in keys:
      result = requests.get(f"https://icanhazdadjoke.com/j/{key}" , headers={"Accept":"application/json"})
      joke = result.json()
      print(joke["joke"])
      print("\n")
      time.sleep(1)
print(joke["joke"])
print(joke["joke"])
print(joke["joke"])
