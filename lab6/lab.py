from turtle import *
import random
import math
class Ball(Turtle):
        def __init__(self, radius, color, speed):
            Turtle.__init__(self)
            self.shape("circle")
            self.shapesize(radius/10)
            self.radius = radius
            self.color(color)
            self.speed(speed)

#Ball ball1 = new Ball(circle, 2, "blue", 2)
#Ball ball2 = new Ball(circle, 3, "green", 3)
ball1 = Ball(10, "blue", 2)
ball2 = Ball(15, "red", 3)


def check_collision(ball1, ball2):
    x1=ball1.xcor()
    x2=ball2.xcor()
    y1=ball1.ycor()
    y2=ball2.ycor()
    D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    sum = ball1.radius+ball2.radius
    if(D<=sum):
        ball1.color("green")
        ball2.color("yellow")
        return True
check_collision(ball1, ball2)
    
print (check_collision(ball1, ball2))

temre=[ball1, ball2]
def check_collision_list(temre):
    for i in range(len(temre)):
        for j in range(i+1, len(temre)):
            if(check_collision(temre[i], temre[j])):
                if(temre[i].radius<temre[j].radius):
                    print("the ball number:"+str(i)+" is smaller than the ball number:"+str(j))
                    temre[i].goto(random.randint(-200, 201), random.randint(-200, 201))
                if(temre[j].radius<temre[i].radius):
                    print("the ball number:"+str(j)+" smaller than the bal number:"+str(i))
                    temre[j].goto(random.randint(-200, 201), random.randint(-200, 201))
check_collision_list(temre)












        
