import random

from sensor import Sensor
from tank import Tank

class TurretTank(Tank):

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 10, 60, True), Sensor(0, 120, 100, False),
            Sensor(120, 120, 100, False), Sensor(240, 120, 100, False)]

    def ai(self, delta):
        if self.turret_ready() and self.read_sensor(0):
           self.fire(True)

        if self.read_sensor(1):
            self.set_turret_target(0)
        elif self.read_sensor(2):
            self.set_turret_target(120)
        elif self.read_sensor(3):
            self.set_turret_target(240)

