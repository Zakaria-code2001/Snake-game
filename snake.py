from turtle import Turtle, Screen

# creating a screen
screen = Screen()
# setting the string size
screen.setup(600, 600)
# a list of tuples containing positions
t_pos = [(0, 0), (-20, 0), (-40, 0)]

# Snake shape creation
for position in t_pos:
    turtel_piece = Turtle("square")
    turtel_piece.color("white")
    turtel_piece.goto(position)

# setting bg color
screen.bgcolor("black")
# setting the title
screen.title("Snake")


# Close the screen when clicked
screen.exitonclick()
