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

    def add_tank(self, tank):
        tank.pos = {'x': 100, 'y': 100}
        tank.facing = 0
        self.tanks.append(tank)

    def step(self, delta):
        for tank in self.tanks:
            tank.step(delta)

    def draw_tanks(self):
        self.canvas.delete(tkinter.ALL)
        for tank in self.tanks:
            x, y = tank.pos['x'], tank.pos['y']
            self.canvas.create_line(x, y, x + math.cos(tank.facing) * 10,
                y + math.sin(tank.facing) * 10)
            self.canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10)

def game_loop(game):
    tank = Tank(game)
    game.add_tank(tank)
    tank.tread_target['l'] = 50
    tank.tread_target['r'] = 40

    delta = 0
    while True:
        start = time.perf_counter()
        game.step(delta)
        game.draw_tanks()
        time.sleep(1 / 60)
        delta = time.perf_counter() - start


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=Game.XSIZE, height=Game.YSIZE)
    canvas.pack()

    t = threading.Thread(target=game_loop, args=(Game(canvas),))
    t.start()

    tkinter.mainloop()

if __name__ == '__main__':
    main()