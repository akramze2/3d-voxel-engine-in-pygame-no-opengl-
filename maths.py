import math
from settings import *

fov = (math.pi/3) * 2

fl_w = (width/2)/(math.tan(fov/2))
fl_h = (height/2)/(math.tan(fov/2))


