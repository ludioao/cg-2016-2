# exercicio 09 - star


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0
width, height = 800, 800
zoom = 1
initial_numberPoints = 5
ENTER_KEY_BTN = 13
CLOSE_KEY_BTN = 27

def keyPressed(key, x, y):
	global initial_numberPoints
	number_key = ord(key)

	if number_key == ENTER_KEY_BTN:
		if initial_numberPoints >= 20:
			return
		print "apertei enter"
		initial_numberPoints = initial_numberPoints + 1
		glFlush()
		draw_filled_star(initial_numberPoints)
	
	elif number_key == CLOSE_KEY_BTN:
		exit()
		print "fechar"



def draw_filled_star(num_points):
	degToRad = 3.14159 / 180
	glColor3f(0.0, 1.0, 0.0)
	
	glBegin(GL_TRIANGLE_FAN)
	cx, cy = 0.0, 0.0

	count = 1
	radius = 0.7
	
	glVertex2f(0.0, 0.0)
	
	for i in range( (num_points * 2) + 1 ):
		degInRad = i * 360 / (num_points * 2) * degToRad
		if count % 2 != 0:
			glVertex2d( cx + cos(degInRad) * radius, cy + sin (degInRad) * radius )
		else:
			glVertex2d( (cx + cos(degInRad) * radius / 2), ( cy + sin (degInRad) * radius / 2) )
		count = count + 1
		#i = i + 360 / (num_points * 2)

	glEnd()



def draw():                                            # ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT) # clear the screen

	#draw_star(num_points = 5)
	draw_filled_star(num_points = initial_numberPoints)
	

	glFlush()
   


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b'Demo')              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutKeyboardFunc(keyPressed)
glClearColor(0.0, 0.0, 0.0, 1.0); # Black and opaque
glutMainLoop()      
