import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("도형 만들기")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
t.pensize(2)
t.pencolor("black")

def draw_shape(points):
    t.penup()
    t.goto(points[0])
    t.pendown()

    for x, y in points:
        t.goto(x, y)

    t.goto(points[0])

points1 = [(-34, 205), (34, 205), (238, -148),
           (-102, -148), (-68, -89), (136, -89)]

points2 = [(-204, -207), (-238, -148), (-34, 205),
           (136, -89), (68, -89), (-34, 87)]

points3 = [(238, -148), (204, -207), (-204, -207),
           (-34, 87), (0, 29), (-102, -148)]

draw_shape(points1)
draw_shape(points2)
draw_shape(points3)

t.hideturtle()
turtle.done()
