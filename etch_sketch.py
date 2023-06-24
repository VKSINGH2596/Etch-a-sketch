class EtchSketch:
    def __init__(self, my_turtle, my_screen):
        self.jimmy = my_turtle
        self.screen = my_screen

    def sketch_box(self):
        self.screen.listen()
        self.screen.onkeypress(key="w", fun=self.move_forward)
        self.screen.onkeypress(key="s", fun=self.move_backward)
        self.screen.onkeypress(key="a", fun=self.turn_left)
        self.screen.onkeypress(key="d", fun=self.turn_right)
        self.screen.onkey(key="c", fun=self.clear_all)
        self.screen.exitonclick()

    def move_forward(self):
        self.jimmy.forward(10)

    def turn_right(self):
        self.jimmy.right(10)

    def turn_left(self):
        self.jimmy.left(10)

    def move_backward(self):
        self.jimmy.backward(10)

    def clear_all(self):
        self.jimmy.clear()
        self.jimmy.penup()
        self.jimmy.home()
        self.jimmy.pendown()
