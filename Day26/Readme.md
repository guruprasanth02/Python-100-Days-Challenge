# 🌟 Day 26: MyPOD Music Player 🎶  

### 🎊 Today’s Highlights:  
- **Interactivity with User Input**: We created an interactive music player that lets the user select actions through a menu. The program responds dynamically based on the user’s choices.
- **Clearing the Screen**: We used the `os` library to clear the console and refresh the interface. This ensures a clean look for the user interface after each action.
- **Pausing Execution**: We incorporated the `time` library to introduce pauses in the program. This allows for smooth transitions, like pausing before clearing the screen, so the user has time to read messages.
- **Function Calls**: The `play()` function was created to handle the music playback logic and interact with the user.

### 🔍 Key Concepts:
- **`os.system("clear")`**: This command clears the console screen, making the interface appear fresh after each action.
- **`time.sleep(seconds)`**: This function pauses the program for the specified number of seconds, allowing us to delay actions such as clearing the screen for a more user-friendly experience.
- **While Loops**: We used an infinite `while True` loop to keep the music player running, ensuring the user can interact with it until they decide to exit.
- **Dynamic Menu**: The menu changes based on user input, providing options to play a song, view the menu again, or exit.

### 👉 **Day 26 Challenge**: Create a Music Player  

Task Overview:
- **Menu System**: Display a music player title and options for the user to select (play a song, exit, or view the menu again).
- **Music Playback**: When the user selects to play a song, the `play()` subroutine is triggered to start the music.
- **Exit Option**: Provide a way to exit the program cleanly.
- **Screen Clearing**: Clear the console each time a new action or menu is displayed to maintain a tidy interface.
- **Pause for Effect**: Add delays using `time.sleep()` to allow users to see the displayed messages before the screen clears.

### 🛠️ Common Errors Encountered:
- **Screen Too Quick to Clear**: If the screen is cleared too fast, the user may not have time to read the message or see the menu.
  
  Fix: Use `time.sleep(seconds)` to delay actions like clearing the screen, giving the user time to see messages.

- **Incorrect Input Handling**: If the input isn't handled correctly (such as not validating the choice), the program may behave unexpectedly.

  Fix: Ensure you validate user input (e.g., checking if the user selects 1, 2, or something else) before performing actions.

- **Audio Playback Not Pausing**: The music may continue playing or fail to pause after being triggered.
  
  Fix: Ensure that the audio player supports pausing and unpausing properly within the `play()` function.

### My Code:
```python
from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True # let's pause the file 
      return # let's go back from this play() subroutine
    else: 
      continue
  
while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue
