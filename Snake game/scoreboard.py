from turtle import Turtle

class Scoreboard(Turtle):
    points=0
    def __init__ (self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {Scoreboard.points}" , align="center",font=("Courier",15,"bold"))
        

    def point_up(self):
        Scoreboard.points+=1
        self.clear()
        self.write(f"Score: {Scoreboard.points}" , align="center",font=("Courier",15,"bold"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier",30,"bold"))

        


    