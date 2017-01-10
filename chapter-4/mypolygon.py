from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print(bob)
bob.delay = 0.1

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
    circ = 2 * math.pi * r
    n = 50
    length = int(circ / n)
    polygon(t, n, length)


# polygon(bob, 100, 7)
circle(4, 5)
wait_for_user()