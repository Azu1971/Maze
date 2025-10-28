from functions import *
import CONSTANTS as C

from random import choice

RES = C.WIDTH, C.HEIGHT

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'T':True, 'B':True, 'R':True, 'L':True}
        self.visited = False

    def draw(self):
        x, y = self.x * C.TILE, self.y * C.TILE
        if self.walls['T']:
            drawLine(x, -y, x + C.TILE, -y, True)
        if self.walls['B']:
            drawLine(x, -y-C.TILE, x+C.TILE, -y-C.TILE, True)
        if self.walls['R']:
            drawLine(x + C.TILE, -y, x + C.TILE, -y - C.TILE, True)
        if self.walls['L']:
            drawLine(x, -y, x, -y-C.TILE, True)

class Maze:
    def __init__(self):
        self.grid_cells = [Cell(col, row) for row in range(C.ROWS) for col in range(C.COLS)]
        self.start_cell = self.grid_cells[0]
        current_cell = self.grid_cells[0]
        stack = []

        temp = 0
        while len(stack)>0 or temp==0:
            temp += 1
            current_cell.visited = True

            next_cell = self.check_neighbors(current_cell)
            if next_cell:
                next_cell.visited = True
                stack.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif stack:
                current_cell = stack.pop()

    def draw(self):
        [cell.draw() for cell in self.grid_cells]

    def check_cell(self, x, y):
        find_index = lambda x, y: x+y*C.COLS
        if x<0 or x>C.COLS-1 or y<0 or y>C.ROWS-1:
            return False
        return self.grid_cells[find_index(x, y)]

    def check_neighbors(self, current_cell):
        neighbors = []
        top = self.check_cell(current_cell.x, current_cell.y-1)
        right = self.check_cell(current_cell.x+1, current_cell.y)
        bottom = self.check_cell(current_cell.x, current_cell.y+1)
        left = self.check_cell(current_cell.x-1,current_cell.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if left and not left.visited:
            neighbors.append(left)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        return choice(neighbors) if neighbors else False

def remove_walls(current, next):
    dx = current.x - next.x
    if dx==1:
        current.walls['L'] = False
        next.walls['R'] = False
    elif dx==-1:
        current.walls['R'] = False
        next.walls['L'] = False
    dy = current.y - next.y
    if dy==1:
        current.walls['T'] = False
        next.walls['B'] = False
    elif dy==-1:
        current.walls['B'] = False
        next.walls['T'] = False

