from turtle import Screen, Turtle
from player import Player
from car import Cars
from level import LevelCount

screen = Screen()
screen.title("Crossing road")
screen.listen()
screen.tracer(0)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()


def close():
    global its_running
    its_running = False


player = Player()
cars = Cars()
current_level = LevelCount(-250, 270)

root.protocol("WM_DELETE_WINDOW", close)
screen.onkeypress(player.go_forward, "Up")

its_running = True
cars_on = True


while its_running:

    screen.update()

    if cars_on:
        cars.move_car()
        cars.generate_number_of_cars()

    for car in cars.cars:
        if player.distance(car.xcor(), car.ycor()) <= 15:
            text = Turtle()
            text.penup()
            text.hideturtle()
            text.color("red")
            cars_on = False
            text.write(arg="GAME OVER", font=("Helvetica", 50, "normal"), align="center")
            screen.onkeypress(None, "Up")

    if player.ycor() >= 300:
        cars.go_faster()
        player.restart_position()
        current_level.level_up()

    if not its_running:
        break
