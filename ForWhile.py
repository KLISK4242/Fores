import turtle

t = turtle.Turtle()
t.shape("turtle")


def my_square(size, steps):
    for i in range(steps):
        for j in range(4):
            t.forward(size)
            t.left(90)
        size -= 20
        t.penup()
        t.goto(t.xcor() + 10, t.ycor() + 10)
        t.pendown()


my_square(200, 8)
turtle.exitonclick()