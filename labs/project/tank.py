import math
import random

from tankutil import InvalidTreadID, random_color, generate_explosion

class Tank(object):
    tread_accel = 50
    tread_max = 50
    turret_speed = 30 / 180 * math.pi
    radius = 12
    cooldown = 2
    #first row is left half of tank, second is right half
    tank_shape = [[2, 2], [3, 2], [3, 3], [-3, 3], [-3, 2], [-2, 2],
        [-2, -2], [-3, -2], [-3, -3], [3, -3], [3, -2], [2, -2]]
    turret_shape = [[0, 0], [1, 1], [4, 0], [1, -1]]

    def __init__(self):
        self.primary_color = random_color()
        self.secondary_color = random_color()

        self.parent = None
        self.pos = None
        self.facing = None
        self.sensors = []
        self.turret_facing = 0
        self.turret_target = 0
        self.time_since_shot = 0
        self.firing = False
        self.alive = True
        self.tread_speed = {'l': 0, 'r': 0}
        self.tread_target = {'l': 0, 'r': 0}
        self.shape = list(map(lambda p: [4 * p[0], 4 * p[1]], Tank.tank_shape))
        self.turret_shape = list(map(lambda p: [4 * p[0], 4 * p[1]],
            Tank.turret_shape))
        self.dead_shape = list(map(lambda p: [10 * p[0], 10 * p[1]],
            generate_explosion()))

    def ai(self, delta):
        pass

    ###FUNCTIONS TO BE USED BY AI###
    def turret_ready(self):
        """Returns true if the turret can be fired again."""
        return self.time_since_shot > self.cooldown

    def fire(self, should_fire=True):
        self.firing = should_fire

    def set_speed(self, tread, speed):
        if tread not in ['l', 'r']:
            raise InvalidTreadID
        else:
            self.tread_target[tread] = speed

    def read_sensor(self, sensor_num):
        return self.sensors[sensor_num].active

    def set_turret_target(self, target):
        """Tells the turret to turn to the given angle. Expects degrees."""
        self.turret_target = target / 180 * math.pi
    ###END OF FUNCTIONS TO BE USED BY AI###


    def step(self, delta):
        self.time_since_shot += delta
        self.ai(delta)

        self.update_speed(delta)
        self.move_tank(delta)

        self.move_turret(delta)

    def update_speed(self, delta):
        """Update tread speed."""
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
        self.facing += ((self.tread_speed['r'] - self.tread_speed['l']) /
            self.radius) * delta

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

        #print(self.facing, self.pos)

    def move_turret(self, delta):
        #enforce bounds
        self.turret_facing %= 2 * math.pi
        self.turret_target %= 2 * math.pi

        change = self.turret_target - self.turret_facing
        if change > math.pi:
            change = 2 * math.pi - change

        change = max(-self.turret_speed, change)
        change = min(self.turret_speed, change)
        change *= delta
        self.turret_facing += change

    def set_pos(self, pos):
        if not self.pos:
            self.pos = {}
        self.pos['x'], self.pos['y'] = pos

    def kill(self):
        self.alive = False
