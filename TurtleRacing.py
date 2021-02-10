from turtle import Turtle, Screen
from random import randint

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter the color:")
colors=["red","orange","yellow","green","blue","purple"]
all_turtlles=[]
y_position=-100
for color in colors:

    new_turtle=Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-240,y=y_position)
    y_position+=40
    all_turtlles.append(new_turtle)

if user_bet:
    is_race_on=True

for turtle in all_turtlles:
    turtle.going_forwrd=True
    turtle.comming_finishline=False

while is_race_on:
    for turtle in all_turtlles:
        if turtle.xcor()>230 and turtle.going_forwrd:
            turtle.going_forwrd=False
            turtle.setheading(180)
            turtle.comming_finishline=True
        if turtle.xcor()<-240 and turtle.comming_finishline:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won the race.The color of the turtle is {winning_color}")
            else:
                print(f"You have loss the race.The color of the turtle is {winning_color}")

        steps=randint(1,10)
        turtle.forward(steps)
print(user_bet)
screen.exitonclick()























# from data import question_data
# from question_model import Question
# from quiz_brain import QuizBrain
# 
# question_bank=[]
# 
# for question in question_data:
#     question_bank.append(Question(question["text"],question["answer"]))
# quiz_brain=QuizBrain(question_bank)
# 
# while quiz_brain.still_has_question():
#     quiz_brain.next_question()
# quiz_brain.final_result()
# print(quiz_brain.score,len(quiz_brain.question_list))