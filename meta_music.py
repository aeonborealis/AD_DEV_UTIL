import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# set the path to your music directory
music_path = "/path/to/your/music/directory"

# loop through all files in the directory
for file in os.listdir(music_path):
    # check if the file is an mp3 file
    if file.endswith(".mp3"):
        # get the full path to the file
        file_path = os.path.join(music_path, file)
        # open the mp3 file and get the length
        audio = MP3(file_path)
        length_in_seconds = int(audio.info.length)
        # convert length to a string formatted as "minutes:seconds"
        length_in_minutes = length_in_seconds // 60
        length_in_seconds = length_in_seconds % 60
        length_string = f"{length_in_minutes:02}:{length_in_seconds:02}"
        # open the mp3 file with easyid3 and add the new metadata field
        audio_with_metadata = EasyID3(file_path)
        audio_with_metadata["length"] = length_string
        audio_with_metadata.save()
