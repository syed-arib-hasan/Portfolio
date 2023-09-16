from turtle import Turtle
starting_pos=[(0,0),(-20,0),(-40,0)]
MOVE_DIS=20
class SNAKE: 
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in starting_pos:
            self.add_segments(i)

            
    def add_segments(self,position):
            seg=Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move (self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(MOVE_DIS)
    
    def up (self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down (self):
        if self.head.heading()!=90:
           self.head.setheading(270)

    def left (self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right (self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    