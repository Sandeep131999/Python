import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
#create a player
#create a cars
#detect collision with car
#detect when reaches to other side

#screen related
screen = Screen()
screen.setup(800,600)
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on  = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect the finishing of cross line

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()




screen.exitonclick()
#Move the turtle with keypress
#create and move the cars
#Detect collision with car
#Detctect when turtle reaches the other side
#create a score board
