import pyfiglet

# Get user input
text = input("Enter your text: ")

# Create ASCII art from user input using Pyfiglet
ascii_art = pyfiglet.figlet_format(text)

# Print ASCII art to the console
print(ascii_art)

# Write ASCII art to a file
with open("ascii_art.txt", "w") as file:
    file.write(ascii_art)
