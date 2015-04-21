import math
import random

from sensor import Sensor

class Tank(object):
    tread_accel = 20
    tread_max = 50
    turret_speed = 30 / 180 * math.pi
    radius = 12
    #first row is left half of tank, second is right half
    tank_shape = [[2, 2], [3, 2], [3, 3], [-3, 3], [-3, 2], [-2, 2],
        [-2, -2], [-3, -2], [-3, -3], [3, -3], [3, -2], [2, -2]]
    turret_shape = [[0, 0], [1, 1], [4, 0], [1, -1]]

    def __init__(self, parent, primary_color, secondary_color):
        self.parent = parent
        self.primary_color = primary_color
        self.secondary_color = secondary_color

        self.pos = None
        self.facing = None
        self.sensors = [Sensor(0, 30, 100, False), Sensor(0, 10, 50, True)]
        self.turret_facing = 0
        self.turret_target = 0
        self.cooldown = 0
        self.alive = True
        self.tread_speed = {'l': 0, 'r': 0}
        self.tread_target = {'l': 0, 'r': 0}
        self.shape = list(map(lambda p: [4 * p[0], 4 * p[1]], Tank.tank_shape))
        self.turret_shape = list(map(lambda p: [4 * p[0], 4 * p[1]],
            Tank.turret_shape))
        self.dead_shape = list(map(lambda p: [10 * p[0], 10 * p[1]],
            generate_explosion()))

    def step(self, delta):
        #Update tread speed
        self.update_speed(delta)
        self.move_tank(delta)

        self.move_turret(delta)

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

        print(self.facing, self.pos)

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

    #value should be given in degrees
    def set_turret_target(self, target):
        self.turret_target = target / 180 * math.pi

    def set_pos(self, pos):
        if not self.pos:
            self.pos = {}
        self.pos['x'], self.pos['y'] = pos

    def kill(self):
        self.alive = False

def generate_explosion():
    explosion = []
    for i in range(16):
        i *= math.pi / 8
        dist = random.random() * math.sqrt(2) + 1
        explosion.append([dist * math.cos(i), dist * math.sin(i)])
    return explosion
