import MazeOpengl as M
import Player_Enemies as pe
import random
import CONSTANTS as C
import functions as f1

def reset():
    Maze = M.Maze()
    endTile = pe.endTile()
    player = pe.player()
    # pac = pac(random.randint(COLS//5,COLS), random.randint(ROWS//5,ROWS))
    pac = pe.pac(5,5)
    enemies = []
    numberOfEnemies = 1
    for i in range(numberOfEnemies):
        enemy1 = pe.enemy(random.randint(C.COLS//5,C.COLS),random.randint(C.ROWS//5,C.ROWS))
        enemies.append(enemy1)
    Win = False
    return Maze, player, pac, enemies, endTile, Win

def gameOver(Win):
    x = -100
    y = 0
    c = 40
    if Win:
        # W
        x += 50
        f1.poly([(x, y + 2 * c), (x + c // 4, y), (x + c // 2, y + 2 * c), (x + 3 * c // 4, y), (x + c, y + 2 * c)])
        # I
        x += 50
        f1.drawLine(x + c // 2, y + 2 * c, x + c // 2, y)
        # N
        x += 50
        f1.poly([(x, y), (x, y + 2 * c), (x + c, y), (x + c, y + 2 * c)])
    else:
        x = -100
        # L
        f1.poly([(x,y+2*c), (x,y), (x+c,y)])
        #O
        x += 50
        f1.poly([(x, y + 2 * c), (x, y), (x+c,y), (x+c,y+2*c)], True)
        #S
        x += 50
        f1.poly([(x,y),(x+c,y),(x+c,y+c),(x,y+c),(x,y+2*c),(x+c,y+2*c)])
        #T
        x += 50
        f1.drawLine(x,y+2*c,x+c,y+2*c)
        f1.drawLine(x+c//2,y+2*c,x+c//2,y)

    x = -50
    y = -100
    c = 15
    #P
    f1.poly([(x, y), (x, y+2*c), (x + c, y+2*c), (x+c, y+c), (x, y+c)])

    x += 20
    #R
    f1.poly([(x, y), (x, y+2*c), (x + c, y+2*c), (x+c, y+c), (x, y+c)])
    f1.drawLine(x,y+c, x+c,y)

    #E
    x += 20
    f1.poly([(x+c,y), (x,y), (x,y+2*c), (x+c,y+2*c)])
    f1.drawLine(x, y+c, x+c, y+c)

    #S
    x += 20
    f1.poly([(x, y), (x + c, y), (x + c, y + c), (x, y + c), (x, y + 2 * c), (x + c, y + 2 * c)])
    x += 20
    f1.poly([(x, y), (x + c, y), (x + c, y + c), (x, y + c), (x, y + 2 * c), (x + c, y + 2 * c)])

    # R
    x += 40
    f1.poly([(x, y), (x, y + 2 * c), (x + c, y + 2 * c), (x + c, y + c), (x, y + c)])
    f1.drawLine(x, y + c, x + c, y)