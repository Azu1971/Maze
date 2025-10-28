from functions import *
import CONSTANTS as C
import random

class movers:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    def draw(self, r, color):
        circleShape(-C.WIDTH // 2 + C.TILE // 2 + self.x * C.TILE,
                    C.HEIGHT // 2 - C.TILE // 2 + self.y * C.TILE,
                    r, 6, color)

class player(movers):
    def __init__(self,x=0, y=0):
        super().__init__(x,y)
    def draw(self):
        midPointCircle(-C.WIDTH // 2 + C.TILE // 2 + self.x * C.TILE, C.HEIGHT // 2 - C.TILE // 2 + self.y * C.TILE, C.TILE//3, C.Player)
        midPointCircle(-C.WIDTH // 2 + C.TILE // 2 + self.x * C.TILE, C.HEIGHT // 2 - C.TILE // 2 + self.y * C.TILE,
                       C.TILE // 4, C.Player)
        midPointCircle(-C.WIDTH // 2 + C.TILE // 2 + self.x * C.TILE, C.HEIGHT // 2 - C.TILE // 2 + self.y * C.TILE,
                       C.TILE // 5, C.Player)
    def canGo(self, Maze, direction):
        return Maze.grid_cells[self.x - self.y * C.ROWS].walls[direction]

class enemy(movers):
    def __init__(self, x, y):
        super().__init__(x, -y)
        self.pulse=True
    def draw(self):
        if self.pulse:
            super().draw(C.TILE, C.Enemy)
        else:
            super().draw(C.TILE // 2, C.Enemy)
    def go(self):
        choose = random.randint(0,4)
        if choose == 0 and -self.y < C.ROWS-1:
            self.y -= 1
        elif choose == 1 and -self.y > 0:
            self.y += 1
        elif choose == 2 and self.x > 0:
            self.x -= 1
        elif choose == 3 and self.x < C.COLS-1:
            self.x += 1
    def collision(self, player):
        if self.pulse:
            epsilon = 2
        else:
            epsilon = 1
        if (abs(player.x-self.x)<epsilon and abs(player.y-self.y)<epsilon):
            return True

class pac(movers):
    def __init__(self, x, y):
        super().__init__(x, -y)
        self.pulse=True
        self.direction = random.randint(0, 4)
    def draw(self):
        drawPac(-C.WIDTH // 2 + C.TILE // 2 + self.x * C.TILE, C.HEIGHT // 2 - C.TILE // 2 + self.y * C.TILE, self.direction)
    def go(self):
        if random.randint(0, 3) == 2:
            self.direction = random.randint(0, 4)
        if self.direction == 2 and -self.y < C.ROWS-1:
            self.y -= 1
        elif self.direction == 0 and -self.y > 0:
            self.y += 1
        elif self.direction == 1 and self.x > 0:
            self.x -= 1
        elif self.direction == 3 and self.x < C.COLS-1:
            self.x += 1
    def collision(self, player):
        epsilon = 1
        if (abs(player.x-self.x)<epsilon and abs(player.y-self.y)<epsilon):
            return True

class endTile:
    def __init__(self):
        self.x = C.COLS
        self.y = C.ROWS
    def draw(self, pulse):
        drawEnd(self.x, self.y, pulse)
    def collision(self, player):
        epsilon = 1
        if (abs(player.x - self.x) <= epsilon and abs(-player.y - self.y) <= epsilon):
            return True