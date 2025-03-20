from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

timmy = Turtle()
tommy = Turtle()
tony = Turtle()
tammy = Turtle()
finishline = Turtle()

turtle_list = [timmy, tommy, tony, tammy]
y_coord = [0, -100, 200, 100]
random.shuffle(y_coord)
index = 0

timmy.color((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
tommy.color((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
tammy.color((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
tony.color((random.randint(1,255), random.randint(1,255), random.randint(1,255)))

finishline.penup()
finishline.goto(500, 250)
finishline.pendown()
finishline.goto(500, -150)

for x in turtle_list:
    x.penup()
    x.goto(-500, y_coord[index])
    index += 1

turn = 0
timmy_done = 0
tommy_done = 0
tammy_done = 0
tony_done = 0
while timmy.xcor() < 500 or tommy.xcor() < 500 or tammy.xcor() < 500 or tony.xcor() < 500:
    if timmy_done == 0:
        if timmy.xcor() < 500:
            timmy.forward(random.randint(1, 20))
        else: 
            print(f"Timmy completed turn {turn}")
            timmy_done = 1
    if(tommy_done == 0):
        if tommy.xcor() < 500:
            tommy.forward(random.randint(1, 20))
        else:
            print(f"Tommy completed turn {turn}")
            tommy_done = 1
    if(tammy_done == 0):
        if tammy.xcor() < 500:
            tammy.forward(random.randint(1, 20))
        else:
            print(f"Tammy completed turn {turn}")
            tammy_done = 1
    if(tony_done == 0):
        if tony.xcor() < 500:
            tony.forward(random.randint(1, 20))
        else:
            print(f"Tony completed turn {turn}")
            tony_done = 1
    turn += 1
    
    

screen = Screen()


screen.exitonclick()