mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

for name, value in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")
