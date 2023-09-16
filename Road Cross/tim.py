from turtle import Turtle
class Tim(Turtle):
    def __init__ (self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto_start()


    def move_up(self):
        y=self.ycor()+10
        self.goto(0,y)

    def move_down(self):
        y=self.ycor()-10
        self.goto(0,y)

    def goto_start(self):
        self.goto(0,-280)

    def finish(self):
        if self.ycor()>280:
            return True
        else:
            return False

