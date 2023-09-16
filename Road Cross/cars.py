from turtle import Turtle
import random

class Cars():
    def __init__ (self):
        self.all_cars=[]
        self.car_speed=10

        

    def crearte_cars(self):
        do=random.randint(1,6)
        if do==6:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            c=["red","purple","blue","sky blue","green","black","orange","yellow","pink"]
            new_car.color(random.choice(c))
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)
        

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed+=10


