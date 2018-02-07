from turtle import *


class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.pu()
        self.x=x
        self.goto(x,y)
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.shape("circle")
        self.color(color)
        self.shapesize(r/10)

    def move(self, width, height):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x+self.dx
        new_y = current_y+self.dy

        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        up_side_ball = new_y + self.r
        down_side_ball = new_y - self.r
        self.goto(new_x, new_y)
        if(left_side_ball<=-width or right_side_ball>=width):
            self.dx*=-1
        if(up_side_ball <= - height or down_side_ball>=height):
            self.dy*=-1
