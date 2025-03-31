from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Randomly Generate a bunch of cars
# Start at base movement speed
# Increase speed whenever

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.hit = True
        self.movespeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance_create = random.randint(0, 5)
        if chance_create == 0:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self, playerx, playery):
        for cars in self.all_cars:
            if cars.ycor() + 20 > playery and cars.ycor() - 20 < playery and cars.xcor() + 30 > playerx and cars.xcor() - 30 < playerx:
                self.hit =  False
            cars.forward(self.movespeed)

    def increase_speed(self):
        self.movespeed += MOVE_INCREMENT
