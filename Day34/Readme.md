# 🌟 Day 34: Spamming Emails with "Spammer Inc." 📧

 ### 🎊 Today’s Highlights:
  * **Email Management:** We created a program to manage a list of emails where users can add, remove, and display email addresses.
  * **Pretty Print:** Implemented a function that displays the email list in a clean, formatted, and numbered list for better readability.
  * **List Indexing:** Explored list indexing and how to access each item in the list using Python’s range() and len() functions.
  * **Spam Functionality:** Added functionality to print out the first 10 emails and simulate sending a spam message to each, clearing the screen after each message.

 ### 🔍 Key Concepts:
  * **List Management:** Storing multiple email addresses in a list and manipulating it through additions, deletions, and display.
  * **Pretty Print Function:** Creating a formatted display of list items using a counter or index to present a numbered list.
  * **Loops and Indices:** Using for loops and list indexing to loop through lists efficiently.
  * **Clear Screen:** Using os.system("clear") to clear the console output, improving the user interface.
  * **String Formatting:** Understanding how to format output using f-strings for clear and structured display.

 ### 👉 Day 34 Challenge: Get SPAMMING!

  ### Task Overview:

   * **Step 1:** Create a list of email addresses.
   * **Step 2:** Implement the ability to add, remove, and display emails with a numbered list.
   * **Step 3:** Implement a spam functionality that loops through the first 10 emails in the list and sends a spam message to each.
   * **Step 4:** Ensure the spam messages are displayed one at a time, pausing between each and clearing the screen before showing the next.

 ### 🛠️ Common Errors Encountered:

   * **Incorrect Looping Through List:** Accidentally using a for loop that doesn't access list indices correctly. 

     **Fix:** Use for index in range(len(list)) to access the correct index of the list.

   * **Missing clear in Loop:** Forgetting to clear the console between spam messages. 

     **Fix:** Use os.system("clear") within the loop to clear the screen before displaying each new email.

   * **Spam Message Not Displayed Properly:** Incorrect formatting or missing f-strings when displaying the spam message.

     **Fix:** Ensure the spam message is printed clearly using f-strings to insert the email address.


### My Code:
```python
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter+=1
  time.sleep(1)

def spam(max):
  for i in range(0,max):
    print(f"""Email {i+1}

Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
    time.sleep(1)
    os.system("clear")
while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu== "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu =="4":
    spam(10)
  time.sleep(1)
  os.system("clear")
