from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

# Challenge 4,page 40; start here next time
def circle(t, r):
    circ = r * 2


polygon(bob, 100, 7)
wait_for_user()