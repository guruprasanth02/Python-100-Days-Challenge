# 🌟 Day 40: Contact Card Using Dictionary 📇📱

### 🎊 Today’s Highlights:

* **Dictionaries in Action:** We used dictionaries to store multiple pieces of information about a user, which is more efficient than lists when accessing values using keys.
* **User Input Collection:** We prompted the user to input key personal details like name, date of birth, telephone number, email, and address.
* **Formatted Output:** Once the information was stored in the dictionary, we formatted and printed it in a user-friendly way.

### 🔍 Key Concepts:

* **Dictionaries:** We learned that dictionaries are made up of key-value pairs, where each key uniquely identifies its corresponding value. This is especially useful when storing related information that needs to be accessed via the key (e.g., "name" or "email").
* **User Input Handling:** We took multiple user inputs using the input() function and stored them in dictionary values. This allowed us to create a personalized contact card.
* **Formatted Printing:** Using f-strings, we output the dictionary data in a readable format, showcasing how easily we can pull information from a dictionary using its keys.

### 👉 Day 40 Challenge: Contact Card Task Overview: Write a program that:

   1. Asks the user to input their name, date of birth, telephone number, email, and physical address.
   2. Stores this information in a dictionary with descriptive keys.
   3. Outputs the information in a friendly, readable format using an f-string.

### 🛠️ Common Errors Encountered:

* **Missing Keys:** When the user forgets to input one of the required details, the dictionary might not contain all the expected keys. This can cause an error when trying to access a missing key.

   **Fix:** Use input() to ensure that all fields are filled and consider adding checks to confirm that the user has entered information for every field.

* **Incorrect Key Names:** If you use inconsistent key names in your code (e.g., name vs Name), it can lead to errors when trying to access the dictionary values.

   **Fix:** Be consistent with your key names and make sure to use the exact key when retrieving values from the dictionary.

* **Missing f-String Formatting:** Forgetting to use f-strings or proper string formatting when printing out the contact card can result in unclear or improperly formatted output.

   **Fix:** Always use f-strings to easily embed variables into your string output and ensure the result is user-friendly.


### My Code:
```python
name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")
