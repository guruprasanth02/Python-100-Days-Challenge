# ✨ Day 56: Music Streaming Service – Categorizing Songs by Artist 🎶🎧

### 🎉 Today’s Highlights:

**Understanding CSV File Handling:**

   * Learned how to read CSV files in Python using the ```csv``` module.
   * Focused on parsing and extracting data to categorize and organize information effectively.
   * Worked with directory and file operations to structure data based on specific criteria (artist names).

**Folder and File Management:**

   * Explored how to create directories and subdirectories using Python’s ```os``` module.
   * Created blank text files for each song, dynamically naming them based on song titles and artist names.

**Working with Artists and Songs:**

   * Categorized songs by their artist, creating one folder per artist.
   * Created one blank text file for each song in the relevant artist folder. The filename of the text file is the song’s name.

### 🔍 Key Concepts:

**Reading CSV Files:**
```python
import csv

with open('100MostStreamedSongs.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Process the data
```

**Directory and File Management:**
```python
Copy code
import os

# Create a directory for each artist
os.makedirs("Artist_Name", exist_ok=True)

# Create a blank text file for each song
with open(f"Artist_Name/{song_name}.txt", "w") as file:
    # The file is created as an empty text file
```

**Dynamic File Naming:**
```python
Copy code
song_name = "Song Title"
artist_name = "Artist Name"

file_path = os.path.join(artist_name, f"{song_name}.txt")
with open(file_path, "w") as file:
    pass  # Create an empty text file with the song name as the filename
```

### 🌟 Day 56 Challenge: Music Streaming Service

**Task Overview:**

   * Read data from the CSV file ```100MostStreamedSongs.csv```.
   * For each song, create a folder named after the artist.
   * Inside each artist folder, create a blank text file for each song with the filename being the song's name.

**Steps Taken:**

1. **Read the CSV File:***
    Opened and read the ```100MostStreamedSongs.csv``` file to extract song and artist details.

2. **Created Directories for Artists:**
    For each unique artist, a new directory was created.

3. **Created Blank Text Files for Songs:**
    For each song by an artist, a new text file was created in the relevant artist's folder. The file was named after the song title.

### 🎡 Common Errors Encountered:

* **File Already Exists Error:**

     Fixed by using ```os.makedirs()``` with the ```exist_ok=True``` argument to avoid errors if a folder already exists.

* **File Naming Conflicts:**

     Resolved by ensuring that file names were sanitized (removing special characters or spaces) and that they accurately reflected the song titles.

* **Incorrect File Paths:**

     Solved by using ```os.path.join()``` to dynamically create file paths that are cross-platform compatible.

🔢 My Code Examples:
```python
import csv, os

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  
  for row in reader:
    dir = os.listdir()
    artist = row["Artist(s)"].title()
    print(artist)
    if artist not in dir:
      os.mkdir(artist)
    song = row["Song"]
    print(row["Song"])
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()

