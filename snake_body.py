from turtle import Turtle

MOVE_DISTANCE = 20


def make_seg():
    t = Turtle("square")
    t.color("grey")
    t.up()
    return t


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.color("dark orange")

    def create_snake(self):
        a = self.snake_body
        for i in range(3):
            t = make_seg()
            t.fd(-20 * i)
            a.append(t)

    def add_body(self):
        a = self.snake_body
        t = make_seg()
        t.goto(a[-1].position())
        a.append(t)

    def reset(self):
        for i in self.snake_body:
            i.ht()
        self.snake_body = []
        self.__init__()

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def face_right(self):
        if self.head.heading() in [90, -90, 270]:
            self.head.seth(0)

    def face_left(self):
        if self.head.heading() in [90, -90, 270]:
            self.head.seth(180)

    def face_up(self):
        if self.head.heading() in [0, 180]:
            self.head.seth(90)

    def face_down(self):
        if self.head.heading() in [0, 180]:
            self.head.seth(270)
