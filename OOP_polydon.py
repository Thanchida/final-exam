import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = []
        self.color = []
        self.border_size = border_size

    def draw_polygon(self, color, location):
        turtle.penup()
        turtle.goto(location[0][0], location[0][1])
        turtle.setheading(self.orientation)
        turtle.color(color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def draw_small_polygon(self):
        # specify a reduction ratio to draw a smaller polygon inside the one above
        reduction_ratio = 0.618

        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio

    def initialize(self):
        location = random.randint(-300, 300), random.randint(-200, 200)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.location.append(location)
        self.color.append(color)

    def simulation(self):
        print('self.location', self.location)
        reduction_ratio = 0.618
        while True:
            self.draw_polygon(self.color, self.location)
        # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            self.draw_polygon(self.color, self.location)
            self.location[0][0] = turtle.pos()[0]
            self.location[0][1] = turtle.pos()[1]
            self.size *= reduction_ratio
        # for i in range(len(self.location)):
        #     self.location[i] = turtle.pos()[0]
        #     self.location[i+1] = turtle.pos()[1]
        #     self.size *= reduction_ratio
        #     self.draw_polygon(self.color[i], self.location[i])
        #     self.draw_small_polygon()
        # while True:
        #     turtle.clear()
        #     for i in range(self.num_sides):
        #         self.draw_polygon(self.color[i], self.location[i])
        #         self.draw_small_polygon()
        #     turtle.update()

num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
border_size = random.randint(1, 10)
polygon = Polygon(num_sides, size, orientation, border_size)
polygon.initialize()
polygon.simulation()


