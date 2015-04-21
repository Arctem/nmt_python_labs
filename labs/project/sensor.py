class Sensor(object):
    def __init__(self, direction, width, size, tracking=False):
        self.direction = direction
        self.width = width
        self.size = size
        self.tracking = tracking
        self.active = False
