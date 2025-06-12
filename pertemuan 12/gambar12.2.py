import vpython
vpython.no_notebook = True
from vpython import *


box1 = box(pos=vector(-3, 0, 0), size=vector(2, 2, 2), color=color.red, opacity=0.5)
sphere1 = sphere(pos=vector(-2, 0, 0), radius=1.2, color=color.blue, opacity=0.5)

box2 = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.orange, opacity=0.5)
sphere2 = sphere(pos=vector(0.5, 0, 0), radius=1, color=color.white, opacity=0.2)

box3 = box(pos=vector(3, 0, 0), size=vector(2, 2, 2), color=color.green, opacity=0.5)
sphere3 = sphere(pos=vector(3, 0, 0), radius=1.2, color=color.yellow, opacity=0.5)


while True:
    rate(60)  #60 FPS loop kosong
