import turtle
import math
bob = turtle.Turtle()
print(bob)

# bob.pd()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

def timesAng(times):
    ang = 360 / times
    for i in range(times):
        bob.fd(100)
        bob.lt(ang)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

# timesAng(9)
polygon(bob, n=7, length=70)
# circle(bob, 120)
turtle.mainloop()