import cv2
import numpy as np
import pyautogui

# Set the output video properties
SCREEN_SIZE = (1920, 1080)
VIDEO_FPS = 30.0
VIDEO_CODEC = cv2.VideoWriter_fourcc(*"mp4v")
OUTPUT_PATH = "screen_capture.mp4"

# Create a VideoWriter object to write the output video
out = cv2.VideoWriter(OUTPUT_PATH, VIDEO_CODEC, VIDEO_FPS, SCREEN_SIZE)

# Capture the screen and write each frame to the output video
while True:
    # Get a screenshot of the screen and convert it to a NumPy array
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)

    # Convert the frame from BGR (OpenCV default) to RGB (video standard)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output video
    out.write(frame)

    # Exit the loop if the user presses the "q" key
    if cv2.waitKey(1) == ord("q"):
        break

# Release the VideoWriter and destroy all windows
out.release()
cv2.destroyAllWindows()
