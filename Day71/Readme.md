# 🌟 Day 71: Login System with Password Hashing & Salt 🛡️🔑

### 🎊 Today’s Highlights:

* **Password Hashing:** We learned how to securely store user passwords by hashing them, so even if our database is compromised, passwords can't be easily reversed.

* **Salting:** To enhance security, we introduced salts—random values appended to passwords before hashing. This ensures that even if two users have the same password, their stored hashes will be unique.

* **Building a Login System:**  Using the hashing and salting techniques, we built a login system that:

     * Asks for a username and password.
     * Hashes the password along with a unique salt before storing it.
     * Verifies the input password by hashing it with the stored salt and comparing it to the stored hash.

### 🔍 Key Concepts:

* **Hashing:** A one-way transformation of a password into a fixed-length value, which is stored in place of the actual password. It's nearly impossible to reverse the hash back into the original password.

* **Salt:** A random value added to a password before hashing. This ensures that even if multiple users have the same password, their hashes are different, making it harder for attackers to use precomputed hash databases (rainbow tables).

* **Secure Password Storage:** The importance of using hashing and salting to store passwords securely. This prevents attackers from easily accessing user passwords if the database is compromised.

### 👉 Day 71 Challenge: Build a Login System Overview:

**The program should:**

1. Allow the user to either **Add User** or **Login**.

2. **Add User** should:
    * Prompt for a username and password.
    * Generate a random 4-digit salt.
    * Append the salt to the password, hash the result, and store the hash along with the salt in a dictionary.

3. **Login should:**
    * Prompt for the username and password.
    * Retrieve the salt for that username from the database, append it to the input password, hash the result, and compare it with the stored hash to authenticate the user.

**Example:**
```yaml
Copy code
🌟Login System🌟
1: Add User, 2: Login >  1
Username: > Kenny
Password: > L0gg1ns
Details stored.
1: Add User, 2: Login >  2
Username: > Kenny
Password: > L0gg1ns
Login successful
```

### 🛠️ Common Errors Encountered:

* **Incorrect Hash Comparison:** Often, the password is compared directly without hashing it with the salt. This will cause the login to fail because the hash of the entered password (without salting) will never match the stored hash.

  **Fix:** Always hash the entered password with the salt and then compare the hashes.

* **Misplaced Salt:** The salt should be added to the password before hashing. Mixing the order (e.g., adding salt after hashing) leads to incorrect results.

  **Fix:** Ensure that the salt is appended to the password before hashing, not afterward.

* **Missing Salt Storage:** If the salt is not stored with the hash, it’s impossible to verify the password during login.

  **Fix:** Store both the hash and the salt for each user.

### My Code:
```python
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
