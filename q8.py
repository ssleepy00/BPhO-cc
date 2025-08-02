import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpimg
from pynput import keyboard

image1=Image.open('cat.jpg')
global array1
array1=np.array(image1)
img1 = mpimg.imread('cat.jpg')
R=1

class position:
    def __init__(self):
        self.x=5000
        self.y=0
    def update(self,Dx,Dy):
            if self.x + Dx > 10000 or self.x + Dx < -10000:
                if self.x < 0:
                    self.x = -10000
                elif self.x > 0:
                    self.x = 10000
            else:
                self.x = self.x + Dx
            if self.y + Dy > 10000 or self.y + Dy < -10000:
                if self.y < 0:
                    self.y = -10000
                elif self.y > 0:
                    self.y = 10000
            else:
                self.y = self.y +Dy
    def getx(self):
            return self.x
    def gety(self):
            return self.y
    def updateImg():
        objW = len(array1)
        objL = len(array1[0])
        array2=[]
        maxX=-1e+19
        minX=1e+19
        maxY=-1e+19
        minY=1e+19
        for i in range(objW):
            for j in range(objL):
                x= (object.getx() - objW/2) + i
                y= (object.gety() - objL/2) + j
                theta = np.arctan(y/np.sqrt(R**2) -(x**2))
                m = np.tan(2*theta)
                X = -(y/x) * ((m) *(np.sqrt((R**2)-(y**2)) - y)/((y/x)+m))
                Y = - m * ((np.sqrt((R**2) - (y**2)) - y)/((y/x) + m))
                array2.append((X,Y,array1[i][j]))
                maxX = max(X,maxX)
                maxY = max(Y,maxY)
                minX = min(X,minX)
                minY = min(Y,minY)
        outW  = maxX-minX
        outH = maxY-minY
        newX= (maxX -minX) /2
        newY= (maxY - minY)/2
        draw = np.empty((outH,outW))
        for i in range(len(array2)):
            for j in range(len(array2[i])):
                point = array2[i][j]
                draw[point[0,1]] = point[2]
        #translate draw into figure, ax fig

    
def on_press(event):
    try:
        if event.key == "w":
            position.update(0,100) 
        elif event.key == "a":
            position.update(-100,0) 
        elif event.key == "x":
            position.update(0,-100) 
        elif event.key == "d":
            position.update(100,0) 
    except AttributeError:
        if event.key == keyboard.Key.esc:
                return False

object= position()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.grid(True)



         

