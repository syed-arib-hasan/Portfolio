from turtle import Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title ("Pong Game by Arib")
screen.tracer(0)


pad1= Padle()
pad2=Padle(-350,0)
ball=Ball()
score=Scoreboard()



screen.listen()
screen.onkey(pad1.go_up,"Up")
screen.onkey(pad1.go_down,"Down")
screen.onkey(pad2.go_up,"w")
screen.onkey(pad2.go_down,"s")


game_is_on= True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detection with wall
    if ball.ycor()>278 or ball.ycor()<-278:
        ball.bounce_y()

    #detection with padle
    if ball.distance(pad1)<50 and ball.xcor()>328:
        ball.bounce_x()
              
    if ball.distance(pad2)<50 and ball.xcor()<-328:
        ball.bounce_x()
             
    #detect r pad miss
    if ball.xcor()>400:
        ball.reset()
        score.l_point_up()
    #detect l pad miss
    if ball.xcor()<-400:
        ball.reset()
        score.r_point_up()

    if score.l_score ==10 or score.r_score==10:
        game_is_on=False
        score.game_over()

screen.exitonclick()
