import turtle

screen = turtle.Screen()
screen.setup(1200, 900)
turtle.speed(50)


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


def house():
    square(-500, 200, 150, 'khaki')
    square(-400, 160, 30, 'lightblue')
    square(-480, 160, 30, 'lightblue')
    triangle(-500, 200, 150, 'brown')
    square(-440, 260, 30, 'lightblue')
    rectangle(-440, 100, 30, 50, 'saddlebrown')


def tree():
    rectangle(-100, 130, 30, 80, 'saddlebrown')
    triangle(-125, 130, 80, 'green')
    triangle(-125, 180, 80, 'green')
    triangle(-125, 230, 80, 'green')
    star(-125, 320, 30, 'red')


def car():
    rectangle(100, 120, 150, 40, 'red')
    circle(130, 50, 20, 'black')
    circle(220, 50, 20, 'black')
    rectangle(140, 170, 75, 50, 'orange')
    rectangle(148, 160, 60, 30, 'lightblue')


def robot():
    rectangle(400, 120, 20, 70, 'gray')
    rectangle(450, 120, 20, 70, 'gray')
    square(390, 210, 90, 'darkgray')
    rectangle(380, 210, 20, 70, 'gray')
    rectangle(470, 210, 20, 70, 'gray')
    hexagon(415, 280, 40, 'lightgray')
    circle(420, 240, 5, 'red')
    circle(450, 240, 5, 'red')


def main():
    house()
    tree()
    car()
    robot()
    turtle.done()


main()
