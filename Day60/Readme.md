# 🌟 Day 60: The Magic of Time – Understanding Dates and Time Calculations ⏳

### 🎊 Today’s Highlights:

* **Introduction to Time Handling:** We delved into the complexities of time representation, discussing the differences between time zones, leap years, leap seconds, and Unix time.
* **Using the ```datetime``` Module:** We learned how to work with dates and times in Python using the built-in ```datetime``` library, understanding how to manipulate dates, perform comparisons, and calculate time differences.
* **The Unix Epoch:** We explored the concept of the Unix epoch, which is the system's way of counting seconds since January 1, 1970.
* **Time Delta Calculations:** We explored how to use ```timedelta``` to calculate differences between dates, adding or subtracting time intervals.

### 🔍 Key Concepts:

* **Unix Epoch:** The Unix epoch is a reference time used by computers to calculate time. It counts the number of seconds since January 1, 1970.
* ```**datetime Module:**``` This built-in Python module helps you work with dates and times. Key classes include ```date```, ```time```, ```datetime```, and ```timedelta```.
* **Date Formatting:** We discussed the importance of using the ```year -> month -> day``` format, which simplifies sorting and comparisons.
* ```**timedelta:**``` A ```timedelta``` represents a difference between two dates, and it allows you to easily add or subtract days, hours, or other time units.
* **Comparing Dates:** You can use comparison operators like ```>```, ```<```, and ```==``` to compare dates, making it possible to check if one date is before or after another.
`
### 👉 Day 60 Challenge: Event Countdown Timer ⏳ Task Overview:

  * Prompt the user to input an event name, along with the event's date (year, month, and day).
  * Calculate how many days are left until the event.
  * If the event is today, display party emojis and a congratulatory message.
  * If the event has passed, show sad face emojis and tell the user how many days ago it occurred.

### 🛠️ Common Errors Encountered:

* **Incorrect Date Format:** Users may input the date in an incorrect format (e.g., ```month-day-year``` instead of ```year-month-day```). Ensure the date is correctly formatted.

* **Comparison Errors:** When comparing dates, ensure that the logic accounts for future, past, or current events. This can be handled using ```if``` and ```elif``` statements.

* **Leap Year Handling:** When working with dates around February 29th, make sure the leap year is accounted for to avoid errors in time differences.

### My Code:
```python
import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference>0:
  print(f"{difference} days to go")
elif difference<0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
  
else:
  print("🥳🥳🥳🥳🥳🥳🥳 Today!")
