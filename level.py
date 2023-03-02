from turtle import Turtle


class LevelCount(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setpos(x_pos, y_pos)
        self.write(arg=f"Level: {self.level}", font=("Helvetica", 20, "normal"), align="center")

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=("Helvetica", 20, "normal"), align="center")
