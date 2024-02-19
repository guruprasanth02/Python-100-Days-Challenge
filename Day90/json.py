import requests, json

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
#print(json.dumps(user, indent=2)) 

    for person in user['results']:
      filename = f"""{person["name"]["first"].lower()} {person["name"]["last"].lower()}.jpg""" 
      picture = requests.get(person["picture"]["medium"])
      f = open(filename, "wb")
      f.write(picture.content)
      f.close()
      print(f"saved {filename}")
