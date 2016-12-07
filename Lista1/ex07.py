# exercicio 07

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 800, 800                               # window size
zoom = 1

pointSize = 4.0
win = 150.0

GLUT_WHEEL_UP = 3
GLUT_WHEEL_DOWN = 4
GLUT_GL_MODELVIEW = GL_MODELVIEW


def draw_axis():
	glColor3f(1.0, 1.0, 1.0)

	#linha Y
	glBegin(GL_LINES)
	glVertex2f(0.0, -1.0)
	glVertex2f(0.0, 1.0)
	glEnd()

	#linha x
	glBegin(GL_LINES)
	glVertex2f(-1.0, 0.0)
	glVertex2f(1.0, 0.0)
	glEnd()

def mouse_callback_zoom(button, state, x, y):
	global win
	if state == GLUT_UP:
		if button == GLUT_WHEEL_UP:
			win = win - 10
			if win < 10:
				win = 0
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			gluOrtho2D(-win, win, -win, win)
			glutPostRedisplay()

		elif button == GLUT_WHEEL_DOWN:
			win = win + 10
			if win > 300:
				win = 300
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			gluOrtho2D(-win, win, -win, win)
			glutPostRedisplay()
			#print "wheel down"
		
		


def draw_triangle():
	glBegin(GL_TRIANGLES)
	glColor3f(0.0, 0.0, 1.0) #azul
	glVertex2f(0.1, -0.6)
	glVertex2f(0.7, -0.6)
	glVertex2f(0.4, -0.1)
	glEnd()

def draw_circle():

	glBegin(GL_POLYGON)
	numLinhas = 700
	
	PI = 3.141592
	raio = 0.2
	centerX, centerY = 0.0, 0.0

	glColor3f(0.0, 1.0, 0.0)
	glVertex2f(centerX, centerY)

	twicePi = 2 * PI
	for i in range(numLinhas):
		valorX = centerX + (raio * cos(i * twicePi / numLinhas))
		valorY = centerY + (raio * sin(i * twicePi / numLinhas))
		glVertex2f(valorX, valorY)

	glEnd()



def draw():     
	global GLUT_GL_MODELVIEW

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
                                       # ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT) # clear the screen
	glPointSize(pointSize)
	win = 150.0
	draw_axis()
	draw_rect()
	draw_triangle()
	draw_circle()

	glFlush()
   
def draw_rect():
   #Draw a Red 1x1 Square centered at origin
   glColor3f(1.0, 0.0, 0.0) # Red
   
   glBegin(GL_QUADS)          # Each set of 4 vertices form a quad
   glVertex2f(-0.5, 0.5)    # x, y
   glVertex2f(-0.2, 0.5)
   glVertex2f(-0.2, 0.2)
   glVertex2f(-0.5, 0.2)
   glEnd()
   

# initialization
glutInit()                                             # initialize glut

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b'Ex 07')              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glClearColor(0.0, 0.0, 0.0, 1.0); # Black and opaque
glMatrixMode(GL_PROJECTION)
glutMouseFunc(mouse_callback_zoom)
glutMainLoop()      