import turtle
import math

# Create the turtle object
t = turtle.Turtle() # creates an instance of the Turtle class from the turtle graphics library and assigns it to the variable t (a turtle object)
t.shape("turtle")  # Change turtle shape to a turtle icon

# Set the speed of drawing (0 is fastest, 10 is slower)
t.speed(1)


def pattern1(x, y, color):
    '''
    Square, Spiral type pattern
    '''
    goldenRatio = (1 + math.sqrt(5)) / 2
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for i in range(1,500):
        multiplyGoldenRatio = i * goldenRatio
        t.right(goldenRatio * 180/math.pi)
        t.forward(multiplyGoldenRatio)


def pattern2(x, y, color):
    '''
    Circular pattern
    '''
    goldenRatio = (1 + math.sqrt(5)) / 2
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for i in range(1, 500):
        multiplyGoldenRatio = 2 * i * goldenRatio
        t.circle(multiplyGoldenRatio)


def fibonacci(n):
    '''
    Generates a sequence of n Fibonacci numbers, e.g for n=6: 0, 1, 1, 2, 3, 5...
    '''
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

# Function to normalize RGB values from 0-255 to 0-1


def rgb(r, g, b):
    '''
    Returns full range of RGB colors
    '''
    return (r / 255.0, g / 255.0, b / 255.0)
