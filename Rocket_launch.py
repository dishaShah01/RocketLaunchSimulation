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

def stars():
    glColor3f(1.0,1.0,1.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    for s in range(50):
        x=random.randint(0,800)
        y=random.randint(0,800)
        glVertex2i(x,y)
    glEnd()


def grass():
    glColor3f(0.0,0.9,0.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for s in range(1000):
        x=random.randint(0,800)
        y=random.randint(0,250)
        glVertex2i(x,y)
    glEnd()

def control():
    global launch,sky_color,count,count1,tx,ty,fumes,DEG2RAD
    count1+=1
    if(count1==775659):
        launch=1
    elif (launch == 1 and (count1 == 805407 )):
        rocket_position()
    elif (launch == 1 and count1 >= 1000000):
        Moving_Rocket()    

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

def rocket_position(): 

    global count,fumes
    count+=1
    for i in range(200):
        glClearColor(0.196078,0.6 ,0.8,1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glBegin(GL_POLYGON) #Sky  
        glColor3f(0.4, 0.5, 1.0)
        glVertex2i(600, 600)
        glVertex2i(0, 600)
        glColor3f(0.7, 0.7, 1.0)
        glVertex2i(0, 0)
        glVertex2i(600, 0)
        glEnd() 
        glColor3f(0.5,0.0 ,0.9)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,20.0+i)
        glVertex2f(262.5,20.0+i)
        glVertex2f(262.5,120.0+i)
        glVertex2f(237.5,120.0+i)
        glEnd()
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,120.0+i)
        glVertex2f(262.5,120.0+i)
        glVertex2f(250,170.0+i)
        glEnd()
        glColor3f(0.9,0.9,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,120.0+i)
        glVertex2f(217.5,95.0+i)
        glVertex2f(237.5,95.0+i)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(237.5,20.0+i)
        glVertex2f(217.5,20.0+i)
        glVertex2f(237.5,70.0+i)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5,20.0+i)
        glVertex2f(282.5,20.0+i)
        glVertex2f(262.5,70.0+i)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5,120.0+i)
        glVertex2f(262.5,95.0+i)
        glVertex2f(282.5,95.0+i)
        glEnd()
        glColor3f(0.556863 ,0.137255  ,0.419608)
        glBegin(GL_POLYGON)
        glVertex2f(237.5,20.0+i)
        glVertex2f(244.5,20.0+i)
        glVertex2f(241,0.0+i)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(246.5,20.0+i)
        glVertex2f(253.5,20.0+i)
        glVertex2f(249.5,0.0+i)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5,20.0+i)
        glVertex2f(255.5,20.0+i)
        glVertex2f(258.5,0.0+i)
        glEnd()
        if((fumes%2)==0):
            glColor3f(1.0,0.25,0.0)
        else:
            glColor3f(1.0,0.816,0.0)

        glBegin(GL_POLYGON)
        glVertex2f(237.5,20+i)
        glVertex2f(234.16,16.66+i)
        glVertex2f(230.82,13.32+i)
        glVertex2f(227.48,9.98+i)
        glVertex2f(224.14,6.64+i)
        glVertex2f(220.8,3.3+i)
        glVertex2f(217.5,0+i)
        glVertex2f(221.56,-5+i)
        glVertex2f(225.62,-10+i)
        glVertex2f(229.68,-15+i)
        glVertex2f(233.74,-20+i)
        glVertex2f(237.8,-25+i)
        glVertex2f(241.86,-30+i)
        glVertex2f(245.92,-35+i)
        glVertex2f(250,-40+i)
        glVertex2f(254.06,-35+i)
        glVertex2f(258.12,-30+i)
        glVertex2f(262.18,-25+i)
        glVertex2f(266.24,-20+i)
        glVertex2f(270.3,-15+i)
        glVertex2f(274.36,-10+i)
        glVertex2f(278.42,-5+i)
        glVertex2f(282.5,0+i)
        glVertex2f(278.5,4+i)
        glVertex2f(274.5,8+i)
        glVertex2f(270.5,12+i)
        glVertex2f(266.5,16+i)
        glVertex2f(262.5,20+i)
        glEnd()

        if((fumes%2)==0):
            glColor3f(1.0,0.816,0.0)
        else:
            glColor3f(1.0,0.25,0.0)        

        glBegin(GL_POLYGON)
        glVertex2f(237.5,20+i)
        glVertex2f(236.5,17.5+i)
        glVertex2f(235.5,15+i)
        glVertex2f(234.5,12.5+i)
        glVertex2f(233.5,10+i)
        glVertex2f(232.5,7.5+i)
        glVertex2f(236,5+i)
        glVertex2f(239.5,2.5+i)
        glVertex2f(243,0+i)
        glVertex2f(246.5,-2.5+i)
        glVertex2f(250,-5+i)
        glVertex2f(253.5,-2.5+i)
        glVertex2f(257,0+i)
        glVertex2f(260.5,2.5+i)
        glVertex2f(264,5+i)
        glVertex2f(267.5,7.5+i)
        glVertex2f(266.5,10+i)
        glVertex2f(265.5,12.5+i)
        glVertex2f(264.5,15+i)
        glVertex2f(263.5,17.5+i)
        glVertex2f(262.5,20+i)
        glEnd()

        fumes=fumes+1
        glutSwapBuffers()
        glutPostRedisplay()
        glFlush()

