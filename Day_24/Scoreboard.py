from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.refresh()

    def go_to_score_drawing_point(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.left(90)
        self.forward(280)
        self.right(90)
        self.pendown()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", move=False, align='center', font=('Century Gothic', 14, 'bold'))

    def refresh(self):
        self.go_to_score_drawing_point()
        self.write(f"Score: {self.score}    High Score: {self.high_score}",
                   move=False, align='center',
                   font=('Century Gothic', 14, 'bold'))
