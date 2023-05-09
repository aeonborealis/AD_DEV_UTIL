from gtts import gTTS
import os

# Get user input
notes = input("Enter your notes: ")

# Save notes to a file
with open('notes.txt', 'w') as file:
    file.write(notes)

# Convert notes to speech
tts = gTTS(notes)
tts.save('notes.mp3')

# Play the audio file
os.system('mpg123 notes.mp3')
