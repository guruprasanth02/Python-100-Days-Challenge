# 🌟 Day 100: The Final Challenge – Price Scraper with Email Automation 💥✨

![code100 credit](https://github.com/user-attachments/assets/58158f02-25ef-40cb-9854-a26fb2062534)

### 🎊 Today’s Highlights:

* **Price Scraping with Automation:** We tackled the challenge of creating a price scraper that automatically checks for price changes on a product's webpage. This scraper stores product prices, compares them to a desired price, and sends an email notification if the price drops below your set threshold.

* **Using a Dictionary for Price Tracking:** We created a Python dictionary to store the product's current price and the price you'd be willing to buy it for. This allowed us to keep track of price changes over time.

* **Web Scraping for Price Updates:** Using tools like BeautifulSoup, we scraped product pages to gather the current prices, and we monitored any price changes.

* **Automated Email Notification:** We used Python's ```smtplib``` to send an email to yourself with the product link, your desired price, and the current price if the scraper finds a price change that fits your criteria.

### 🔍 Key Concepts:

* **Web Scraping:** We used Python libraries like ```requests``` and ```BeautifulSoup``` to fetch and parse HTML content from product pages.

* **Data Handling with Dictionaries:** The dictionary structure helped us store and manage product information, such as the current price and the desired price.

* **Email Automation:** We set up automated emails using ```smtplib``` to notify you when prices drop below your target.

* **Time and Date Management:** We added the ability to scrape the product page every day and check for any price changes over time.

### 👉 Day 100 Challenge: 

**Task Overview:** 

* **Goal:** Create a price scraper that checks for price changes daily and sends an email if the price drops below your desired price.

**Tasks:**

  1. Use a dictionary to store the current product price and the price you're willing to pay.

  2. Scrape the product page daily for price changes.

  3. If the price drops below your desired threshold, automate an email to notify you with the following details:

     * A link to the product

     * Your desired price

     * The current price

### 🛠️ Common Errors Encountered:

* **IP Blocking by Websites:** Websites, like Amazon, may block scrapers after detecting them. To avoid this, we used a less stringent product website for scraping.

* **Email Sending Issues:** There were occasional issues with sending emails if the ```smtplib``` setup was incorrect, such as incorrect SMTP server settings.

* **Web Scraping Failures:** Sometimes, websites change their HTML structure, causing the scraper to fail. It’s essential to inspect the page structure regularly and adjust the scraper accordingly.

**Fixes:**

   * Used headers and rotated IPs or proxies to avoid detection and blocking by websites.

   * Verified and adjusted email configuration settings to ensure reliable email sending.
