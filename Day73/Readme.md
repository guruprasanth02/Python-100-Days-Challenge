# 🌟 Day 73: Portfolio Challenge - Showcase Your Coding Projects 📄

### 🎊 Today’s Highlights:

Creating a personal web portfolio to display your programming achievements. The goal is to showcase your projects, demonstrating both your coding skills and your creativity. We’ll build a webpage to highlight five of your top projects.

**Step-by-Step Guide:**

1. **Create a Web Page for Portfolio:**

    * Title the page ‘My Portfolio’.
    * Use the ```<h1>``` tag to add the main heading: ‘Your Name - Portfolio’.
    * Under this heading, we’ll display your top 5 projects.
      
2. **Display Each Project:**

    * For each project, use an ```<h2>``` tag to provide a secondary heading (e.g., Project 1, Project 2).
    * Under each project, provide a **short description** (in a ```<p>``` tag) explaining what the project is about.
    * Add an image of each project (you can take a screenshot or capture relevant visuals) with an ```<img>``` tag to give users a visual preview of your work.
    * Link each image to the project page or Repl link so users can directly access the project.

### 🔍 Key Concepts:

* **HTML Structure:** Learn how to use ```<h1>```, ```<h2>```, ```<p>```, and ```<img>``` tags to display information and organize your webpage.
* **External Links:** Use the ```<a href>``` tag to create links to your projects or external pages (e.g., Repl links).
* **Portfolio Design:** Focus on presenting your projects in an aesthetically pleasing way, with organized sections, proper use of headings, and images.

### 👉 Day 73 Challenge:

Build a webpage to showcase 5 of your best projects. For each project, include:

   * A second-level heading ```<h2>``` for each project.
   * A descriptive paragraph ```<p>``` explaining each project.
   * A screenshot or image representing each project.
   * Links to the project pages or Repl for each project.

### 🔧 Common Errors:

   * Missing ```<html>```, ```<head>```, or ```<body>``` tags – These tags define the structure of the webpage.
   
   * Broken image links – Make sure the image path and file name are correct.
   
   * Incorrect link references – Ensure all project links are correctly formatted with the full URL (or relative path if linking within your project).

**Fix:** Always check the syntax and paths for images and links. Double-check project titles and descriptions to ensure accuracy.

### My Code:
```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>

  <h1>GURU'S PORTFOLIO</h1>
  <h2>Welcome to my portfolio website!</h2>
  <P>Hello, I'm Guru Pasanth D, a Computer Science Engineering Student with a passion for becoming AI Engineer.</P>
<a href="https://www.linkedin.com/in/guru-prasanth-d-6b67a01ab/"><img src="portfolio.jpg" width="500px"></a>
  <script src="script.js"></script>

  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>
