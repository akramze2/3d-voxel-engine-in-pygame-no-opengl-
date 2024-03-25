import pygame as pg
from functions import *
from triangle import Triangle

class Cube:
    def __init__(self,world,pos,camera,color):
        self.world = world
        self.pos = pos
        self.color = color
        self.vertecies = [
            [100 ,100 ,100],
            [100 ,-100 ,100],
            [-100 ,-100 ,100],
            [-100 ,100 ,100],
            [100 ,100 ,-100],
            [100 ,-100 ,-100],
            [-100,-100 ,-100],
            [-100 ,100 ,-100]
        ]
        for i in range(8):
            for j in range(3):
                self.vertecies[i][j] += pos[j] * 200
        self.faces = [
            [0,3,2,1],
            [0,1,5,4],
            [3,0,4,7],
            [7,4,5,6],
            [1,2,6,5],
            [7,3,2,6]
        ]
        self.camera = camera
        self.triangeles = []
        color_val = 0
        for face in self.faces:
            point = [self.vertecies[face[0]], self.vertecies[face[1]], self.vertecies[face[2]], self.vertecies[face[3]]]
            self.create_triangele(point, color_val)
            color_val += 10
    
    def draw(self,app):
        for triangle in self.triangeles:
            triangle.draw(app,self.camera)
    
    def create_triangele(self,point,color_val):
        t1 = Triangle([point[0],point[1],point[2]],(self.color[0]+color_val,self.color[1]+color_val,self.color[2]+color_val))
        self.triangeles.append(t1)
        t2 = Triangle([point[0],point[3],point[2]],(self.color[0]+color_val,self.color[1]+color_val,self.color[2]+color_val))
        self.triangeles.append(t2)
    

    

    
    
    
    

