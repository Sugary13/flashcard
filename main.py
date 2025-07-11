import random
import pandas
import os
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA ---------------------------- #

if os.path.exists("./data/words_to_learn.csv"):
    data = pandas.read_csv("./data/words_to_learn.csv")
else:
    data = pandas.read_csv("./data/french_words.csv")
    data.to_csv("./data/words_to_learn.csv", index=False)
    data = pandas.read_csv("./data/words_to_learn.csv")

words = data.to_dict(orient="records")

current_word = {}

# ---------------------------- UI ---------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer de voltear
flip_timer = window.after(3000, lambda: None)  # Inicializado vacío

# Canvas (tarjeta de vocabulario)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



# ---------------------------- FUNCIONES ---------------------------- #

def change_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)

    if not words:
        canvas.itemconfig(card_title, text="Congratulations!", fill="black")
        canvas.itemconfig(card_word, text="You know all words!", fill="black")
        canvas.itemconfig(card_image, image=card_front)
        return

    current_word = random.choice(words)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")

    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")

def known_word():
    words.remove(current_word)
    words_df = pd.DataFrame(words)
    words_df.to_csv("./data/words_to_learn.csv", index=False)
    change_word()

# ---------------------------- BOTONES ---------------------------- #

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(column=0, row=1)

# ---------------------------- START ---------------------------- #

change_word()
window.mainloop()