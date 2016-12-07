# exercicio 11

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 900, 600                               # window size
zoom = 1


def draw():                                            # ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT) # clear the screen

	draw_maps()
	draw_house()

	glFlush()


def draw_house():
	print "desenhar uma casa aqui do mal"
	glColor3f(0.0, 0.0, 0.0) # Red

	glBegin(GL_QUADS)          # Each set of 4 vertices form a quad
	glVertex2f(0.5, 0.3)    # x, y
	glVertex2f(0.4, 0.3)
	glVertex2f(0.4, 0.2)
	glVertex2f(0.5, 0.2)
	glEnd()
   	
   	glBegin(GL_TRIANGLES)
   	glColor3f(0.7, 0.7, 0.7)
	
	glVertex2f(0.5, 0.3)
	glVertex2f(0.4, 0.3)
	glVertex2f(0.45, 0.4)
	
	glEnd()



def draw_maps():
   #Draw a Red 1x1 Square centered at origin
   glColor3f(1.0, 1.0, 1.0) # white
   glLineWidth(30.0)
  

   # rua beira mar
   glBegin(GL_LINES)
   glVertex2f(-1.0, 0.9)
   glVertex2f(1.0, 0.6)
   glEnd()

   # espaco da pequena ruazinha acima da beira mar
   glBegin(GL_LINES)
   glVertex2f(0.35, 0.70)
   glVertex2f(0.4, 1.0)
   glEnd()


   # rua verde louro
   glBegin(GL_LINES)
   glVertex2f(-1.0, 0.55)
   glVertex2f(1.0, 0.35)
   glEnd()

   # rua florao
   glBegin(GL_LINES)
   glVertex2f(-1.0, -0.4)
   glVertex2f(1.0, -1.0)
   glEnd()

   #rua acaia
   glBegin(GL_LINES)
   glVertex2f(-1.0, 0.1)
   glVertex2f(1.0, -0.4)
   glEnd()


   vertice_inicial = [0.6, -1.0]
   vertice_final = [0.8, 0.4]
   
   # loop de ruas
   for i in range(5):

   	glBegin(GL_LINES)
   	glVertex2f(vertice_inicial[0], vertice_inicial[1])
   	glVertex2f(vertice_final[0], vertice_final[1])
   	glEnd()

   	vertice_inicial[0] = vertice_inicial[0] - 0.2
   	vertice_final[0] = vertice_final[0] - 0.2
   	vertice_final[1] = vertice_final[1] + 0.015



   #rua q aquela q tem 2 quadras	
   glBegin(GL_LINES)
   glVertex2f(-0.46, 0.5)
   glVertex2f(-0.67, -1.0)
   glEnd()

   glBegin(GL_LINES)
   glVertex2f(vertice_inicial[0] + 0.07, -0.07)
   glVertex2f(vertice_final[0] - 0.05, vertice_final[1])
   glEnd()


   glBegin(GL_LINES)
   glVertex2f(-0.45, -1.0)
   glVertex2f(-0.39, -0.57)
   glEnd()


# initialization
glutInit()                                             # initialize glut

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b'Ex 11')              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glClearColor(0.8, 0.8, 0.8, 1.0); # branco fumaca
glutMainLoop()      