import turtle

screen = turtle.Screen()
screen.setup(1200, 900)


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


def rhomb(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()


def hexagon(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.end_fill()


def star(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(72)
    turtle.forward(a)
    turtle.right(144)
    turtle.forward(a)
    turtle.left(72)
    turtle.forward(a)
    turtle.right(144)
    turtle.forward(a)
    turtle.left(72)
    turtle.forward(a)
    turtle.right(144)
    turtle.forward(a)
    turtle.left(72)
    turtle.forward(a)
    turtle.right(144)
    turtle.forward(a)
    turtle.left(72)
    turtle.forward(a)
    turtle.right(144)
    turtle.end_fill()


def main():
    '''square(-200, -100, 100, 'red')
    triangle(100, -300, 100, 'blue')
    rectangle(-200, 200, 100, 50, 'green')
    circle(200, 50, 50, 'yellow')
    rhomb(200, 50, 50, 'red')
    hexagon(-100, 50, 50, 'blue')
    star(300, 50, 50, 'black')'''
    turtle.done()


main()
