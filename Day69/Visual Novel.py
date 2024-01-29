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
