from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

COLLISION_THRESHOLD = 290

# Create and se tup the screen
screen = Screen()
screen.title("The Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.tracer(0) #To fix the snake movement segmentations. The screen needs to be updated after each segment moves forward.

# Create the snake
snake = Snake()

# Create food
food = Food()

# Create scoreboard
scoreboard = Scoreboard()

# Binding up, down, lef and right keys to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_running = True
while game_running:
    screen.update()
    time.sleep(0.05)
    snake.snake_move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.spawn_at_random_location()
        snake.extend_snake_segment()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > COLLISION_THRESHOLD or snake.head.xcor() < -COLLISION_THRESHOLD or snake.head.ycor() > COLLISION_THRESHOLD or snake.head.ycor() < -COLLISION_THRESHOLD:
        game_running = False
        scoreboard.game_over()

    # Detect collision with tail
    for seg in snake.snake_segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_running = False


screen.exitonclick()
