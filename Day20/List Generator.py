print("WELCOME TO MY NUMBER LIST GENERATOR.")

print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)
