from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = .5
LONG_BREAK_MIN = 1
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def get_started():
    global reps
    if reps==0:
        start_timer()
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        timer_label.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif  reps%2==0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def restart():
    global reps
    reps=0
    window.after_cancel(timer)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="✓"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
timer_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_imp=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_imp)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",command=get_started)
start_button.grid(column=0,row=2)
restart_button=Button(text="Restart",command=restart)
restart_button.grid(column=2,row=2)
check_mark=Label(font=(FONT_NAME,15,"bold"),fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)



window.mainloop()