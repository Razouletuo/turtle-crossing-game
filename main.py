import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# turtle = Turtle()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_cars()
    car.move_cars()

    #detect collision
    for gari in car.all_cars:
        if gari.distance(player) < 20:
            score.over()

            game_is_on = False

    #detect success crossing
    if player.player_reach():
        player.go_to_start()
        score.increase_lev()
        car.level_up()


screen.exitonclick()