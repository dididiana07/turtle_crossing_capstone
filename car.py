import random
from turtle import Turtle
from random import choice
from time import sleep

COLORS = ["pink", "red", "blue", "green", "yellow", "orange"]


class Cars:
    def __init__(self):
        self.SECONDS = 0.2
        self.cars = []

    def move_car(self):
        try:
            sleep(self.SECONDS)
        except ValueError:
            self.SECONDS = 0.01
        for car in self.cars:
            steps = random.randint(1, 20)
            car.forward(steps)

    def generate_number_of_cars(self):
        NUM_CARS = random.randint(0, 1)
        for _ in range(NUM_CARS):
            car = Turtle("square")
            Y = random.randint(-200, 280)
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.setpos(x=320, y=Y)
            self.cars.append(car)

    def go_faster(self):
        if self.SECONDS != 0:
            self.SECONDS -= 0.05
