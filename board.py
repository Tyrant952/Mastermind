'''
Bowen Niu
CS 5001 Fall 2023
Final Project
'''
# Constants
import turtle
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 800
OFFSET = 8
LINEWIDTH = 5

def draw_gameboard(t):
    draw_rectangle_down(t, 120, WINDOW_WIDTH - OFFSET * 2 - 5)
    draw_rectangle_left(t, 460, WINDOW_HEIGHT - 163)
    draw_rectangle_right(t, WINDOW_WIDTH - 500, WINDOW_HEIGHT - 163)


def draw_rectangle_left(t, width, height):
    # Positioning the turtle based on alignment
    t.penup()
    t.goto(-WINDOW_WIDTH/2 + OFFSET, WINDOW_HEIGHT/2 - OFFSET)
    t.pendown()

    # Drawing the rectangle
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_rectangle_down(t, width, height):
    # Positioning the turtle based on alignment
    t.penup()
    t.goto(-WINDOW_WIDTH/2 + OFFSET, -WINDOW_HEIGHT/2 + OFFSET + LINEWIDTH)
    t.pendown()

    # Drawing the rectangle
    for _ in range(2):
        t.forward(height)
        t.left(90)
        t.forward(width + LINEWIDTH * 2)
        t.left(90)

def draw_rectangle_right(t, width, height):
    # Positioning the turtle based on alignment
    t.penup()
    t.pencolor("blue")
    t.goto(WINDOW_WIDTH/2 - OFFSET - LINEWIDTH, WINDOW_HEIGHT/2 - OFFSET)
    t.pendown()

    # Drawing the rectangle
    for _ in range(2):
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(width)

def draw_yes(x, y):
    turtle.register_shape("checkbutton.gif")
    t1 = turtle.Turtle()
    t1.shape("checkbutton.gif")
    t1.penup()
    t1.goto(x, y)
    t1.pendown()

def draw_no(x, y):
    turtle.register_shape("xbutton.gif")
    t1 = turtle.Turtle()
    t1.shape("xbutton.gif")
    t1.penup()
    t1.goto(x, y)
    t1.pendown()

def draw_quit(x, y):
    turtle.register_shape("quit_resized.gif")
    t1 = turtle.Turtle()
    t1.shape("quit_resized.gif")
    t1.penup()
    t1.goto(x, y)
    t1.pendown()