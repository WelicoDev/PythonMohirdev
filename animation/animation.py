import turtle

# Create a turtle object and set some basic properties
t = turtle.Turtle()
t.speed(0)  # Set the animation speed to the maximum
t.penup()   # Lift the pen to avoid drawing lines
t.goto(0, 0)  # Move the turtle to the center of the screen

# Define a function to draw a square with a given size
def draw_square(size):
    t.pendown()  # Lower the pen to start drawing
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.penup()  # Lift the pen to stop drawing

# Loop to animate the squares
for i in range(100):
    draw_square(i*5)  # Increase the size of the square each iteration
    t.right(5)  # Turn the turtle by 5 degrees to the right

# Hide the turtle object after the animation is done
t.hideturtle()

# Wait for the user to close the window before exiting
turtle.done()