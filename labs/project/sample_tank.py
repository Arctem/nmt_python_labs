from sensor import Sensor
from tank import Tank

class SampleTank(Tank):
    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 30, 100, False), Sensor(0, 10, 50, True)]

    def ai(self, delta):
        self.set_turret_target(90)
        if self.turret_ready() and self.read_sensor(1):
           self.fire(True)

        #avoid running into things
        if self.read_sensor(0):
            self.set_speed('l', -30)
            self.set_speed('r', -30)
        else:
            self.set_speed('l', 40)
            self.set_speed('r', 35)
