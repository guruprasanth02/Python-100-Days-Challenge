import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup 
from replit import db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

interests = ["python", "replit", "100days"]

keys = db.keys()
for key in keys:
  del db[key]

def email(text, link):
  password = os.environ['mailPassword']
  username = os.environ['mailUsername']
  host = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host = host, port = port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg['To'] = username
  msg['From'] = username
  msg['Subject'] = "New Community Event"
  text = f"""<a href='{link}'>{text}</a>"""
  msg.attach(MIMEText(text, 'html'))
  s.send_message(msg)
  del msg
  
def getHub():
  url = "https://replit.com/community-hub"

  response = requests.get(url)
  html = response.text

  soup = BeautifulSoup(html, 'html.parser')

  myLinks = soup.find_all("div", {"class":"css-1dgfpnh"})

  counter = 0 
  keys = db.keys()
  for link in myLinks:
    if "Community spaces" in link.text:
      break
    if counter !=0:
      print(link.text)
      thisLink = link.find("a")["href"]
      print(thisLink)
      words = link.text.split()
      amInterested = False
      for word in words:
        if word.lower() in interests:
          amInterested = True
      if amInterested and link.text not in keys:
        db[link.text] = thisLink
        email(link.text, thisLink)
        
    counter += 1


getHub()

schedule.every(3).hours.do(getHub)

while True:
  schedule.run_pending()
  time.sleep(1)
