from flask import Flask, request
from replit import db
import requests, json, os
from requests.auth import HTTPBasicAuth


def getTracks(year):
  clientID = os.environ['CLIENT_ID']
  clientSecret = os.environ['CLIENT_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type":"client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSecret)

  response = requests.post(url, data=data, auth=auth)
  accessToken = response.json()["access_token"]

  offset = 0
  try:
    offset = db[year]
    if offset > 200:
      offset = 0
    db[year] += 10
  except:
    db[year]=10

  headers = {'Authorization': f'Bearer {accessToken}'}
  url = "https://api.spotify.com/v1/search"
  search = f"?query=year%3A{2011}&type=track&include_external=audio&locale=en-US%2Cen%3Bq%3D0.9&offset={offset}&limit=20"
  fullURL = f"{url}{search}"

  response = requests.get(fullURL, headers=headers)
  data = response.json()
  print(data)

  songs = ""
  f = open("songs.html", "r")
  songs = f.read()
  f.close()

  listsongs = ""

  for track in data['tracks']['items']:
    thistrack = songs
    thistrack = thistrack.replace("{name}", f"""{track['name']} by {track['artists'][0]['name']}""")
    thistrack = thistrack.replace("{url}", track["preview_url"] if track["preview_url"] is not None else "No Preview Available")
    listsongs += thistrack

  return listsongs

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def change():
  page = ""
  f = open("form.html", "r")
  page = f.read()
  f.close()
  year = request.form["year"]
  songs = getTracks(year)
  page = page.replace("{songs}", songs)
  page = page.replace("{value}", year)
  return page 

@app.route('/')
def index():
  page = ""
  f = open("form.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{songs}", "")
  page = page.replace("{value}","2011")
  return page 

app.run(host='0.0.0.0', port=81)
