# 🌟 Day 97: Wikipedia Scraping and OpenAI Summarization Challenge 📝💡

![code97 input](https://github.com/user-attachments/assets/98e38461-91d9-459a-97a5-1f20be05f200)

### 🎊 Today’s Highlights:

* **Wikipedia Scraping:** We fetch an article from Wikipedia on a topic of your choice.

* **OpenAI Summarization:** We use OpenAI’s language model to summarize the article into no more than 3 concise paragraphs.

* **Summary Display:** The summary is displayed with the original article's references for full transparency.

### 🔍 Key Concepts:

* **Web Scraping:** We'll use Python libraries (e.g., BeautifulSoup, Requests) to scrape content from Wikipedia.

* **Summarization with OpenAI:** The scraped article text is sent to OpenAI for summarization.

* **References Handling:** We keep track of references used in the original Wikipedia article and append them to the summary.

### 👉 Day 97 Challenge: Task Overview:

  1. Scrape a Wikipedia article of your choice using Python and BeautifulSoup.

  2. Send the article content to OpenAI for summarization in no more than 3 paragraphs.

  3. Display the summary along with the Wikipedia references at the bottom.

### 🛠️ Implementation Details:

* **Wikipedia Scraping:** Use ```requests``` and ```BeautifulSoup``` to fetch and parse the Wikipedia page.

* **OpenAI Summarization:** The full article (minus some HTML formatting) is sent to OpenAI to generate a concise summary of 3 paragraphs or fewer.

* **References Handling:** Extract the references and include them in the output summary for completeness.

### 🛠️ Common Errors Encountered:

* **HTML Parsing Issues:** The Wikipedia page might contain tricky HTML formatting that could interfere with content extraction.

     * **Fix:** Clean the text and ensure you're removing unnecessary tags and HTML elements before sending to OpenAI.

* **Text Length for Summarization:** OpenAI has token limits on input, which may cause issues with longer Wikipedia articles.

     * **Fix:** You may need to preprocess the text to break it down into manageable chunks for summarization.

* **Handling Special Characters:** Some Wikipedia pages may include special characters or math formulas that don't translate well in the summary.

     * **Fix:** Ensure these are either removed or properly formatted before summarization.
