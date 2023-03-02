import random
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(0, -270)
        self.setheading(90)

    def go_forward(self):
        steps = random.randint(1, 20)
        self.forward(steps)

    def restart_position(self):
        self.setpos(0, -270)

