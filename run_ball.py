import turtle
import ball
import random

class Run_ball:
    def __init__(self, n_balls,dt):
        self.num_balls = n_balls
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.ball_list = []
        self.dt = dt

    def random_attr(self):
        for i in range(self.num_balls):
            xpos = random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            ypos = random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = 10*random.uniform(-1.0, 1.0)
            vy = 10*random.uniform(-1.0, 1.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball.Ball(xpos, ypos, vx, vy, ball_color, self.ball_radius))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def runb(self):
        self.random_attr()
        while True:
            turtle.clear()
            self.draw_border()
            for b in self.ball_list:
                b.draw_ball()
                b.move_ball(self.dt)
                b.update_ball_velocity(self.canvas_width, self.canvas_height)
            turtle.update()



