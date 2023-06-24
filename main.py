from turtle import Turtle, Screen
from etch_sketch import EtchSketch

my_turtle = Turtle()
my_screen = Screen()

# Etch-a-sketch project #
my_sketch = EtchSketch(my_turtle=my_turtle, my_screen=my_screen)
my_sketch.sketch_box()
