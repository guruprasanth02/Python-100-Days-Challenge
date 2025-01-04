# 🌟 Day 69: Visual Novel Creation Challenge 🎮📖

### 🎊 Today’s Highlights:

* **Visual Novel Basics:** We learned the core structure of a visual novel, including creating a branching story with multiple decisions and endings.
* **User Interaction:** We incorporated buttons for users to make choices that influence the story’s progression.
* **Simple Branching Logic:** The novel features two main branches, one of which leads to an unhappy ending, while the other includes both a bad and a good ending.
* **Story Flow:** We built a story where the user’s choices determine which images and text are displayed, creating an interactive experience.

### 🔍 Key Concepts:

* **Interactive Storytelling:** A visual novel involves presenting choices to the player, where each decision they make alters the path and outcome of the story.
* **Branching Paths:** We created two main branches of the story, with decisions leading to different endings (unhappy, bad, and good).
* **Buttons for Choices:** We used buttons for players to select their choices, making the experience interactive and dynamic.
* **Story Resetting:** Each ending (whether bad or good) includes a "start again" button to let the user restart the visual novel.

### 👉 Day 69 Challenge: Visual Novel Task Overview:

**Create a simple visual novel with two main decisions:**

* **Introduction & Decision 1:** Begin with an image and a short text. Provide two options for the player to choose from. Each choice will lead to a different branch.
* **Branch 1:** The first branch leads to an unhappy ending. Both options in this branch lead to the same result, which is not ideal, but saves time.
* **Branch 2:** The second branch has a mix of good and bad endings. One option should lead to a bad ending, while the other leads to a good ending.
* **Ending Screens:** After each ending, the user can click a "start again" button to return to the first page.

### 🛠️ Common Errors Encountered:

* **Poor Flow Control:** Sometimes it’s difficult to manage the flow between the different branches, especially when you need to ensure the right image and text appear based on the user’s choices.

  * **Fix:** Carefully track the branching logic to ensure choices lead to the correct story paths and that each choice is properly linked to a unique outcome.

* **Incorrect Button Functionality:** If buttons aren't properly linked to their actions, the story may not flow as expected.

  * **Fix:** Double-check that each button is correctly tied to its corresponding function (i.e., to either transition to a new part of the story or reset the game).

* **Lack of Dynamic Content:** Sometimes the visual novel may feel static or repetitive, with the same images or text being displayed multiple times.

  * **Fix:** Ensure the visual novel has multiple dynamic elements, like unique images or background changes depending on the player's choice.

### My Code (Pseudo-Logic):
```python
import tkinter as tk

window = tk.Tk()
window.title("Visual Novel")
window.geometry("400x400")

story = "You meet a woman on the way to a Replit meetup IRL"

def iCode():
  global story
  canvas.itemconfig(container, image=codes)
  story = "She tries to pull out her laptop and drops it on the floor"
  storyLabel["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()

def iReplit():
  global story
  canvas.itemconfig(container, image=replit)
  story = "Why I use Replit of course, like every sane individual!"
  storyLabel["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button5.pack()
  button6.pack()

def iEdit():
  global story
  canvas.itemconfig(container, image=vs)
  story = "She spends two hours loading up a code editor\nand getting it working, you wait politely"
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()

def iUse():
  global story
  canvas.itemconfig(container, image=amazing)
  story = "You both celebrate using the best\n coding platform on your way to the meetup"
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()

def iToo():
  global story
  canvas.itemconfig(container, image=days)
  story = "She tells you all about 100 days of code!"
  storyLabel["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  restartButton.pack()

def iWin():
  global story
  canvas.itemconfig(container, image=amazing)
  story = "You both celebrate using the best\n coding platform on your way to the meetup\nand talk about 100 days of code"
  storyLabel["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  restartButton.pack()
  
def restart():
  global story
  canvas.itemconfig(container, image=start)
  story = "You meet a woman on the way to a Replit meetup IRL"
  storyLabel["text"] = story
  restartButton.pack_forget()
  button.pack()
  button2.pack()
  
start = tk.PhotoImage(file="visualNovel/1.png")
start = start.subsample(4)
codes = tk.PhotoImage(file="visualNovel/3.png")
codes = codes.subsample(4)
replit = tk.PhotoImage(file="visualNovel/2.png")
replit = replit.subsample(4)
days = tk.PhotoImage(file="visualNovel/4.png")
days = days.subsample(4)
amazing = tk.PhotoImage(file="visualNovel/5.png")
amazing = amazing.subsample(4)
vs = tk.PhotoImage(file="visualNovel/6.png")
vs = vs.subsample(4)

canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()
container = canvas.create_image(150,150, image=start)
storyLabel = tk.Label(text=story)
storyLabel.pack()
button = tk.Button(text="Ask her how she codes?", command=iCode)
button.pack()
button2 = tk.Button(text="Tell her about Replit", command=iReplit)
button2.pack()
button3 = tk.Button(text="She says 'I use a local editor'", command=iEdit)
button4 = tk.Button(text="She says 'I use Replit'", command=iUse)
button5 = tk.Button(text="You say 'I use Replit too'", command=iToo)
button6 = tk.Button(text="You say 'Im actually going through 100 days of code right now", command=iWin)
restartButton = tk.Button(text="Restart", command=restart)

tk.mainloop()
