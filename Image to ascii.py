from PIL import Image

# Open the image and resize it to a desired size
img = Image.open("image.jpg")
img = img.resize((120, 80))

# Define a string of ASCII characters to use for the conversion
ascii_chars = "@#$%&?*+;:,. "

# Convert each pixel to its corresponding ASCII character
ascii_image = ""
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        brightness = sum(pixel) / 3
        char_index = int((brightness / 255) * (len(ascii_chars) - 1))
        ascii_char = ascii_chars[char_index]
        ascii_image += ascii_char
    ascii_image += "\n"

# Print the ASCII art to the console
print(ascii_image)
