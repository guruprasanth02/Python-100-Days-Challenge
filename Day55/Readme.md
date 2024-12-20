# 🌟 Day 55: Backup Your Files Program 📂

### 🎊 Today’s Highlights:

* **File Management with os Library:** We explored how to use Python’s ```os``` library for managing files and directories.
* **Creating Folders:** Using ```os.mkdir()```, we created a backup folder where we will store copies of files.
* **Renaming Files:** We learned how to rename files using ```os.rename()``` to better manage them.
* **Checking for Files:** We used ```os.listdir()``` to list the files in a directory and ensure that specific files are present.
* **Automated Backup Process:** We combined these skills to create an automated backup system for important files.

### 🔍 Key Concepts:

* **File and Directory Management:** We focused on using ```os.mkdir()``` to create directories, ```os.rename()``` to rename files, and ```os.listdir()``` to list files in a directory.
* **Backup Automation:** We automated the process of creating backups by generating a random filename and storing a copy of the original file in a designated backup folder.
* **Error Handling:** The program checks whether a specific file exists in the directory and reports an error if the file is not found, ensuring that the backup process only happens if the necessary files are present.

### 👉 Day 55 Challenge: Task Overview:

* Your program must create a backup folder and automatically back up a file before proceeding with any other tasks, such as autosave or loading data.
* The program will:
  
     * Create a backup folder called "backup".
     * Generate a random filename for the backup.
     * Save a copy of a file (e.g., "quickSave.txt") into that folder with the random filename.

**Example Output:**
```
bash
Copy code
Backup folder created.
Backup of quickSave.txt saved as backup/xy1234.txt.
```

### 🛠️ Common Errors Encountered:

* **Directory Already Exists:** If the backup folder already exists, attempting to create it again will result in an error.

   * **Fix:** Use a try-except block to catch the error or check if the folder exists before creating it.

* **File Not Found:** If the file you are trying to back up (e.g., "quickSave.txt") doesn’t exist, the program will fail.

  * **Fix:** Use ```os.listdir()``` to check for the file before proceeding with the backup process.

* **Invalid Filename:** When generating random filenames, ensure that the filename is valid (e.g., no special characters that are not allowed in filenames).

  * **Fix:** Validate the filename generation process by ensuring it’s formatted correctly.

### My Code:
```python
  # | Name | Date | Priority
import os, time, random
todo = []
fileExists = True
try:
  f = open("to.do", "r")
  todo = eval(f.read())
  f.close()
except:
  fileExists = False

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")

  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass
    name = f"backup{random.randint(1,1000000000)}.txt"
    os.popen(f"cp to.do backups/{name}")


  f = open("to.do", "w")
  f.write(str(todo))
  f.close()
