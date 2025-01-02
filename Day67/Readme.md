# 🌟 Day 67: GUI Fun with tkinter and Images 🎨

### 🎉 Today’s Highlights:

1. **Exploring tkinter for GUI Development:** We took a deeper dive into tkinter, a Python library for creating graphical user interfaces. Despite its quirks and lack of drag-and-drop design, it offers full control and flexibility.

2. **Working with Images in tkinter:**

      * Displaying images on a canvas.

      * Resizing images using the ```subsample``` method.

      * Dynamically changing images in response to user actions.

3. **Common Errors and Debugging:** Identified typical pitfalls when working with tkinter and learned how to resolve them effectively.

4. **Challenge Time:** A practical exercise to load and display images based on user input.

### 🔍 Key Concepts:

* **Canvas Widget:** Used to display and manage graphical elements, including images.

Example:
```python
canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()
```

* **Loading Images:** Using ```PhotoImage``` to load and manipulate image files.

Example:
```python
image = tk.PhotoImage(file="example.png")
image = image.subsample(5)  # Resize the image
canvas.create_image(150, 1, image=image)  # Place the image on the canvas
```
* **Dynamic Updates:** Leveraging ```itemconfig``` to change canvas elements dynamically.

Example:
```python
canvas.itemconfig(container, image=new_image)
```
* **Command Binding:** Connecting button clicks to specific functions using the ```command``` parameter.

Example:
```python
button = tk.Button(text="Click me!", command=changeImage)
```

### 🔧 Day 67 Challenge: Guess Who Image Loader

Your task is to create a tkinter program that:

  1. Prompts the user to input a name.

  2. Displays the corresponding image if the name matches one of the predefined options (```Charlotte```, ```Gerald```, ```Kate```, ```Mo```).

  3. Shows an “Image Not Found” message if the name does not match.

### 🔎 Debugging Tips:

* **Image Not Displaying:** Ensure the file path is correct and the image file is in the same directory or properly referenced.

* **Resizing Issues:** Use ```subsample``` or ```zoom``` to adjust image size to fit the canvas.

* **Memory Management:** Keep references to ```PhotoImage``` objects to prevent them from being garbage-collected.

### Example Code:
```python
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "mo":
    canvas.itemconfig(container, image=mo)
  elif person.lower().strip() == "charlotte":
    canvas.itemconfig(container, image=charlotte)
  elif person.lower().strip() == "gerald":
    canvas.itemconfig(container, image=gerald)
  elif person.lower().strip() == "katie":
    canvas.itemconfig(container, image=katie)
  else:
    hello["text"] = "Unable to find this user"

hello = tk.Label(text=label)
hello.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()
charlotte = ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))
container = canvas.create_image(150,1,image=mo)

tk.mainloop()
