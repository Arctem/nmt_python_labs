import random

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
    def __init__(self, width, height, seed=None):
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
        self.facing = 'down'
        

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
        for x in range(self.width):
            for y in range(self.height):
                print(' ' if self.maze[x][y] else 'X', end='')
            print()

