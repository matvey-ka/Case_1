# Case-study #1
# Developers: Popov M., Kartashov A.
#

import turtle

screen = turtle.Screen()
screen.setup(1200, 900)
turtle.speed(50)


def square(x, y, a, color):
    '''
    Function drawing square
    :param x: upper left x coordinate
    :param y: upper left y coordinate
    :param a: side length of square
    :param color: color of square
    :return: None
    '''
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
    '''
    Function drawing triangle
    :param x: lower left x coordinate
    :param y: lower left y coordinate
    :param a: side length of triangle
    :param color: color of triangle
    :return: None
    '''
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
    '''
    Function drawing rectangle
    :param x: upper left x coordinate
    :param y: upper left y coordinate
    :param a: side 1 length of rectangle
    :param b: side 2 length of rectangle
    :param color: color of rectangle
    :return: None
    '''
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
    '''
    Function drawing circle
    :param x: lower central x coordinate
    :param y: lower central y coordinate
    :param r: radius of circle
    :param color: color of circle
    :return: None
    '''
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
    '''
    Function drawing house
    :return: None
    '''
    square(-500, 200, 150, 'khaki')
    square(-400, 160, 30, 'lightblue')
    square(-480, 160, 30, 'lightblue')
    triangle(-500, 200, 150, 'brown')
    square(-440, 260, 30, 'lightblue')
    rectangle(-440, 100, 30, 50, 'saddlebrown')


def tree():
    '''
    Function drawing tree
    :return: None
    '''
    rectangle(-100, 130, 30, 80, 'saddlebrown')
    triangle(-125, 130, 80, 'green')
    triangle(-125, 180, 80, 'green')
    triangle(-125, 230, 80, 'green')
    star(-125, 320, 30, 'red')


def car():
    '''
    Function drawing car
    :return: None
    '''
    rectangle(100, 120, 150, 40, 'red')
    circle(130, 50, 20, 'black')
    circle(220, 50, 20, 'black')
    rectangle(140, 170, 75, 50, 'orange')
    rectangle(148, 160, 60, 30, 'lightblue')


def robot():
    '''
    Function drawing robot
    :return: None
    '''
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


if __name__ == '__main__':
    main()
