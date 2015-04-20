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
        tank.pos = {'x': 100, 'y': 100}
        tank.facing = 0
        self.tanks.append(tank)
        self.drawing_map[tank] = {}

    def step(self, delta):
        for tank in self.tanks:
            tank.step(delta)

    def draw_tanks(self):
        for tank in self.tanks:
            x, y = tank.pos['x'], tank.pos['y']

            if 'facing' in self.drawing_map[tank]:
                self.canvas.delete(self.drawing_map[tank]['facing'])
            self.drawing_map[tank]['facing'] = self.canvas.create_line(x, y, 
                x + math.cos(tank.facing) * 10, y + math.sin(tank.facing) * 10)

            if 'body' in self.drawing_map[tank]:
                self.canvas.delete(self.drawing_map[tank]['body'])
            self.drawing_map[tank]['body'] = self.canvas.create_rectangle(
                x - 10, y - 10, x + 10, y + 10)

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