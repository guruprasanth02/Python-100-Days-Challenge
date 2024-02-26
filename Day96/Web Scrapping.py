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
