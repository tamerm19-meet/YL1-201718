###########################1

from turtle import *
import turtle

##class  Square (Turtle):
##    def __init__(self, size):
##        Turtle.__init__(self)
##
##
##        self.shapesize(size)
##        self.shape("square")

###########################2




class Hexagon (Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.begin_poly()
        for i in range(6):
            self.pu()
            self.rt(60)
            self.fd(100)
        self.end_poly()
        p =self.get_poly()
        register_shape("hexagon",p)
        self.shape("hexagon")
H1= Hexagon(1)

