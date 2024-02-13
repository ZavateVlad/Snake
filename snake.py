from turtle import Turtle
import random
MOVE_DISTANCE = 20
STARTING_POSITION = [(-20, 0), (-40, 0), (-60, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.new_x = self.segments[seg_num - 1].xcor()
            self.new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(self.new_x, self.new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_block = Turtle('square')
        new_block.color('white')
        new_block.penup()
        new_block.goto(position)
        self.segments.append(new_block)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)







