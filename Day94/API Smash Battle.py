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
