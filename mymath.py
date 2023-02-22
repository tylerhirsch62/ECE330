import math

def cos(angle):
    angle = math.radians(angle)
    return math.cos(angle)

def acos(input):
    return math.degrees(math.acos(input))

def sin(angle):
    angle = math.radians(angle)
    return math.sin(angle)

def asin(input):
    return math.degrees(math.asin(input))

def tan(angle):
    angle = math.radians(angle)
    return math.tan(angle)

def atan(input):
    return math.degrees(math.atan(input))

def magnitude(x: float, y: float):
    return math.sqrt(x**2 + y**2)

class vector:
    x, y, mag, angle = 0, 0, 0, 0
    def __init__(self, _x: float, _y: float):
        self.x = _x
        self.y = _y
        self.mag = magnitude(self.x, self.y)
        if self.x != 0:
            self.angle = atan(self.y / self.x)
        elif self.y > 0:
            self.angle = 90
        else:
            self.angle = -90

def addvec(list: vector):
    x = 0
    y = 0
    for i in list:
        x += i.x
        y += i.y
    vec = vector(x, y)
    return vec


def divideint(x: float, vec: vector):
    vec = vector(x/vec.mag * cos(vec.angle), x/vec.mag * sin(vec.angle))
    return vec

def dividevec(vec1: vector, vec2: vector):
    vec = vector(vec1.mag/vec2.mag * cos(vec1.angle - vec2.angle), vec1.mag/vec2.mag * sin(vec1.angle - vec2.angle))
    return vec

def multiplyvec(vec1: vector, vec2: vector):
    vec = vector(vec1.mag * vec2.mag * cos(vec1.angle + vec2.angle), vec1.mag*vec2.mag * sin(vec1.angle + vec2.angle))
    return vec

pi = math.pi
mu = 4 * pi * 10**-7