from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.25, 0.25, 0.0)
    glVertex3f(0.75, 0.25, 0.0)
    glVertex3f(0.75, 0.75, 0.0)
    glVertex3f(0.25, 0.75, 0.0)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Program Pertama OpenGL")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(display)
    glutMainLoop()

main()
