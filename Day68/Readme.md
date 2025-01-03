# 🌟 Day 68: Image Toggle and Error Handling in Tkinter 🖼️🖱️

### 🎊 Today’s Highlights:

* **Image Toggle Functionality:** We enhanced a Tkinter application to toggle an image on the screen, using a button that hides or displays the image based on user interaction.
* **Dynamic Image Replacement:** We also added functionality to switch between two images in a canvas, triggered by a button click.
* **Error Handling with Images:** Implemented error handling by checking if an image exists. If an image is not found, the program displays a fallback message in the same spot as the image.
* **Boolean States:** The concept of toggling visibility was implemented using a Boolean state to manage whether the image is visible or not.

### 🔍 Key Concepts:

* **Tkinter Pack Forget:** We used the ```pack_forget()``` method to hide widgets like labels, buttons, and canvas items, and ```pack()``` to bring them back to the interface.
* **Image Handling in Tkinter:** We loaded images using ```PhotoImage```, and learned how to scale images with the subsample() method.
* **Error Handling for Images:** A fallback message ("Unable to find image") is shown when an image cannot be found, providing feedback to the user.
* **Button Commands:** Buttons are connected to functions using the ```command``` parameter, which enables user interaction with the application.

### 👉 Day 68 Challenge:

**Task Overview:**

   1. Start the program with no image displayed.
   2. Allow the user to input a name for an image.
   3. If the specified image is not found, display a label saying "Unable to find image" in the image's place.

### 🛠️ Implementation Details:

  * We use the ```input()``` function to receive the image name from the user.
  * We employ a simple check to verify if the image file exists using Python's exception handling, and if not, display an error message.
  * Toggle the visibility of the image using a button, ensuring the program provides visual feedback depending on the state of the image.

### 🛠️ Common Errors Encountered:

* **FileNotFoundError for Images:** If the image file path is incorrect or the file doesn't exist, an error will be raised.

  * **Fix:** We handle this by using a try-except block around the image loading code.

* **Using an Undefined Image Variable:** If trying to reference an image variable that hasn’t been defined yet, such as an empty canvas, errors occur.

  * **Fix:** Make sure the image variable is initialized and updated appropriately.

* **Incorrect Packing Order:** Widgets that are packed or unpacked incorrectly may overlap or not appear as expected.

  * **Fix:** Always pack/unpack widgets in the correct order.

### Example:
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
    canvas.pack_forget()
    warning.pack()
    return
  warning.pack_forget()
  canvas.pack()

hello = tk.Label(text=label)
hello.pack()
warning = tk.Label(text="Unable to find this user")
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)

charlotte = ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))
container = canvas.create_image(150,1,image=mo)

tk.mainloop()
