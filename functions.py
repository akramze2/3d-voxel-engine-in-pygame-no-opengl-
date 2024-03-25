from math import *
from maths import *

def rotate_x(point,angel):
    angel = radians(angel)
    point[2] -= fl_w
    x,z = point[0], point[2]
    point[0] = x * cos(angel) - z * sin(angel)
    point[2] = z * cos(angel) + x * sin(angel)
    return point

def rotate_y(point,angel):
    angel = radians(angel)
    point[2] -= fl_h
    y,z = point[1], point[2]
    point[1] = y * cos(angel) - z * sin(angel)
    point[2] = z * cos(angel) + y * sin(angel)
    return point


def projected_point(point,camera):
    x, y, z = point[0] - camera.pos[0], point[1] - camera.pos[1], point[2] - camera.pos[2]
    x, y, z = rotate_x([x, y, z], camera.rots[0])
    x, y, z = rotate_y([x, y, z], camera.rots[1])
    if z != -fl_w and z != -fl_h:
        x = (x * fl_w) / (fl_w + z)
        y = (y * fl_h) / (fl_h + z)
    if z > -fl_w:
        return [x + width / 2, -y + height / 2], z
    else :
        return None



