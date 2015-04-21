import random

class InvalidTreadID(Exception):
    pass

def random_color():
    """Returns the string of a random color for use with tkinter."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)
