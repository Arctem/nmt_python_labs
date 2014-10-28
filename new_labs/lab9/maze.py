import random
import time

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

offset = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class Maze:
    #Each tile in the maze is either open or shut, with no data on walls in each direction
    #This means that effectively odd-indexed values are spaces and even-indexed values are
    #either walls or gaps between two spaces. Example representation of a simple maze:

    ###########
    #   #   # #
    # # ### # #
    # #   #   #
    # # # # # #
    # # #   # #
    ###########

    #Note that every space represented by two odd indices is open, every space with two even
    #indices is closed, and a space with one of each can be either, determining the path
    #through the maze.

    #Note that the dimensions are counted in terms of number of possible spaces, so the
    #internal size is different.
    def __init__(self, width=10, height=10, seed=None):
        if not seed:
            seed = random.randint(0, 2**16)
        self.rand = random.Random(seed)
        self.width = width * 2 + 1
        self.height = height * 2 + 1
        self.maze = []
        self.build_maze()

        #player info
        self.pos = (1, 1)
        self.end = (self.width - 2, self.height - 2)
        self.facing = DOWN
        self.steps = 0
        self.start_time = time.clock()
        

    def build_maze(self):
        for x in range(self.width):
            self.maze.append([False] * self.height)
            #self.maze.append([])
            #for y in range(self.height):
                #self.maze[-1].append(x % 2 == 1 and y % 2 == 1)

        stack = []
        start = (1, 1)
        stack.append(start)
        
        while stack:
            x, y = stack[-1]
            self.maze[x][y] = True
            possibles = []
            if x > 2 and not self.maze[x-2][y]:
                possibles.append((x-2, y))
            if x < self.width - 2 and not self.maze[x+2][y]:
                possibles.append((x+2, y))
            if y > 2 and not self.maze[x][y-2]:
                possibles.append((x, y-2))
            if y < self.height - 2 and not self.maze[x][y+2]:
                possibles.append((x, y+2))
            if possibles:
                stack.append(self.rand.choice(possibles))
                x2, y2 = stack[-1]
                #set space between them to True
                self.maze[int((x+x2)/2)][int((y+y2)/2)] = True
            else:
                stack.pop()
                
        self.print_maze()

    def print_maze(self):
        for y in range(self.width):
            for x in range(self.height):
                print(' ' if self.maze[x][y] else 'X', end='')
            print()

    def look_around(self):
        #return string of 3 space-separated numbers, representing clear distance
        #to left, in front, and to right of player
        left = 0
        off = offset[(self.facing-1)%4]
        print(off)
        x, y = self.pos[0] + off[0], self.pos[1] + off[1]
        print(x, y)
        while 0 <= x < self.width and 0 <= y < self.height and self.maze[x][y]:
            print(x, y)
            left += 1
            x += off[0] * 2
            y += off[1] * 2
        
        front = 0
        off = offset[self.facing%4]
        x, y = self.pos[0] + off[0], self.pos[1] + off[1]
        while 0 <= x < self.width and 0 <= y < self.height and self.maze[x][y]:
            front += 1
            x += off[0] * 2
            y += off[1] * 2
        
        right = 0
        off = offset[(self.facing+1)%4]
        x, y = self.pos[0] + off[0], self.pos[1] + off[1]
        while 0 <= x < self.width and 0 <= y < self.height and self.maze[x][y]:
            right += 1
            x += off[0] * 2
            y += off[1] * 2

        return "{} {} {}".format(left, front, right)
