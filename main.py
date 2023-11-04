import turtle

# Screen setup
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = -1.5
ball.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Bricks
number_of_columns = 12
bricks_per_column = 4
bricks = []

# The y coordinate for the top-most brick
top_most_position = wn.window_height() / 2 - 20  # Leave a small gap from the top edge

# Calculate the left-most position for the x coordinate, leaving a small gap from the edge
left_most_position = -wn.window_width() / 2 + 20

for x in range(number_of_columns):
    for y in range(bricks_per_column):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color("green")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        color_index = (x + y) % len(colors)  # This will cycle through the colors list
        brick.color(colors[color_index])
        # Set the brick's x and y positions based on the column and row
        brick.goto(left_most_position + x * (40 + 10), top_most_position - y * (20 + 10))  # Adjust spacing as needed
        bricks.append(brick)


# Functions
def paddle_right():
    x = paddle.xcor()
    if x < 225:
        paddle.setx(x + 20)

def paddle_left():
    x = paddle.xcor()
    if x > -225:
        paddle.setx(x - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop function
def game_loop():
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick and ball collisions
    for brick in bricks:
        if brick.isvisible() and (ball.ycor() > brick.ycor() - 10) and (ball.ycor() < brick.ycor() + 10) and (ball.xcor() > brick.xcor() - 20) and (ball.xcor() < brick.xcor() + 20):
            ball.dy *= -1
            brick.hideturtle()

    # Schedule the next game loop iteration
    wn.ontimer(game_loop, 10)
    wn.update()

# Start the game loop
game_loop()

# Keep the window open
wn.mainloop()
