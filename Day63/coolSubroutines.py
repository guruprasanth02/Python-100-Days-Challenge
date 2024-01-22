def newPrint(color):
  if color=="red":
    print("\033[31m", sep="", end="")
  elif color=="green":
    print("\033[32m", sep="", end="")
  elif color=="blue":
    print("\033[34m", sep="", end="")
  else:
    print("\033[0m", sep="", end="")