def Moving_Rocket():    
    global sky_color,count,tx,ty
    count+=1
    
    for i in range(195,201):
        if(count>=50):
            glClearColor(0.0 ,0.0 ,0.0,1.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            if(sky_color==0):
                glColor3f(0, 0, 1)
                sky_color=1
            else:
                stars()
                sky_color=0
        else:
            glClearColor(0.196078  ,0.6 ,0.8,1.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if(count>=100):
            moon(20.0)	 
        if(count<=300):
            glColor3f(0.5,0.0 ,0.9)
            glBegin(GL_POLYGON)
            glVertex2f(237.5,20.0+i)
            glVertex2f(262.5,20.0+i)
            glVertex2f(262.5,120.0+i)
            glVertex2f(237.5,120.0+i)
            glEnd()
        if(count>=150):
            k = i
            glColor3f(1.0,1.0,1.0)
            glBegin(GL_POLYGON)#core
            glVertex2f(237.5,150.0+k)
            glVertex2f(252.5,150.0+k)
            glVertex2f(252.5,120.0+k)
            glVertex2f(237.5,120.0+k)
            glEnd()	
            glBegin(GL_POLYGON)
            glVertex2f(237.5,140.0+k)
            glVertex2f(230,140.0+k)
            glVertex2f(230,130.0+k)
            glVertex2f(237.5,130.0+k)
            glVertex2f(262.5,140.0+k)
            glVertex2f(227.5,140.0+k)
            glVertex2f(227.5,130.0+k)
            glVertex2f(262.5,130.0+k)
            glEnd()
        else:
            glColor3f(1.0,1.0,1.0)
            glBegin(GL_POLYGON)#front
            glVertex2f(237.5,120.0+i)
            glVertex2f(262.5,120.0+i)
            glVertex2f(250,170.0+i)
            glEnd()	
        if(count<=120):
            glColor3f(0.9,0.9,0.0)
            glBegin(GL_POLYGON)
            glVertex2f(237.5,120.0+i)
            glVertex2f(217.5,95.0+i)
            glVertex2f(237.5,95.0+i)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(237.5,20.0+i)
            glVertex2f(217.5,20.0+i)
            glVertex2f(237.5,70.0+i)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(262.5,20.0+i)
            glVertex2f(282.5,20.0+i)
            glVertex2f(262.5,70.0+i)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(262.5,120.0+i)
            glVertex2f(262.5,95.0+i)
            glVertex2f(282.5,95.0+i)
            glEnd()
        if(count<=110):
            glColor3f(0.556863 ,0.137255  ,0.419608)
            glBegin(GL_POLYGON)
            glVertex2f(237.5,20.0+i)
            glVertex2f(244.5,20.0+i)
            glVertex2f(241,0.0+i)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(246.5,20.0+i)
            glVertex2f(253.5,20.0+i)
            glVertex2f(249.5,0.0+i)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(262.5,20.0+i)
            glVertex2f(255.5,20.0+i)
            glVertex2f(258.5,0.0+i)
            glEnd()	
    glutSwapBuffers()
    glutPostRedisplay()
    glFlush()

def moon(radius):  
    global tx,ty,DEG2RAD
    glBegin(GL_POLYGON)
    for i in range(359):
        degInRad = i*DEG2RAD
        glVertex2f(300+ty+math.cos(degInRad)*radius,500-tx+(math.sin(degInRad))*radius)
    glEnd()
    tx=tx+0.1
    ty=ty+0.1

def iterate():
    glClearColor(0.196078  ,0.6 ,0.8,1.0)
    glPointSize(1.0)
    gluOrtho2D(0.0,499.0,0.0,499.0)


def Showscreen():
    global launch,sky_color,count,count1,tx,ty,fumes,DEG2RAD
    if (launch == 0):
        glClear(GL_COLOR_BUFFER_BIT)        
        glutSwapBuffers()
    else:
        control()
    for i in range(100):
        Rocket_on_Ground()
    launch = 1
    for i in range(100):
        Rocket_on_Ground()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow("rocket")
iterate()
glutDisplayFunc(Showscreen)
glutIdleFunc(Showscreen)
glutMainLoop()