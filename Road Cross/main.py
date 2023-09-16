from turtle import Screen
from cars import Cars
from scoreboard import Score
import time
from tim import Tim


screen=Screen()
screen.setup(600,600)
screen.tracer(0)

tim=Tim()
car=Cars()
score=Score()


screen.listen()
screen.onkey(tim.move_up,"Up")
screen.onkey(tim.move_down,"Down")

game_is_on= True 

while game_is_on:
    time.sleep(.1)
    screen.update()
    car.crearte_cars()
    car.move_cars()

    #detect collision with cars
    for i in car.all_cars:
        if tim.distance(i)<20:
            game_is_on=False
            score.game_over()

    #finish road
    if tim.finish():
        tim.goto_start()
        car.lvl_up()
        score.lvl_add()







screen.exitonclick()


