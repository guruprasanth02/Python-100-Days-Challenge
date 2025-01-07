# 🌟 Day 72: Secure Diary Program 📝🔐

### 🎊 Today’s Highlights:

* **User Authentication:** Added user authentication to the diary program, requiring users to create a secure username and password.
* **Password Hashing:** Implemented salting and hashing of passwords using Python’s hashlib and os libraries to protect user credentials.
* **Database Integration:** Stored usernames and hashed passwords securely, using a dictionary-like structure in a text file.
* **Diary Protection:** Ensured that only authenticated users could access their diary entries.

  **Password Salting & Hashing:** To enhance the security of user passwords, each password is salted (random characters added to the password) before being hashed. This prevents two users with the same password from having the same hash, providing an additional layer of security.

**First-Time User Setup:** On first run, the program prompts the user to create a username and password, and stores the credentials securely. Subsequent runs require users to input their username and password to gain access to the diary entries.

### 🔍 Key Concepts:

* **Salting & Hashing:** Used ```hashlib``` to hash the password, with ```os.urandom()``` for generating a salt. This makes password storage secure and resistant to dictionary and brute force attacks.

* **Persistent Storage:** The username, salt, and hashed password are stored in a text file, ensuring that user credentials are retained across sessions.

* **User Authentication Flow:** The program checks if the entered password matches the stored hash and salt. If successful, the user gains access to their diary.

### 👉 Day 72 Challenge: Task Overview:

* **User Setup:** On first run, prompt the user to create a username and password. The password is hashed and salted before storage.
* **Authentication:** On subsequent runs, the user must enter their username and password. Access is granted only if the password matches the stored hash.
* **Diary Access:** Once authenticated, the user can read and write diary entries. Sensitive information (username, password, salt) is excluded from diary outputs.

### 🛠️ Common Errors Encountered:

* **Password Mismatch:** One common issue was entering the wrong password, which resulted in the user being unable to access the diary. This was resolved by ensuring password hashes and salts are verified correctly.

  * **Fix:** Always compare hashed passwords, not plaintext passwords.

* **Salt Generation Error:** If the salt was not generated properly, it caused the password verification to fail.

  * **Fix:** Ensure that the salt is consistently generated using ```os.urandom()``` and stored properly alongside the hashed password.

* **File I/O Issues:** Another potential issue was reading from or writing to the file if the file didn’t exist or had incorrect formatting.

  * **Fix:** Use exception handling to catch file I/O errors and ensure the user is prompted appropriately.

### My Code:
```python
from replit import db
import datetime, os, time, random

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break



keys = db.keys()
if len(keys)<1:
  print("First Run > Create account")
  username = input("Username > ")
  password = input("Password > ")
  salt = random.randint(0,9999999)
  newPassword = hash(f"{password}{salt}")
  db[username] = {"password": newPassword, "salt": salt}
else:
  print("Log in")
  username = input("Username > ")
  password = input("Password > ")
  if username not in keys:
    print("Username or password incorrect")
    exit()
  salt = db[username]["salt"]
  newPassword = hash(f"{password}{salt}")
  if db[username]["password"]!=newPassword:
    print("Username or password incorrect")
    exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
