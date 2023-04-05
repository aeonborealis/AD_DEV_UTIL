import os
import subprocess
import pydvdread

# Mount the DVD and get the list of titles
dvd = pydvdread.DVD("/dev/sr0")
titles = dvd.get_titles()

# Select the longest title (assuming it's the main feature)
longest_title = max(titles, key=lambda title: title.get_length())

# Get the DVD path and output file path
dvd_path = longest_title.get_path()
output_path = os.path.join(os.getcwd(), "output.mp4")

# Use FFmpeg to convert the DVD to an MP4 file
ffmpeg_cmd = f"ffmpeg -i '{dvd_path}' -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k '{output_path}'"
subprocess.run(ffmpeg_cmd, shell=True, check=True)

# Unmount the DVD
dvd.eject()
