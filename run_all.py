import turtle

from run_ball import Run_ball
from seven_segments_proc import seven_segments


class Run_all(Run_ball, seven_segments):
    def __init__(self):
        Run_ball.__init__(self, 5, 0.2)
        seven_segments.__init__(self, turtle.Turtle(), (255, 0, 0), 0.2)

    def run(self):
        self.random_attr()
        while True:
            for i in range(0, 10):
                self.clear()
                self.draw(i)
                turtle.update()
                turtle.clear()
                self.draw_border()
                for b in self.ball_list:
                    b.draw_ball()
                    b.move_ball(1)
                    b.update_ball_velocity(self.canvas_width, self.canvas_height)
                turtle.update()
                self.my_delay(0.1)
r1 = Run_all()
r1.run()

