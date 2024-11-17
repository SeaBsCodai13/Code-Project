import tkinter as tk
import subprocess
import sys

def on_start_button_click():
    try:
        # Run the external Python file
        subprocess.run([sys.executable, 'main.py'])
    except FileNotFoundError:
        print("The specified file was not found!")

def on_enter(event):
    start_button.config(bg="#005f73", fg="white")  # Change to hover color

def on_leave(event):
    start_button.config(bg="#0a9396", fg="white")  # Return to original color

# Create the main window
root = tk.Tk()
root.title("Home Screen Menu")

# Set the window size
root.geometry("500x400")
root.configure(bg="#94d2bd")

# Create a label for the title
title_label = tk.Label(root, text="A dollar a day keeps John Pork", font=("Helvetica", 20, "bold"), bg="#94d2bd", fg="#003d3d")
title_label.pack(pady=20)

# Create a label for the financial advice
advice_label = tk.Label(root, text="Financial Tips:", font=("Helvetica", 16, "bold"), bg="#94d2bd", fg="#003d3d")
advice_label.pack(pady=10)

# Create the text for financial tips
tips_text = """
- Use credit card, but remember to pay it off.
- Buy property to gain money overtime.
- Live below means (there will be drip in the game).
- Stocks can go up and down, but over the long term, S&P 500 will typically go up.
- Pay yourself first.
"""
tips_label = tk.Label(root, text=tips_text, font=("Helvetica", 12), bg="#94d2bd", fg="#003d3d", justify="left")
tips_label.pack(pady=10)

# Create a stylish Start button
start_button = tk.Button(root, text="Start", font=("Helvetica", 16, "bold"), 
                          bg="#0a9396", fg="white", relief="flat", 
                          width=20, height=2, bd=0, command=on_start_button_click)

# Adding hover effect
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# Add the button to the window
start_button.pack(pady=20)

# Run the application
root.mainloop()
