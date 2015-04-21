import math
import random
import threading
import tkinter
import time

from tank import Tank

class Game(object):
    XSIZE = 500
    YSIZE = 500

    def __init__(self, canvas):
        self.canvas = canvas
        self.tanks = []
        self.drawing_map = {}
        for x in [-self.XSIZE, 0, self.XSIZE]:
            for y in [-self.YSIZE, 0, self.YSIZE]:
                self.drawing_map[x, y] = {}


    def add_tank(self, tank):
        self.tanks.append(tank)
        for i in self.drawing_map:
            self.drawing_map[i][tank] = {}

    def step(self, delta):
        for tank in self.tanks:
            tank.step(delta)
        for tank in self.tanks:
            for sensor in tank.sensors:
                sensor.active = self.check_arc(sensor, tank)

    def draw_tanks(self):
        """Handle drawing of all things related to tanks."""
        for tank in self.tanks:
            x, y = tank.pos['x'], tank.pos['y']
            angle = tank.facing
            tur_angle = angle + tank.turret_facing

            #use of drawing_map is to help prevent flicker due to how
            #tkinter.Canvas handles buffering
            #it's horrid and I hate it, but unfortunately it's how tkinter
            #does things
            for xoffset, yoffset in self.drawing_map.keys():
                tmp_map = self.drawing_map[xoffset, yoffset]
                x, y = tank.pos['x'] + xoffset, tank.pos['y'] + yoffset

                #draw body
                rotated = list(map(lambda v: [
                    x + v[0] * math.cos(angle) - v[1] * math.sin(angle),
                    y + v[0] * math.sin(angle) + v[1] * math.cos(angle)
                    ], tank.shape))

                if 'body' in tmp_map[tank]:
                    self.canvas.delete(tmp_map[tank]['body'])
                tmp_map[tank]['body'] = self.canvas.create_polygon(rotated,
                    fill=tank.primary_color, outline=tank.secondary_color)

                #draw turret
                rotated = list(map(lambda v: [
                    x + v[0] * math.cos(tur_angle) - v[1] * math.sin(tur_angle),
                    y + v[0] * math.sin(tur_angle) + v[1] * math.cos(tur_angle)
                    ], tank.turret_shape))
                if 'turret' in tmp_map[tank]:
                    self.canvas.delete(tmp_map[tank]['turret'])
                tmp_map[tank]['turret'] = self.canvas.create_polygon(
                    rotated, fill='black')

                #draw all sensors
                for sensor in tank.sensors:
                    start_arc = -tank.facing / math.pi * 180 + sensor.direction -\
                        sensor.width / 2
                    if sensor.tracking:
                        start_arc -= tank.turret_facing / math.pi * 180

                    if sensor in tmp_map[tank]:
                        #self.canvas.delete(tmp_map[tank][sensor])
                        self.canvas.coords(tmp_map[tank][sensor],
                            (x - sensor.size, y - sensor.size,
                            x + sensor.size, y + sensor.size),)
                        self.canvas.itemconfig(tmp_map[tank][sensor],
                            start=start_arc, extent=sensor.width,
                            outline='black',
                            fill=tank.primary_color if sensor.active else '')
                    else:
                        tmp_map[tank][sensor] = self.canvas.create_arc(
                            (x - sensor.size, y - sensor.size,
                            x + sensor.size, y + sensor.size),
                            start=start_arc, extent=sensor.width,
                            outline='black',
                            fill=tank.primary_color if sensor.active else '')

    def check_arc(self, sensor, tank):
        start = -tank.facing / math.pi * 180 + sensor.direction -\
            sensor.width / 2
        if sensor.tracking:
            start -= tank.turret_facing / math.pi * 180

        #convert to radians and normalize
        start = start / 180 * math.pi
        start %= 2 * math.pi

        for t in self.tanks:
            if t is tank:
                continue
            else:
                x1, y1 = t.pos['x'], t.pos['y']
                x2, y2 = tank.pos['x'], tank.pos['y']
                if abs(x1 + self.XSIZE - x2) < abs(x1 - x2):
                    x1 += self.XSIZE
                if abs(y1 + self.YSIZE - y2) < abs(y1 - y2):
                    y1 += self.YSIZE


                dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                angle = math.atan2(y2 - y1, x1 - x2)
                diff = (angle - start) % (2 * math.pi)
                if dist < sensor.size and diff < (sensor.width / 180 * math.pi):
                    return True
        return False

    def start(self):
        tank = Tank(self, random_color(), random_color())
        self.add_tank(tank)
        tank.tread_target['l'] = 35
        tank.tread_target['r'] = 40
        tank.set_pos((100, 100))
        tank.facing = 0
        tank.set_turret_target(120)

        tank = Tank(self, random_color(), random_color())
        self.add_tank(tank)
        tank.tread_target['l'] = 40
        tank.tread_target['r'] = 35
        tank.set_pos((50, 100))
        tank.facing = 0
        tank.set_turret_target(300)

        t = threading.Thread(target=self.loop)
        t.start()

    def loop(self):
        delta = 0
        while True:
            start = time.perf_counter()
            self.step(delta)
            self.draw_tanks()
            time.sleep(1 / 60)
            delta = time.perf_counter() - start



def random_color():
    """Returns the string of a random color for use with tkinter."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=Game.XSIZE, height=Game.YSIZE)
    canvas.pack()

    game = Game(canvas)
    game.start()

    tkinter.mainloop()

if __name__ == '__main__':
    main()
