"""Python turtle로 펜로즈 삼각형 착시를 그립니다."""

import math
import turtle


BACKGROUND = "#08111f"
OUTLINE = "#192740"
COLORS = ("#b5f4ff", "#49c3ed", "#5965ce")


def rotate_points(points, angle):
    """좌표를 원점 주위로 angle도 회전합니다."""
    radians = math.radians(angle)
    cosine = math.cos(radians)
    sine = math.sin(radians)
    return [
        (x * cosine - y * sine, x * sine + y * cosine)
        for x, y in points
    ]


def draw_polygon(pen, points, color):
    """꼭짓점을 순서대로 연결하고 내부를 색칠합니다."""
    pen.penup()
    pen.goto(points[0])
    pen.pencolor(OUTLINE)
    pen.fillcolor(color)
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def draw_penrose_triangle(pen, size=68):
    """같은 모양의 면을 120도씩 회전해 불가능 삼각형을 만듭니다."""
    height = math.sqrt(3) * size

    # 오목한 육각형 한 면입니다. 세 면의 경계가 정확히 이어집니다.
    face = [
        (-0.5 * size, 13 * height / 6),
        (0.5 * size, 13 * height / 6),
        (3.5 * size, -5 * height / 6),
        (-1.5 * size, -5 * height / 6),
        (-size, -height / 3),
        (2 * size, -height / 3),
    ]

    for index, color in enumerate(COLORS):
        points = rotate_points(face, index * 120)
        draw_polygon(pen, points, color)


def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=760)
    screen.title("Penrose Triangle | Python Turtle")
    screen.bgcolor(BACKGROUND)
    screen.tracer(0)

    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    pen.pensize(2)
    pen.penup()

    pen.goto(0, 315)
    pen.color("#e7f5ff")
    pen.write("PENROSE TRIANGLE", align="center", font=("Arial", 25, "bold"))

    draw_penrose_triangle(pen)

    pen.goto(0, -245)
    pen.color("#91a9c2")
    pen.write(
        "THREE SIDES. ONE IMPOSSIBLE LOOP.",
        align="center",
        font=("Arial", 11, "normal"),
    )
    pen.goto(0, -282)
    pen.color("#647992")
    pen.write("Click anywhere to close", align="center", font=("Arial", 10, "normal"))

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
