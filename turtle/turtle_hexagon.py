import turtle

turtle.speed(12)
turtle.bgcolor("black")

colors = ["red", "blue", "green", "yellow", "#727272", "violet"]

for i in range(360):
    turtle.pencolor(colors[i%6])
    turtle.forward(i)
    turtle.left(60)
