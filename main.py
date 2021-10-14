import time
from turtle import Screen
from snake_body import Snake
from food import Food
from score import Score

screen = Screen()


def screen_setup():
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)


screen_setup()

my_snake = Snake()
food = Food()
score = Score()

is_game_on = True


def play_game():
    global is_game_on
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        my_snake.move()
        # collision with food
        if my_snake.head.distance(food) < 18:
            food.refresh()
            my_snake.add_body()
            score.update_score()

        # collision with walls
        if (my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290
                or my_snake.head.ycor() < -290):
            is_game_on = False
            score.game_over()

        for segment in my_snake.snake_body[1:]:
            if my_snake.head.distance(segment) <= 10:
                is_game_on = False
                score.game_over()


def start_game():
    global is_game_on
    if not is_game_on:
        my_snake.reset()
        score.user_score = 0
    score.clear()
    is_game_on = True
    play_game()


screen.listen()
screen.onkey(key="w", fun=my_snake.face_up)
screen.onkey(key="s", fun=my_snake.face_down)
screen.onkey(key="a", fun=my_snake.face_left)
screen.onkey(key="d", fun=my_snake.face_right)
screen.onkey(key="Up", fun=my_snake.face_up)
screen.onkey(key="Down", fun=my_snake.face_down)
screen.onkey(key="Left", fun=my_snake.face_left)
screen.onkey(key="Right", fun=my_snake.face_right)
screen.onkey(key='space', fun=start_game)
screen.exitonclick()
