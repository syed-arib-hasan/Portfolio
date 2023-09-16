from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=.1

    def move(self):
        x=(self.xcor()+self.x_move)
        y=(self.ycor()+self.y_move)
        self.goto(x,y)


    def bounce_y(self):
        self.y_move*=-1   

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=.9

    def reset(self):
        self.goto(0,0)
        self.move_speed=.1
        self.bounce_x()


        