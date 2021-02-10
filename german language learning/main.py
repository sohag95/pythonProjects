from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_card={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except:
    original_data=pandas.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(title_text,text="German",fill="black")
    canvas.itemconfig(word_text,text=current_card["german"],fill="black")
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_background,image=card_back)
    canvas.itemconfig(title_text, text="Bengali",fill="white")
    canvas.itemconfig(word_text, text=current_card["bengali"],fill="white")

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window=Tk()
flip_timer=window.after(3000, func=flip_card)
window.title("German Language Learning App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
card_front=PhotoImage(file="./images/card_front.png")
card_back=PhotoImage(file="./images/card_back.png")
right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_background=canvas.create_image(400,263,image=card_front)
title_text=canvas.create_text(400,150,text="",fill="black",font=(FONT_NAME,25,"bold"))
word_text=canvas.create_text(400,263,text="",fill="black",font=(FONT_NAME,35,"bold"))

canvas.grid(column=0,row=0,columnspan=2)

known_button=Button(image=right,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=0)
unknown_button=Button(image=wrong,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=1)
next_card()
window.mainloop()