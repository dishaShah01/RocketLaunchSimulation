import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

DEG2RAD = 3.14159/180
count=0
count1=0
launch=0
sky_color=0
tx=0
ty=0
fumes=0





glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow("rocket")
iterate()
glutDisplayFunc(Showscreen)
glutIdleFunc(Showscreen)
glutMainLoop()