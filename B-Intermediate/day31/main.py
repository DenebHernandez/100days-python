import pandas as pd
import tkinter as tk
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    current_word = current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_word)

def flip_card():
    current_word = current_card["English"]
    canvas.config(card_title, text="English")
    canvas.config(card_word, text=current_word)

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)
check_img = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=0)

next_card()

window.mainloop()
