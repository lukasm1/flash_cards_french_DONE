import pandas
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# -----------------------FUNCTIONALITY-------------------#
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
words_list = data.to_dict(orient="records")
print(words_list)
current_card={}


def new_card():
    global current_card, time_flp_card
    window.after_cancel(time_flp_card)
    current_card=choice(words_list)
    random_fr_wrd = current_card["French"]
    canvas.itemconfig(new_txt, text="French", fill="black")
    canvas.itemconfig(new_wrd, text=random_fr_wrd, fill="black")
    canvas.itemconfig(img_bg, image=card_frt)
    time_flp_card=window.after(3000, flip_card)


def flip_card():
        random_en_wrd = current_card["English"]
        canvas.itemconfig(new_txt, text="English", fill="white")
        canvas.itemconfig(new_wrd, text=random_en_wrd, fill="white")
        canvas.itemconfig(img_bg, image=card_bck)

def knows_it():
    global words_list, current_card
    words_list.remove(current_card)
    new_df=pandas.DataFrame(words_list)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    new_card()

# -----------------------GUI-------------------#
window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_frt = PhotoImage(file="./images/card_front.png")
card_bck=PhotoImage(file="./images/card_back.png")
img_bg=canvas.create_image(400, 263, image=card_frt)
canvas.grid(column=0, row=0, columnspan=2)


new_txt = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
new_wrd = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

card_wrong = PhotoImage(file="./images/wrong.png")
card_wrong_bt = Button(image=card_wrong, highlightthickness=0, command=new_card)
card_wrong_bt.grid(column=0, row=1)

card_right = PhotoImage(file="./images/right.png")
card_right_bt = Button(image=card_right, highlightthickness=0, command=knows_it)
card_right_bt.grid(column=1, row=1)

time_flp_card = window.after(3000, flip_card)

new_card()

window.mainloop()
