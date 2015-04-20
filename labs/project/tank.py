import math

class Tank(object):
    tread_accel = 20
    tread_max = 50
    turret_speed = 30
    width = 10

    def __init__(self, parent):
        self.parent = parent
        self.pos = None
        self.facing = None
        self.sensors = None
        self.turret_facing = 0
        self.turret_target = 0
        self.cooldown = 0
        self.tread_speed = {'l': 0, 'r': 0}
        self.tread_target = {'l': 0, 'r': 0}

    def step(self, delta):
        #Update tread speed
        self.update_speed(delta)
        self.move_tank(delta)

        #handle gun firing

    def update_speed(self, delta):
        for i in 'lr':
            change = self.tread_target[i] - self.tread_speed[i]

            #enforce max acceleration
            change = max(-self.tread_accel, change)
            change = min(self.tread_accel, change)
            change *= delta
            
            self.tread_speed[i] += change
            self.tread_speed[i] = max(-self.tread_max, self.tread_speed[i])
            self.tread_speed[i] = min(self.tread_max, self.tread_speed[i])


    #This is an approximation. It rotates in place, then moves straight, rather
    #than moving smoothly in a curve. This should be fine as long as delta is
    #small.
    def move_tank(self, delta):
        self.facing += (self.tread_speed['r'] - self.tread_speed['l']) /\
            self.width * delta

        self.pos['x'] += (self.tread_speed['r'] + self.tread_speed['l']) *\
            math.cos(self.facing) * delta
        self.pos['y'] += (self.tread_speed['r'] + self.tread_speed['l']) *\
            math.sin(self.facing) * delta

        #enforce map bounds
        while self.pos['x'] < 0:
            self.pos['x'] += self.parent.XSIZE
        while self.pos['x'] > self.parent.XSIZE:
            self.pos['x'] -= self.parent.XSIZE

        while self.pos['y'] < 0:
            self.pos['y'] += self.parent.YSIZE
        while self.pos['y'] > self.parent.YSIZE:
            self.pos['y'] -= self.parent.YSIZE

        print(self.facing, self.pos)


    def set_pos(self, pos):
        self.pos = pos