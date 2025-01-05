# ✨ Day 70: Login System with User Types 👤🔐

### 🎉 Today’s Highlights:

* **Two Types of Users:** Implemented a system with different usernames and passwords for admin and normal users.
* **User Authentication:** Created a simple password-checking mechanism to authenticate users.
* **Custom Greetings:** Personalized the greeting based on the user's type—admin or normal.

 ### 🔍 Key Concepts:

* **Environment Variables:** Learned how to securely store passwords using environment variables to keep sensitive information hidden.
* **User Input:** Used ```input()``` to gather username and password data from the user.
* **Conditional Statements:** Incorporated ```if-else``` statements to differentiate the responses based on the type of user (admin vs. normal).
* **Simple Authentication System:** Implemented a basic authentication flow to check passwords and validate user login.

### 🔧 Implementation Steps:

1. **Setting Up Secrets:**

      * Utilized the secrets tab in Replit to store passwords securely.
      * Created a key for the password in the secrets menu to keep it hidden from prying eyes.

2. **Password Access:**

      * Retrieved the password stored in secrets using the os.environ['password'] method.
      * Used the input() function to prompt the user for their password.

3. **Login Validation:**

      * Compared the entered password with the stored password.
      * Printed a corresponding message based on whether the password matched.

4. **Handling Multiple Users:**

      * Created distinct usernames and passwords for the admin and normal users.
      * Greeted the admin with "Hello admin" and the normal user with "Hello normie."

### 💪 Day 70 Challenge:

* **Create a Login System for Two Types of Users:**

     * The program should prompt for both the username and password.
     * Based on the credentials, the system should either greet the admin with "Hello admin" or the normal user with "Hello normie."

**Example Output:**

🌟Login System🌟

Username > admin01

Password > thepowerTHEPOWER

Hello admin

### 🛠️ Common Challenges & Fixes:

* **KeyError (when no secret is set):**

     * Issue: The error "KeyError" happens when trying to access a secret that has not been set in the secrets tab.

     * Fix: Make sure the secret is properly added in Replit's secret manager, and the key matches the one used in the code.

* **Wrong Username/Password Handling:**

     * Issue: The user input doesn't match the expected username or password.

     * Fix: Double-check the values entered for the username and password and ensure they match the secret data set.

* **Incorrect Indentation:**

     * Issue: ```If else```: is not properly indented, the program will throw an indentation error.

     * Fix: Ensure that ```else```: aligns correctly under the ```if``` statement.

### 🔹 My Code:
```python
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


