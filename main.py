BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random


# ----------------RANDOM WORDS DISPLAY -----------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv", index_col=False)

except FileNotFoundError:
    data = pandas.read_csv("data/en_tr_words.csv",index_col=False)
    to_learn = data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

# ----------------FUNCTIONS -----------------#
current_card:{}
def next_card():
    global flip_timer
    global current_card
    window.after_cancel(flip_timer)
    current_card = (random.choice(to_learn))
    new_word = current_card["English"]
    canvas.itemconfigure(card_title, text="English", fill="black")
    canvas.itemconfigure(card_words, text=new_word, fill="black")
    canvas.itemconfigure(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    next_card()
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)



def flip_card():
    kelime = current_card["Türkçe"]
    canvas.itemconfigure(card_title, text="Türkçe", fill="white")
    canvas.itemconfigure(card_words, text= kelime, fill="white")
    canvas.itemconfigure(card_background, image=back_img)


# ---------------- UI GRAPHICS -----------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img= PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_words = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

# Buttons:
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()


