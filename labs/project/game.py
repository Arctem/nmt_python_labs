import math
import threading
import tkinter
import time

from tank import Tank

class Game(object):
    XSIZE = 300
    YSIZE = 300

    def __init__(self, canvas):
        self.canvas = canvas
        self.tanks = []
        self.drawing_map = {}

    def add_tank(self, tank):
        tank.set_pos((100, 100))
        tank.facing = 0
        tank.set_turret_target(120)
        self.tanks.append(tank)
        self.drawing_map[tank] = {}

    def step(self, delta):
        for tank in self.tanks:
            tank.step(delta)

    def draw_tanks(self):
        for tank in self.tanks:
            x, y = tank.pos['x'], tank.pos['y']
            angle = tank.facing
            tur_angle = angle + tank.turret_facing

            #use of drawing_map is to help prevent flicker due to how
            #tkinter.Canvas handles buffering
            if 'body' in self.drawing_map[tank]:
                self.canvas.delete(self.drawing_map[tank]['body'])
            #self.drawing_map[tank]['body'] = self.canvas.create_rectangle(
                #x - 10, y - 10, x + 10, y + 10)
            rotated = list(map(lambda v: [
                x + v[0] * math.cos(angle) - v[1] * math.sin(angle),
                y + v[0] * math.sin(angle) + v[1] * math.cos(angle)
                ], tank.shape))
            self.drawing_map[tank]['body'] = self.canvas.create_polygon(rotated,
                fill='#ff0000')

            rotated = list(map(lambda v: [
                x + v[0] * math.cos(tur_angle) - v[1] * math.sin(tur_angle),
                y + v[0] * math.sin(tur_angle) + v[1] * math.cos(tur_angle)
                ], tank.turret_shape))
            if 'turret' in self.drawing_map[tank]:
                self.canvas.delete(self.drawing_map[tank]['turret'])
            self.drawing_map[tank]['turret'] = self.canvas.create_polygon(
                rotated, fill='black')

    def start(self):
        tank = Tank(self)
        self.add_tank(tank)
        tank.tread_target['l'] = 50
        tank.tread_target['r'] = 40

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


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=Game.XSIZE, height=Game.YSIZE)
    canvas.pack()

    game = Game(canvas)
    game.start()

    tkinter.mainloop()

if __name__ == '__main__':
    main()
