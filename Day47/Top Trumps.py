import os, time, random

trumps = {}
trumps["Guru"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["vishaal"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Nithish"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Pawan"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Pick your character\n> ")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

  answer = input("> ")

  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")


  time.sleep(2)
  os.system("clear")
