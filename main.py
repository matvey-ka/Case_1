import turtle


def square(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


def triangle(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()


def rectangle(x, y, a, b, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()


def circle(x, y, r, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def main():
    square(-200, -100, 200, 'red')
    triangle(100, -300, 200, 'blue')
    rectangle(-200, 200, 200, 100, 'green')
    circle(200, 50, 100, 'yellow')
    turtle.done()


main() $
