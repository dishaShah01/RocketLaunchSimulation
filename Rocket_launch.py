import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random





glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow("rocket")
iterate()
glutDisplayFunc(Showscreen)
glutIdleFunc(Showscreen)
glutMainLoop()