# exercicio 08


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0
width, height = 800, 800
zoom = 1

def callMatrixMode():

	#utilizado para selecionar
	#em qual modo as operacoes de matriz
	#irao ser tratadas


	#os modos utilizados sao
	#GL_projection 			==> aplica operacoes de matriz subsequente para a matriz de projecao
	#GL_texture 			==> aplica operacoes de matriz subsequente para a matriz de textura
	#GL_modelview 			==> aplica operacoes de matriz subsequente para a matriz "model-view"
	#GL_color_matrix_ext 	==> aplica operacoes de matriz subsequente para a matriz de cores

	glMatrixMode(GL_MODELVIEW) 
	glLoadIdentity() # resetar identidade

	glTranslatef(-0.5, 0.4, 0.0)
	glBegin(GL_QUADS)
	glColor3f(1.0, 0.0, 0.0)
	glVertex2f(-0.3, -0.3)
	glVertex2f(0.3, -0.3)
	glVertex2f(0.3, 0.3)
	glVertex2f(-0.3, 0.3)
	glEnd()

	glFlush()


def draw():                                            # ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT) # clear the screen

	callMatrixMode()

	glFlush()
   


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b'Demo')              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glClearColor(0.0, 0.0, 0.0, 1.0); # Black and opaque
glutMainLoop()      
