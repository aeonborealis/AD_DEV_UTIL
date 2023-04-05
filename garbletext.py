import random

# Get user input
text = input("Enter your text: ")

# Convert input string to a list of characters
chars = list(text)

# Shuffle the list of characters randomly
random.shuffle(chars)

# Join the shuffled characters back into a string
garbled_text = ''.join(chars)

# Print the garbled text
print("Garbled text:", garbled_text)
