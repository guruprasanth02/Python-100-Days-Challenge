# 🌟 Day 94: API Smash Battle - Combining NewsAPI & OpenAI 🌟

### 🎊 Today’s Highlights:

* **API Integration:** Combined NewsAPI to fetch the top headlines of the day with OpenAI to generate summaries of these articles.

* **Modular Code Setup:** Separated the logic for fetching news and summarizing it, so you can easily swap between different APIs or adjust parameters.

* **Dynamic Input Handling:** Allow users to specify their country of interest for the news API, and automatically fetch summaries from OpenAI using those articles.

* **Command Line Program:** Created a simple CLI tool that fetches and summarizes the top 5 news articles for the day.

### 🔍 Key Concepts:

* **API Calls:** Fetching data from multiple APIs in a seamless flow—NewsAPI for news headlines and OpenAI for text processing.

* **JSON Data Parsing:** Handling JSON responses to extract useful information, like titles, URLs, and content.

* **OpenAI Completion Model:** Using OpenAI to summarize lengthy news content into a short, digestible summary.

* **Error Handling:** Basic checks and error handling for API responses and missing fields to ensure the program runs smoothly.

### 👉 Day 94 Challenge: Task Overview:

* Fetch top 5 headlines from NewsAPI for the day.

* Send these headlines and article content to OpenAI for summarization.

* Display the summarized articles to the user via a simple command line interface.

### 🛠️ Common Errors Encountered:

* **Incorrect API Key Handling:** Make sure the API keys are correctly set up in the secrets section and are referenced properly in the code.

   * **Fix:** Double-check that the environment variables are set and correctly referenced.

* **API Response Format Mismatch:** OpenAI's response format might need special handling for extracting text from the returned JSON structure.

   * **Fix:** Always extract the text properly from ```response["choices"][0]["text"].strip()```.

* **Handling Empty News Content:** Sometimes, NewsAPI may return empty or non-informative content.

   * **Fix:** Check for missing content and handle gracefully by either skipping those articles or summarizing available text.

### My Code:
```python
import requests, json, os, openai

newskey = os.environ['newsapi']
openai.organisation = os.environ['organisationID']
openai.api_key = os.environ['openai']
openai.Model.list()

country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newskey}"

result = requests.get(url)
data = result.json()
print(json.dumps(data, indent=2))

counter = 0
for article in data['articles']:
  counter +=1
  if counter > 5:
    break
  prompt = (f"""Summarise {article['url']} in one sentence""")
  response = openai.completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)
  print(response["choices"][0]['text'].strip())
