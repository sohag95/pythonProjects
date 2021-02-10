from turtle import  Screen
from random import randint
import time
from food import Food
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
from snake import Snake
from scoreboard import Scoreboard

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    #Detect food collition with snake
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_is_on=False
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
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