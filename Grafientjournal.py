from tkinter import *
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.geometry("800x600")
root.configure(bg="#202020")
root.title("Terminal Journal")

# Add neon gradient background
bg_gradient = Canvas(root, width=800, height=600, bg="#202020", highlightthickness=0)
bg_gradient.pack()
gradient_colors = ["#f02fc2", "#6094ea", "#b4ec51", "#f5d64c", "#f02fc2"]
for i in range(5):
    bg_gradient.create_rectangle(i*(800/5), 0, (i+1)*(800/5), 600, fill=gradient_colors[i], width=0)

# Add text area
text_area = Text(root, font=("OCR A Extended", 12), fg="#FFFFFF", bg="#202020", insertbackground="#FFFFFF", bd=0)
text_area.pack(padx=20, pady=10)

# Add save button function
def save():
    text = text_area.get(1.0, END).strip()
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"
    with open(filename, "w") as file:
        file.write(text)
    messagebox.showinfo("Saved", f"Journal saved as {filename}")

# Add save button
save_button = Button(root, text="Save Journal", font=("OCR A Extended", 12), fg="#FFFFFF", bg="#202020", bd=0, command=save)
save_button.pack(pady=10)

root.mainloop()
