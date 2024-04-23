from level1 import *
from abc import ABC, abstractmethod

class Game(ABC):
    
    import pygame as p
    
    global WHITE,BLACK,YELLOW,thickness


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    thickness = 20

    def __init__(self, width=320, height=320, root=p):
        self.height = height
        self.width = width
        self.root = root.display.set_mode((width, height))
        self.draw = root.draw
        self.disp = root.display
        self.event = root.event
    
    @property
    @abstractmethod
    def get_thickness(self):
        return self.thickness

        
    def get_width(self):
        return self.root.get_width()

    def get_height(self):
        return self.root.get_height()
    
    def fill(self, clr):
        self.root.fill(clr)

    def draw_line(self, clr, crd: tuple, crd2: tuple):
        self.draw.line(self.root ,clr, crd, crd2)

    def draw_rect(self, clr: tuple, cord: list):
        self.draw.rect(self.root, clr, cord)

    def update_wind(self):
        self.disp.update()

    

    def Rendering(self):
        for y in range(0 , len(map_1)):
            for x in range(0 , len(map_1[y])):
                print(map_1[x][y],x,y)
                if map_1[x][y] == 0:
                    print(map_1[x][y],x,y)
                elif map_1[x][y] == 1:
                    self.draw_rect((255, 0, 0),
                                    [y * self.thickness,
                                     x * self.thickness,
                                     self.thickness,
                                     self.thickness])

                elif map_1[x][y] > 2 and map_1[x][y] <10:
                    print(f"meet an unexpected occurrence: {map_1[x][y],x,y}")
                elif map_1[x][y] >= 10:
                    self.draw_rect((0, 0, 255),
                                    [y * self.thickness,
                                     x * self.thickness,
                                     self.thickness,
                                     self.thickness])
class Creature(object):
    
    def __init__(self, cord: list = [], clr: tuple = BLACK):
        self.color = clr
        self.posi = cord
    

    @abstractmethod
    def pacman_cord(Game):
        for y in range(0 , len(map_1)):
            for x in range(0 , len(map_1[y])):
                if map_1[x][y] == 2:
                    pos_y = y * Game.thickness
                    pos_x = x * Game.thickness
        return  [pos_y,pos_x]

class Enemy(Creature):
    def move():
        pass

class Pacman(Creature):
    
    def __init__(self, cord: list = Creature.pacman_cord(Game), clr: tuple = YELLOW):
        super().__init__(Game)
        self.cord = cord
        self.clr = clr
    
    def draw(self, pacman):
        pacman = self.pacman
        Game.draw_rect(self.clr, pacman)


            
    

    
    def move():
        pass




                


