import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object for drawing
car = turtle.Turtle()
car.speed(5)

# Draw the main body of the car
car.penup()
car.goto(-150, -40)
car.pendown()
car.color("red")
car.begin_fill()

# Front of the car
car.setheading(0)
car.forward(100)  # Hood
car.circle(50, 180)  # Front curve
car.forward(100)  # Bottom side

# Back of the car
car.left(90)
car.forward(40)
car.left(90)
car.forward(200)  # Top side
car.left(90)
car.forward(40)
car.left(90)
car.forward(100)  # Rear
car.circle(50, 180)  # Back curve
car.forward(100)

car.end_fill()

# Draw the roof of the car
car.penup()
car.goto(-100, 0)
car.pendown()
car.color("black")
car.begin_fill()
car.setheading(30)
car.forward(100)  # Slanted front roof
car.setheading(150)
car.forward(100)  # Slanted back roof
car.setheading(270)
car.forward(50)  # Top
car.end_fill()

# Draw the windows
car.penup()
car.goto(-80, 10)
car.pendown()
car.color("white")
car.begin_fill()
car.setheading(30)
car.forward(30)
car.setheading(150)
car.forward(30)
car.setheading(270)
car.forward(20)
car.end_fill()

car.penup()
car.goto(0, 10)
car.pendown()
car.color("white")
car.begin_fill()
car.setheading(30)
car.forward(30)
car.setheading(150)
car.forward(30)
car.setheading(270)
car.forward(20)
car.end_fill()

# Draw the wheels
car.penup()
car.goto(-120, -50)
car.pendown()
car.color("black")
car.begin_fill()
car.circle(20)
car.end_fill()

car.penup()
car.goto(60, -50)
car.pendown()
car.color("black")
car.begin_fill()
car.circle(20)
car.end_fill()

# Draw the rear spoiler
car.penup()
car.goto(-150, 0)
car.pendown()
car.color("red")
car.setheading(180)
car.forward(20)
car.left(90)
car.forward(10)
car.left(90)
car.forward(40)
car.left(90)
car.forward(10)
car.left(90)
car.forward(20)

# Hide the turtle and display the result
car.hideturtle()

# Keep the window open
turtle.done()
