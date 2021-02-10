from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):

        self.window=Tk()
        self.quiz=quiz_brain
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.canvas=Canvas(height=250,width=300)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=30)
        self.text=self.canvas.create_text(150,125,width=288,text="QUESTION WILL BE HERE",fill="black",font=("arial",20,"italic"))
        self.score_label=Label(text="Score : 0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0)
        self.true=PhotoImage(file="images/true.png")
        self.false=PhotoImage(file="images/false.png")
        self.right_button=Button(image=self.true,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(row=2,column=0)
        self.wrong_button = Button(image=self.false,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"Questions have been finished.\nYour score is :{self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        ans=self.quiz.check_answer("true")
        self.give_feedback(ans)

    def false_pressed(self):
        ans=self.quiz.check_answer("false")
        self.give_feedback(ans)

    def give_feedback(self,ans):
        score=self.quiz.score
        self.score_label.config(text=f"Score : {score}\nDone :{self.quiz.question_number}")
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
