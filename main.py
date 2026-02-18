# Case-study #1
# Developers: Popov M., Kartashov A.
#

import turtle

screen = turtle.Screen()
screen.setup(1200, 900)
screen.bgcolor("azure")
turtle.tracer(False)

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
    for _ in range(4):
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
    for _ in range(3):
        turtle.forward(a)
        turtle.left(120)
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
    for _ in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
    turtle.end_fill()


def circle(x, y, r, color):
    '''
    Function drawing circle
    :param x: bottom x coordinate
    :param y: bottom y coordinate
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
    '''
        Function drawing rhomb
        :param x: lower left x coordinate
        :param y: lower left y coordinate
        :param a: side length of rhomb
        :param color: color of rhomb
        :return: None
        '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(a)
        turtle.right(60)
        turtle.forward(a)
        turtle.right(120)
    turtle.end_fill()


def hexagon(x, y, a, color):
    '''
        Function drawing hexagon
        :param x: lower left x coordinate
        :param y: lower left y coordinate
        :param a: side length of hexagon
        :param color: color of hexagon
        :return: None
        '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(a)
        turtle.right(60)
    turtle.end_fill()


def star(x, y, a, color):
    '''
        Function drawing star
        :param x: lower left x coordinate
        :param y: lower left y coordinate
        :param a: side length of star
        :param color: color of star
        :return: None
        '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(5):
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


def rocket():
    '''
    Function drawing rocket
    :return: None
    '''
    rectangle(-500, -100, 80, 200, 'lightgray')
    triangle(-500, -100, 80, 'red')
    circle(-460, -160, 15, 'lightblue')
    circle(-460, -210, 15, 'lightblue')
    circle(-460, -260, 15, 'lightblue')
    rectangle(-530, -250, 30, 50, 'gray')
    rectangle(-420, -250, 30, 50, 'gray')
    turtle.right(60)
    rhomb(-515, -300, 35, 'orange')
    rhomb(-405, -300, 35, 'orange')
    turtle.left(60)


def tank():
    '''
    Function drawing tank
    :return: None
    '''
    rectangle(-220, -200, 150, 70, 'green')
    circle(-270, -320, 25, 'darkgreen')
    circle(-20, -320, 25, 'darkgreen')
    rectangle(-270, -270, 250, 50, 'darkgreen')
    rectangle(-70, -230, 80, 15, 'grey')
    circle(-265, -318, 22, 'black')
    circle(-205, -318, 22, 'black')
    circle(-145, -318, 22, 'black')
    circle(-85, -318, 22, 'black')
    circle(-25, -318, 22, 'black')
    star(-200, -220, 15, 'red')


def flower():
    '''
        Function drawing flower
        :return: None
    '''
    rectangle(160, -130, 5, 200, 'green')
    hexagon(150, -100, 25, 'yellow')
    hexagon(115, -80, 25, 'red')
    hexagon(150, -60, 25, 'orange')
    hexagon(187, -80, 25, 'gold')
    hexagon(187, -123, 25, 'lightgreen')
    hexagon(150, -143, 25, 'lightblue')
    hexagon(114, -123, 25, 'brown')
    turtle.left(60)
    rhomb(165, -250, 40, 'darkgreen')
    turtle.right(60)


def ship():
    '''
    Function drawing ship
    :return: None
    '''
    turtle.left(60)
    triangle(350, -320, 58, 'saddlebrown')
    triangle(500, -320, 58, 'saddlebrown')
    turtle.right(60)
    rectangle(350, -270, 150, 50, 'saddlebrown')
    rectangle(400, -70, 7, 200, 'saddlebrown')
    turtle.right(90)
    triangle(407, -100, 150, 'teal')
    triangle(407, -70, 25, 'red')
    turtle.left(90)
    circle(370, -310, 13, 'lightblue')
    circle(420, -310, 13, 'lightblue')
    circle(470, -310, 13, 'lightblue')
    star(430, -160, 15, 'yellow')


def main():
    house()
    tree()
    car()
    robot()
    rocket()
    tank()
    flower()
    ship()
    turtle.hideturtle()
    turtle.done()
    turtle.update()


if __name__ == '__main__':
    main()
