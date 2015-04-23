import math
import random
import threading
import tkinter
import time

from sample_tank import SampleTank

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
        tank.parent = self
        self.tanks.append(tank)
        for i in self.drawing_map:
            self.drawing_map[i][tank] = {}

    def step(self, delta):
        self.handle_shooting()
        for tank in self.tanks:
            tank.step(delta)
        self.check_collisions(delta)
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

                if tank.alive:
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
                        start_arc = -tank.facing / math.pi * 180 -\
                            sensor.direction - sensor.width / 2
                        if sensor.tracking:
                            start_arc -= tank.turret_facing / math.pi * 180

                        if sensor in tmp_map[tank]:
                            #we can just move these to avoid flicker.
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

                    #draw shooting things
                    if 'shot' in tmp_map[tank]:
                        self.canvas.delete(tmp_map[tank]['shot'])
                    if tank.firing and tank.turret_ready():
                        tmp_map[tank]['shot'] = self.canvas.create_line(
                            x, y, x + tank.turret_range * math.cos(tur_angle),
                            y + tank.turret_range * math.sin(tur_angle),
                            width=3.0)
                else:
                    #if tank is dead, draw explosion and remove other items
                    if 'body' in tmp_map[tank]:
                        self.canvas.delete(tmp_map[tank]['body'])
                    if 'turret' in tmp_map[tank]:
                        self.canvas.delete(tmp_map[tank]['turret'])
                    for sensor in tank.sensors:
                        if sensor in tmp_map[tank]:
                            self.canvas.delete(tmp_map[tank][sensor])
                    if 'shot' in tmp_map[tank]:
                        self.canvas.delete(tmp_map[tank]['shot'])
                    if 'corpse' not in tmp_map[tank]:
                        translation = list(map(lambda v: (x + v[0], y + v[1]),
                            tank.dead_shape))
                        tmp_map[tank]['corpse'] = self.canvas.create_polygon(
                            translation, fill=tank.primary_color,
                            outline=tank.secondary_color)


    def check_arc(self, sensor, tank):
        start = -tank.facing / math.pi * 180 - sensor.direction -\
            sensor.width / 2
        if sensor.tracking:
            start -= tank.turret_facing / math.pi * 180

        #convert to radians and normalize
        start = start / 180 * math.pi
        start %= 2 * math.pi

        for t in self.tanks:
            if t is tank or not t.alive:
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

    def check_collisions(self, delta):
        for t1 in self.tanks:
            if not t1.alive:
                continue
            for t2 in self.tanks:
                if not t2.alive or t1 is t2:
                    continue
                else:
                    x1, y1 = t1.pos['x'], t1.pos['y']
                    x2, y2 = t2.pos['x'], t2.pos['y']
                    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    if dist < t1.radius + t2.radius:
                        t1.kill()
                        t2.kill()

    def handle_shooting(self):
        for t1 in self.tanks:
            if not t1.alive or not (t1.firing and t1.turret_ready()):
                continue
            t1.firing = False
            t1.time_since_shot = 0

            tur_angle = t1.facing + t1.turret_facing
            x1, y1 = t1.pos['x'], t1.pos['y'] #origin of shot
            x2 = x1 + t1.turret_range * math.cos(tur_angle)
            y2 = y1 + t1.turret_range * math.sin(tur_angle)
            for t2 in self.tanks:
                if not t2.alive or t1 is t2:
                    continue
                else:
                    x3, y3 = t2.pos['x'], t2.pos['y'] #target of shot
                    #code based on http://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment
                    l2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                    t = ((x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)) / l2

                    if t < 0:
                        dist = math.hypot(x3 - x1, y3 - y1)
                    elif t > 1:
                        dist = math.hypot(x3 - x2, y3 - y2)
                    else:
                        xtmp = x1 + t * (x2 - x1)
                        ytmp = y1 + t * (y2 - y1)
                        dist = math.hypot(xtmp - x3, ytmp - y3)
                    if dist < t2.radius:
                        t2.kill()


    def place_tanks(self):
        for i, tank in enumerate(self.tanks):
            placed = False
            while not placed:
                pos = (random.randint(0, self.XSIZE),
                    random.randint(0, self.YSIZE))
                acceptable = True

                for t in self.tanks[:i]:
                    dist = math.sqrt((pos[0] - t.pos['x']) ** 2 +
                        (pos[1] - t.pos['y']) ** 2)
                    if dist < (tank.radius + t.radius) * 1.5:
                        acceptable = False

                if acceptable:
                    placed = True
                    tank.set_pos(pos)
                    tank.facing = random.random() * math.pi * 2

    def start(self):
        self.place_tanks()

        t = threading.Thread(target=self.loop)
        t.start()

    def loop(self):
        delta = 0
        while True:
            start = time.perf_counter()
            self.step(delta)
            self.draw_tanks()
            #time.sleep(1 / 60)
            delta = time.perf_counter() - start
            #print(1 / delta)
            # if delta < 1 / 30:
            #     time.sleep(1 / 30 - delta)
            #     delta = time.perf_counter() - start


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=Game.XSIZE, height=Game.YSIZE)
    canvas.pack()

    game = Game(canvas)

    ###ADD YOUR TANKS HERE###
    for i in range(10):
        game.add_tank(SampleTank())
    game.start()

    tkinter.mainloop()

if __name__ == '__main__':
    main()
