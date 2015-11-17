import tkinter

from game import Game
from sample_tank import SampleTank

def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=Game.XSIZE, height=Game.YSIZE)
    canvas.pack()

    game = Game(root, canvas)

    ###ADD YOUR TANKS HERE###
    for i in range(10):
        game.add_tank(SampleTank())
    game.start()

    tkinter.mainloop()

if __name__ == '__main__':
    main()
