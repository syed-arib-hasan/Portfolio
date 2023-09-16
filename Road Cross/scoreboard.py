from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-256,275)
        self.lvl=0
        self.update_socre()


    def update_socre(self):
        self.clear()
        self.write(f"Level: {self.lvl}" , align="center",font=("Courier",12,"normal"))

    def lvl_add(self):
        self.lvl+=1
        self.update_socre()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER" , align="center",font=("Courier",30,"normal"))
    
        