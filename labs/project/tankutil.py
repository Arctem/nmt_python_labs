import math
import random

class InvalidTreadID(Exception):
    pass

def random_color():
    """Returns the string of a random color for use with tkinter."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

def generate_explosion():
    explosion = []
    for i in range(16):
        i *= math.pi / 8
        dist = random.random() * math.sqrt(2) + 1
        explosion.append([dist * math.cos(i), dist * math.sin(i)])
    return explosion
