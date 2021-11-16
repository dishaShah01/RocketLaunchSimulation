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

def grass():
    glColor3f(0.0,0.9,0.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for s in range(1000):
        x=random.randint(0,800)
        y=random.randint(0,250)
        glVertex2i(x,y)
    glEnd()

def Rocket_on_Ground():
    global launch,count1,DEG2RAD
    count1+=1
    if(count1==150):
        launch=1
    if(launch==0):
        glClearColor(0.196078  ,0.6 ,0.8,1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
       
        glColor3f(0,0.3,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(0.0,0.0)
        glVertex2f(0.0,250.0)
        glVertex2f(300.0,250.0)
        glVertex2f(600.0,250.0)
        glVertex2f(600.0,0.0)
        glEnd()
        grass()

        glColor3f(0.0,0.0,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(170,0.0)
        glVertex2f(200,0.0)
        glVertex2f(200,180.0)
        glVertex2f(170,180.0)
        glEnd()
        glLineWidth(5)
        glBegin(GL_LINES)
        glVertex2f(170,30.0)
        glVertex2f(262,30.0)

        glVertex2f(170,130.0)
        glVertex2f(260,130.0)
        glEnd()

        glColor3f(0.5,0.0 ,0.9)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,20.0)
        glVertex2f(262.5,20.0)
        glVertex2f(262.5,120.0)
        glVertex2f(237.5,120.0)
        glEnd()

        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,120.0)
        glVertex2f(262.5,120.0)
        glVertex2f(250,170.0)
        glEnd()
        glColor3f(0.9,0.9,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,120.0)
        glVertex2f(217.5,95.0)
        glVertex2f(237.5,95.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(237.5,20.0)
        glVertex2f(217.5,20.0)
        glVertex2f(237.5,70.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5,20.0)
        glVertex2f(282.5,20.0)
        glVertex2f(262.5,70.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5,120.0)
        glVertex2f(262.5,95.0)
        glVertex2f(282.5,95.0)
        glEnd()
        glColor3f(1.0 ,0.5,0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,20.0)
        glVertex2f(244.5,20.0)
        glVertex2f(241,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(246.5,20.0)
        glVertex2f(253.5,20.0)
        glVertex2f(249.5,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5,20.0)
        glVertex2f(255.5,20.0)
        glVertex2f(258.5,0.0)
        glEnd()
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(182.5,15.0)
        glVertex2f(182.5,0.0)
        glVertex2f(187.5,0.0)
        glVertex2f(187.5,10.0)
        glVertex2f(237.5,10.0)
        glVertex2f(237.5,15.0)
        glVertex2f(182.5,15.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(312.5,15.0)
        glVertex2f(312.5,0.0)
        glVertex2f(307.5,0.0)
        glVertex2f(307.5,10.0)
        glVertex2f(262.5,10.0)
        glVertex2f(262.5,15.0)
        glVertex2f(312.5,15.0)
        glEnd()
        glBegin(GL_POLYGON) #Sky  
        glColor3f(0.4, 0.5, 1.0)
        glVertex2i(600, 600)
        glVertex2i(0, 600)
        glColor3f(0.7, 0.7, 1.0)
        glVertex2i(0, 250)
        glVertex2i(600, 250)
        glEnd()
        glutSwapBuffers()
        glutPostRedisplay()
        glFlush()




glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow("rocket")
iterate()
glutDisplayFunc(Showscreen)
glutIdleFunc(Showscreen)
glutMainLoop()