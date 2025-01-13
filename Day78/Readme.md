# 🌟 Day 78: Reflections on My Coding Journey ✅

### 🎉 Today’s Highlights:

* **Code Organization and Structure:** Focused on improving the organization of my codebase, making it more modular and efficient.
* **Dynamic Page Generation:** Implemented dynamic page rendering based on a URL parameter to showcase daily reflections in a web application.
* **Template Rendering:** Used Flask templating to create reusable components and render content based on the day number provided in the URL.

### 🔍 Key Concepts:

* **Flask Framework:** Utilized Flask to set up a simple web application that dynamically generates pages based on URL parameters.
* **Routing and URL Parameters:** Explored how to capture parts of a URL to generate dynamic content. This allowed me to show content specific to each day in my coding challenge.
* **HTML & CSS:** Integrated HTML for the structure of the page and CSS for styling, providing a clean and pleasant user interface for displaying daily reflections.

### 💪 Day 78 Challenge:

Create a web application that displays reflections for each day of the coding challenge based on a dynamic URL route. The application should generate a new page for each day number, styled with custom CSS.

* **Features Implemented:**
     
   * Dynamic URL routing (```/<pageNumber>```) to show reflections for specific days.
   * Integrated a Flask template system to render the reflections and highlight key aspects of each day.
   * Styled the page with CSS to ensure readability and aesthetic appeal.

### 💪 Common Challenges & Fixes:

* **Dynamic URL Parameters:**

  Issue: The page wasn’t rendering correctly when navigating to different day numbers.
  Fix: Ensured that Flask's dynamic routing worked properly with the ```<pageNumber>``` parameter, so the page content updates dynamically based on the URL.

* **CSS Styling:**

  Issue: The page wasn’t visually appealing at first.
  Fix: Applied custom CSS to improve the layout, text size, and structure for readability.

* **Template Rendering Logic:**

  Issue: Struggling with passing correct data to the template for each day.
  Fix: Utilized Flask’s ```render_template``` function to pass the day-specific data (such as the day number and reflections) to the template for rendering.

### 🔹 My Code:
```python
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
