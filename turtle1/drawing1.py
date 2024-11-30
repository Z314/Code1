
import turtle # The turtle module, part of the standard Python library
import my_graphics # Custom module

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# constants
X1 = 0
Y1 = 0
# myColor = 'blue'
myColor = my_graphics.rgb(255, 0, 0) # calling the rgb function from the my_graphics module 


def main():
    my_graphics.pattern2(X1, Y1, myColor) # calling the pattern2 function from the my_graphics module 


main()
# Keep the window open
turtle.mainloop()
