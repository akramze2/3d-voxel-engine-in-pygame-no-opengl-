from functions import *
import pygame as pg

class Triangle:
    def __init__(self,points,color):
        self.points = points
        self.color = color
    
    def convert(self,points,camera):
        points_ = []
        for i in range(len(points)):
            points_.append([])
        for i in range(len(points)):
            if projected_point(points[i],camera):
                points_[i] = projected_point(points[i],camera)
        return points_
    
    def draw(self,app,camera):
        points = self.convert(self.points,camera)
        if points[0] and points[1] and points[2]:
            for i in range(3):
                points[i] = points[i][0]
        if points[0] and points[1] and points[2]:
            pg.draw.polygon(app,self.color,points)
            




