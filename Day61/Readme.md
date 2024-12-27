# 🌟 Day 61: Creating a Twitter for One – Implementing a Tweeting System with Replit DB 🐦

### 🎊 Today’s Highlights:

* **Replit DB Integration:** We learned how to leverage the Replit DB to store data persistently. This allowed us to implement a system for adding and viewing tweets.
* **Storing Data with Timestamps:** We used Python's ```datetime``` module to create a timestamp for each tweet. This way, tweets are stored with the exact date and time they were posted.
* **Pagination for Tweet Viewing:** We implemented a feature to display tweets in reverse chronological order, showing only 10 at a time. Users are prompted to continue viewing more tweets or return to the menu.

### 🔍 Key Concepts:

* **Replit DB:** A simple, persistent storage solution for storing data within a Replit environment. We used it to store tweets and their timestamps.
* **Datetime Module:** We used Python's ```datetime.datetime.now()``` to generate a timestamp for each tweet. This ensures that tweets can be sorted and displayed chronologically.
* **List Slicing:** To handle displaying tweets 10 at a time, we made use of list slicing, ensuring that the tweets are displayed in batches.
* **User Interaction:** The program asks the user whether they want to continue viewing tweets after displaying 10 at a time, allowing for a more interactive experience.

### 👉 Day 61 Challenge: Create Your Own Twitter 🐦

**Task Overview:**

  * **Add a Tweet:** Get the tweet input from the user and store it in the Replit DB, using the current timestamp as the key.
  * **View Tweets:** Display the most recent tweets in reverse chronological order, with the option to view 10 tweets at a time.
  * **Prompt to View More:** After displaying the first 10 tweets, prompt the user if they want to see more tweets (yes or no).
  * **Exit Option:** If the user chooses 'no', they are returned to the main menu.

### 🛠️ Common Errors Encountered:

* **KeyError:** If a key (tweet timestamp) is accessed that doesn't exist. Make sure to check for the presence of keys before trying to access them.
* **IndexError:** When slicing the list of tweets, ensure that the slice range is valid, especially when fewer than 10 tweets are remaining.
* **TypeError:** When input types are not handled properly, such as trying to store a non-string value as a tweet.

### My Code:
```python

from replit import db
import datetime, os, time

def addTweet():
  tweet = input("🐥 > ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")

def viewTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      carryOn = input("Next 10?: ")
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")


while True:
  print("Tweeter")
  menu = input("1: Add Tweet\n2: View Tweets\n> ")
  if menu == "1":
    addTweet()
  else:
    viewTweet()
