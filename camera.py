import pygame as pg
from math import *

class Camera:
    def __init__(self):
        self.pos = [0,0,0]
        self.rots = [0,0,0]
        pg.mouse.set_pos((300,300))
        pg.mouse.set_visible(False)
        self.m, self.k = 0,0        
    
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos[2] += cos(radians(self.rots[0])) * 10
            self.pos[0] += sin(radians(self.rots[0])) * 10
        if keys[pg.K_s]:
            self.pos[2] -= cos(radians(self.rots[0])) * 10
            self.pos[0] -= sin(radians(self.rots[0])) * 10
        if keys[pg.K_d]:
            self.pos[2] -= sin(radians(self.rots[0])) * 10
            self.pos[0] += cos(radians(self.rots[0])) * 10
        if keys[pg.K_a]:
            self.pos[2] += sin(radians(self.rots[0])) * 10
            self.pos[0] -= cos(radians(self.rots[0])) * 10
        if keys[pg.K_SPACE]:
            self.pos[1] += 10
        if keys[pg.K_LSHIFT]:
            self.pos[1] -= 10
        if keys[pg.K_LEFT]:
            self.rots[0] += 1
        if keys[pg.K_RIGHT]:
            self.rots[0] -= 1
        mouse_pos = pg.mouse.get_pos()
        self.rots[0] = (int(mouse_pos[0]) - 300) + self.m
        self.rots[1] = -(int(mouse_pos[1]) - 300)
        if mouse_pos[0] > 500:
            self.m = (int(mouse_pos[0]) - 300) + self.m
            pg.mouse.set_pos((300,mouse_pos[1]))
        if mouse_pos[0] < 100:
            self.m = (int(mouse_pos[0]) - 300) + self.m
            pg.mouse.set_pos((300,mouse_pos[1]))
        if mouse_pos[1] > 375:
            pg.mouse.set_pos((mouse_pos[0],375))
        if mouse_pos[1] < 225:
            pg.mouse.set_pos((mouse_pos[0],225))



