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

    def draw_polygon(self,color, location):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(self.orientation)
        turtle.color(color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
            turtle.penup()

    def initialize(self):
        location1 = random.randint(-300, 300)
        location2 = random.randint(-200, 200)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.location.append(location1)
        self.location.append(location2)
        self.color.append(color)

    def simulation(self, num_polygon):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        print('self.location', self.location)
        print('self.color', self.color)
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(num_polygon):
            self.draw_polygon(self.color, self.location)

            reduction_ratio = 0.618
            turtle.penup()
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= reduction_ratio
        turtle.done()

num_polygon = int(input('Enter number: '))
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
border_size = random.randint(1, 10)
polygon = Polygon(num_sides, size, orientation, border_size)
polygon.initialize()
polygon.simulation(num_polygon)
# polygon.initialize()
# polygon.simulation(num_polygon)
#     def get_new_color(self):
#         return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
# turtle.speed(0)
# turtle.bgcolor('black')
# turtle.tracer(0)
# turtle.colormode(255)
#
# # draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)
#
# # specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618
#
# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# print('self.lacation', location)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]
#
# # adjust the size according to the reduction ratio
# size *= reduction_ratio
#
# # draw the second polygon embedded inside the original
# draw_polygon(num_sides, size, orientation, location, color, border_size)
#
# # hold the window; close it by clicking the window close 'x' mark
# turtle.done()