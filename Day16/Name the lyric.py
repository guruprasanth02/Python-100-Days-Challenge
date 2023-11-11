print("Welcome to Name the Song Lyric")

print("Figure out the missing word as quickly as you can!")

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")
