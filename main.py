import pygame as pg
from settings import *
from world import World

class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption('3d game')
        self.clock = pg.time.Clock()

        self.world = World()

    def main_loop(self):
        while True:
            self.check_events()
            self.update()
            pg.display.update()
            self.clock.tick(fps)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            
    def update(self):
        self.world.update()
        self.world.show(self.screen)


Game().main_loop()






