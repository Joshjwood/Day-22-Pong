from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.clear()
        self.p1score = 0
        self.p2score = 0
        self.write(f"{self.p1score}      -      {self.p2score}", False, align="Center", font=("Arial", 24, "normal"))
        
    def player2score(self):
        self.p2score += 1
        self.clear()
        self.write(f"{self.p1score}      -      {self.p2score}", False, align="Center", font=("Arial", 24, "normal"))
        
    def player1score(self):
        self.p1score += 1
        self.clear()
        self.write(f"{self.p1score}      -      {self.p2score}", False, align="Center", font=("Arial", 24, "normal"))