from flask import Flask

app = Flask(__name__)

myReflections = {}

myReflections["78"] = {"link": "https://replit.com/@DavidAtReplit/Day-078-Solution#index.html", "Reflection": "was a bit of head scratcher but i got there in the end. Even if I was bit lazy with CSS 😂"}

@app.route('/<pageNumber>')
def index(pageNumber):
  global myReflections    
  page = ""
  if pageNumber in myReflections:  
    with open("template/reflection.html", "r") as f:  # Properly indent the block
      page = f.read()
    page = page.replace("{day}", pageNumber)
    page = page.replace("{link}", myReflections[pageNumber]["link"])
    page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
    return page
  else:
    return "Page not found" 


app.run(host="0.0.0.0", port=8080)
