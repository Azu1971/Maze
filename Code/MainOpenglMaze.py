import functions2 as f2
import CONSTANTS as C

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

# initialize Pygame
pygame.init()

# set up the display
screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT), DOUBLEBUF|OPENGL)

# set up OpenGL
glViewport(0, 0, C.WIDTH, C.HEIGHT)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, C.WIDTH, C.HEIGHT, 0) # set up a 2D orthogonal projection matrix
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glClearColor(1, 251/255, 218/255, 1)

# game loop
clock = pygame.time.Clock()

Maze, player, pac, enemies, endTile, Win = f2.reset()
GameOver = False
while True:
    # event loop
    # print(clock.get_fps())
    for event in pygame.event.get():
        # handle window closing
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not player.canGo(Maze, 'T'):
                player.y += 1
            elif event.key == pygame.K_DOWN and not player.canGo(Maze, 'B'):
                player.y -= 1
            elif event.key == pygame.K_LEFT and not player.canGo(Maze, 'L'):
                player.x -= 1
            elif event.key == pygame.K_RIGHT and not player.canGo(Maze, 'R'):
                player.x += 1
            elif event.key == pygame.K_SPACE:
                C.Player, C.Pac, C.Enemy = C.Pac, C.Player, C.Player

            if event.key == pygame.K_r:
                Maze, player, pac, enemies, endTile, Win = f2.reset()
                GameOver=False
            if event.key == pygame.K_e:
                C.setTile(C.TILE+10)
                Maze, player, pac, enemies, endTile, Win = f2.reset()
                GameOver = False
            if event.key == pygame.K_q:
                C.setTile(C.TILE-10)
                Maze, player, pac, enemies, endTile, Win = f2.reset()
                GameOver = False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if GameOver:
        f2.gameOver(Win)
    else:
        pac.go()
        for enemy in enemies:
            enemy.go()
            enemy.pulse = not enemy.pulse
        #Draw
        player.draw()
        Maze.draw()
        pac.draw()
        endTile.draw(enemy.pulse)

        for enemy in enemies:
            enemy.draw()
        # Collision
            if enemy.collision(player):
                GameOver = True
        if pac.collision(player):
            GameOver = True
        if endTile.collision(player):
            GameOver = True
            Win = True

    pygame.display.flip()
    clock.tick(5)