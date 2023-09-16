from turtle import Turtle

class Padle (Turtle):
    def __init__(self,a=350,b=0):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.setpos(a,b)

    def go_up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)

    def go_down(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)