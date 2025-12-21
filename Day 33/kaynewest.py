import tkinter as tk
import random
import requests


def show_quote():
    response = requests.get("https://api.kanye.rest/")
    data = response.json()
    quote = data['quote']
    quote_label.config(text= quote)

# Main window
root = tk.Tk()
root.title("Quote Generator")
root.geometry("600x400")
root.resizable(False, False)

# Background color
bg_color = "#1e1e2f"
card_color = "#2a2a40"
button_color = "#6c63ff"
text_color = "white"

root.configure(bg=bg_color)

# Card frame (fancy look)
card = tk.Frame(root, bg=card_color, bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=300)

# Title
title_label = tk.Label(
    card,
    text="✨ Daily Motivation ✨",
    font=("Helvetica", 18, "bold"),
    fg=text_color,
    bg=card_color
)
title_label.pack(pady=(20, 10))

# Quote display
quote_label = tk.Label(
    card,
    text="Click the button to get inspired",
    wraplength=440,
    font=("Helvetica", 14, "italic"),
    fg=text_color,
    bg=card_color,
    justify="center"
)
quote_label.pack(pady=30)

# Generate button
generate_btn = tk.Button(
    card,
    text="Generate Quote",
    command=show_quote,
    font=("Helvetica", 12, "bold"),
    bg=button_color,
    fg="white",
    activebackground="#574bdb",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
generate_btn.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Stay inspired 💙",
    font=("Helvetica", 10),
    fg="gray",
    bg=bg_color
)
footer.pack(side="bottom", pady=10)

root.mainloop()
