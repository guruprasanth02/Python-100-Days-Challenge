# 🌟 Day 96: Hacker News Scraper Challenge 📰💻

### 🎊 Today’s Highlights:

* **Hacker News Scraping:** Scrape the Hacker News website for headlines that include "Python" or "Replit."

* **Data Filtering:** Filter the headlines to display only the relevant results containing the specified keywords.

* **Basic Text Parsing:** Learn to navigate and extract useful information from a website.

### 🔍 Key Concepts:

* **Web Scraping:** Using Python libraries like ```requests``` and ```BeautifulSoup``` to extract data from websites.

* **HTML Parsing:** Understanding the structure of web pages and how to target specific elements like headlines.

* **Text Filtering:** Using Python string operations to filter out headlines based on specific keywords.

### 👉 Day 96 Challenge:

**Task Overview:**

  * Scrape the headlines from Hacker News.

  * Display only the headlines that include the words "Python" or "Replit."

### 🛠️ Implementation Details:

* **Web Scraping with Requests:** Use the ```requests``` library to download the HTML content of the Hacker News page.

* **HTML Parsing with BeautifulSoup:** Pass the HTML to ```BeautifulSoup``` to extract all headlines.

* **Text Filtering:** Search for headlines containing the words "Python" or "Replit" using Python string methods.

### 🔧 Challenges Faced & Solutions:

* **HTML Structure Understanding:** The initial difficulty may be understanding the structure of the Hacker News page. By inspecting the HTML, we can target the specific tags (e.g., ```<a class="storylink">```) for extracting the headlines.

    * **Fix:** Use the browser’s developer tools (Inspect Element) to identify the correct HTML tags and classes.

* **Text Filtering:** It’s essential to ensure that case-insensitive filtering is performed correctly, or you may miss relevant headlines.

    * **Fix:** Use Python’s ```.lower()``` method for case-insensitive searching or use regular expressions for more flexible matching.

* **Error Handling:** The program assumes the page is available and the HTML structure doesn’t change.

    * **Fix:** Implement error handling, such as checking for successful HTTP status codes and try-except blocks to catch possible parsing errors.

### 🛠️ Code Example:
```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("span", {"class":"titleline"})

#print(len(myLinks))
things = ["bad", "apple", "python","Micrsoft"]

for link in myLinks:
  text = link.text
  textlist = text.split()
  containsword = False
  for word in textlist:
    if word.lower() in things:
      containsword = True
  if containsword:    
     print(link.text)
     myLinks = link.find_all("a")
     print(myLinks[0]["href"])
