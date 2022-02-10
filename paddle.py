from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(cords)

    def go_up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            pass

    def go_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            pass