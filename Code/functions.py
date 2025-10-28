import math

import CONSTANTS as C

from OpenGL.GL import *
import numpy as np

def addvertex(x,y):
  glVertex2f(x+(C.WIDTH//2), -y+(C.HEIGHT//2))

def toZone0(x0, y0, x1, y1):
  dx = x1 - x0
  dy = y1 - y0
  abdx, abdy = abs(dx), abs(dy)
  if abdx >= abdy:
    if dx >= 0 and dy >= 0:
      zone=0
    elif dx > 0 and dy < 0:
      x0, y0, x1, y1 = x0, -y0, x1, -y1
      zone=7
    elif dx < 0 and dy > 0:
      x0, y0, x1, y1 = -x0, y0, -x1, y1
      zone=3
    else:
      x0, y0, x1, y1 = -x0, -y0, -x1, -y1
      zone=4
  else:
    if dx >= 0 and dy >= 0:
      x0, y0, x1, y1 = y0, x0, y1, x1
      zone=1
    elif dx < 0 and dy > 0:
      x0, y0, x1, y1 = -y0, x0, -y1, x1
      zone=2
    elif dx < 0 and dy < 0:
      x0, y0, x1, y1 = -y0, -x0, -y1, -x1
      zone=5
    else:
      x0, y0, x1, y1 = y0, -x0, y1, -x1
      zone=6
  return (x0, y0, x1, y1, zone)

def drawLine(x0, y0, x1, y1,convert=False, size=1, color=C.MazeLine):
  if convert:
    x0 -= C.WIDTH // 2
    y0 += C.HEIGHT // 2
    x1 -= C.WIDTH // 2
    y1 += C.HEIGHT // 2
  x0, y0, x1, y1, zone = toZone0(x0, y0, x1, y1)
  if x1<x0:
    x0, x1, y0, y1 = x1, x0, y1, y0
  x, y = x0, y0
  dx, dy = x1 - x0, y1 - y0
  d = 2*dy-dx
  while x<=x1:
    if d>0:
      d += 2*dy-2*dx
      x+=1
      y+=1
    else:
      d += 2*dy
      x += 1
    glColor3f(*color)
    glPointSize(size)
    glBegin(GL_POINTS)
    if zone==0:
      addvertex(x,y)
    elif zone==1:
      addvertex(y,x)
    elif zone==2:
      addvertex(y,-x)
    elif zone==3:
      addvertex(-x,y)
    elif zone==4:
      addvertex(-x,-y)
    elif zone==5:
      addvertex(-y,-x)
    elif zone==6:
      addvertex(-y,x)
    elif zone==7:
      addvertex(x,-y)
    glEnd()

def drawSquare(x0, y0, x1, y1, color=(1,1,0)):
  glColor3f(*color)
  glPointSize(100)
  glBegin(GL_QUADS)
  addvertex(x0, y0)
  addvertex(x0, y1)
  addvertex(x1, y1)
  addvertex(x1, y0)
  glEnd()

def eightway(x,y,xo, yo, color):
  glColor3f(*color)
  glPointSize(2)
  glBegin(GL_POINTS)
  addvertex(x+xo,y+yo)
  addvertex(x+xo,-y+yo)
  addvertex(-x+xo,-y+yo)
  addvertex(-x+xo,y+yo)

  addvertex(y+xo,x+yo)
  addvertex(-y+xo,x+yo)
  addvertex(y+xo,-x+yo)
  addvertex(-y+xo,-x+yo)
  glEnd()

def midPointCircle(xo, yo, r, color):
  d = 1-r
  x, y = 0,r
  while x<=y:
    eightway(x,y, xo, yo, color)
    if d>=0:
      d += 2*x-2*y+5
      x+=1
      y-=1
    else:
      d += 2*x+3
      x += 1

def circleShape(xo, yo,r, n, color):
  midPointCircle(xo,yo,r, color)
  d = 360/n
  for i in range(n):
    midPointCircle((r/2)*math.cos(math.radians(d*i))+xo, (r/2)*math.sin(math.radians(d*i))+yo, r/2, color)

def translate(M, xt, yt):
  T = np.array(
    [[1,0,xt],
     [0,1,yt],
     [0,0,1]]
  )
  return np.matmul(T,M)

def scale(M, scaler):
  T = np.array(
    [[scaler, 0, 0],
     [0, scaler, 0],
     [0, 0, 1]]
  )
  return np.matmul(T, M)

def rotate(M, angle):
  T = np.array(
    [[math.cos(math.radians(angle)), -math.sin(math.radians(angle)), 0],
     [math.sin(math.radians(angle)),  math.cos(math.radians(angle)), 0],
     [0,0,1]]
  )
  return np.matmul(T,M)

def rotatePlus(M, angle, x, y):
  M = translate(M, -x, -y)
  M = rotate(M, angle)
  M = translate(M, x, y)
  return M

def scalePlus(M, scaler, x, y):
  M = translate(M, -x, -y)
  M = scale(M, scaler)
  M = translate(M, x, y)
  return M

def M(x, y):
  M = [
    x,
    y,
    1
  ]
  return M

def drawPac(x, y, d):
  x0, x1, x2 = x - C.TILE//2, x, x + C.TILE//2
  y0, y1, y2 = y + C.TILE//2, y - C.TILE//2, y + C.TILE//2
  if d==0:
    pass
  elif d==1:
    x0, y0 = rotatePlus(M(x0, y0), 90, x, y)[0:2]
    x1, y1 = rotatePlus(M(x1, y1), 90, x, y)[0:2]
    x2, y2 = rotatePlus(M(x2, y2), 90, x, y)[0:2]
  elif d==2:
    x0, y0 = rotatePlus(M(x0, y0), 180, x, y)[0:2]
    x1, y1 = rotatePlus(M(x1, y1), 180, x, y)[0:2]
    x2, y2 = rotatePlus(M(x2, y2), 180, x, y)[0:2]
  else:
    x0, y0 = rotatePlus(M(x0, y0), 270, x, y)[0:2]
    x1, y1 = rotatePlus(M(x1, y1), 270, x, y)[0:2]
    x2, y2 = rotatePlus(M(x2, y2), 270, x, y)[0:2]
  drawLine(x0, y0, x1, y1,size=4, color=C.Pac)
  drawLine(x1, y1, x2, y2,size=4, color=C.Pac)

def drawEnd(x,y, pulse, color=C.EndQuad):
  x = C.TILE*x
  y = C.TILE*y
  vertices = [(x - C.TILE, y - C.TILE), (x - C.TILE, y), (x, y), (x, y - C.TILE)]
  for i in range(len(vertices)):
    if pulse:
      vertices[i] = scalePlus(M(vertices[i][0],vertices[i][1]), 0.5, x-C.TILE//2, y-C.TILE//2)[0:2]
    else:
      vertices[i] = scalePlus(M(vertices[i][0], vertices[i][1]), 0.9, x - C.TILE // 2, y - C.TILE // 2)[0:2]
  glColor3f(*color)
  glBegin(GL_QUADS)
  for vertex in vertices:
    glVertex2fv(vertex)
  glEnd()

def poly(pointArr, closed=False):
  for i in range(1,len(pointArr)):
    drawLine(pointArr[i-1][0], pointArr[i-1][1], pointArr[i][0], pointArr[i][1])
  if closed:
    drawLine(pointArr[i][0], pointArr[i][1], pointArr[0][0], pointArr[0][1])