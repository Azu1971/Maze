WIDTH, HEIGHT = 703, 703
TILE = 50

COLS, ROWS = WIDTH//TILE, HEIGHT//TILE

MazeLine = (0,0,0)
Player = (8/255,8/255,90/255)
Enemy = (89/255,25/255,31/255)
Pac = Enemy
EndQuad = (73/255,182/255,117/255)

def setTile(tile):
    if tile < 5:
        tile = 5
    elif tile > 100:
        tile = 100
    global TILE
    TILE = tile
    global COLS, ROWS
    COLS, ROWS = WIDTH // TILE, HEIGHT // TILE