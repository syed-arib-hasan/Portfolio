from turtle import Screen
import time
from Snake import SNAKE
from Food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game") 
screen.tracer(0)

snake= SNAKE()
food= Food()
score=Scoreboard()
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

    #detect collison with food
    if snake.head.distance(food)<15:
        food.refresh()
        score.point_up()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()==-300 or snake.head.ycor()>280 or snake.head.ycor()== -300:
        game_is_on= False
        score.game_over()

    #detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_is_on=False
            score.game_over()
screen.exitonclick()