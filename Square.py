import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import threading

class Square:
    def __init__(self):
        self.angle = 0
        self.lock = threading.Lock()

    def draw(self):
        glPushMatrix()
        glRotatef(self.angle, 0, 1, 0)
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        glVertex3f(-1, 1, 0)
        glColor3f(0, 1, 0)
        glVertex3f(1, 1, 0)
        glColor3f(0, 0, 1)
        glVertex3f(1, -1, 0)
        glColor3f(1, 1, 1)
        glVertex3f(-1, -1, 0)
        glEnd()
        glPopMatrix()

    def update(self):
        while True:
            self.lock.acquire()
            self.angle += 1
            self.lock.release()
            pygame.time.wait(10)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    square = Square()

    t = threading.Thread(target=square.update)
    t.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        square.draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
