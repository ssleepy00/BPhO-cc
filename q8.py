import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pynput import keyboard

image1=Image.open('cat.jpg')
array1=np.array(image1)
img1 = mpimg.imread('cat.jpg')
R=10000
newImage=np.zeros((100, 100, 3), dtype=np.uint8)
outW = 0
outH = 0
newX=0
newY=0

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
    def updateImg(self):
        try:    
            global newImage
            global newX
            global newY
            global outH
            global outW
            objW = len(array1)
            objL = len(array1[0])
            array2=[]
            maxX=-1e+19
            minX=1e+19
            maxY=-1e+19
            minY=1e+19
            objW = array1.shape[1]
            objL = array1.shape[0]
            for i in range(0,objW,2):
                for j in range(0,objL,2):
                    x= (object.getx() - objW/2) + i
                    y= (object.gety() - objL/2) + j
                    theta = np.arctan(y/(np.sqrt((R**2) -(x**2))))
                    m = np.tan(2*theta)
                    d = (y/x) + m
                    X =   ((m) *(np.sqrt((R**2)-(y**2)) - y)/d)
                    Y =  (y/x) * X
                    array2.append((X,Y,array1[j][i]))
                    maxX = max(X,maxX)
                    maxY = max(Y,maxY)
                    minX = min(X,minX)
                    minY = min(Y,minY)
            outW  = maxX-minX
            outH = maxY-minY
            newX= (maxX -minX) /2
            newY= (maxY - minY)/2
            draw = np.empty((round(outH),round(outW)))
            for i in range(len(array2)):
                for j in range(len(array2[i])):
                    point = array2[i][j]
                    draw[point[0],point[1]] = point
            newImage = mpimg.imshow(outH,outW,draw)
        except (ValueError,ZeroDivisionError,RuntimeWarning):
            pass


def on_press(event):
    try:
        if event.key == "w":
            object.update(0,100) 
        elif event.key == "a":
            object.update(-100,0) 
        elif event.key == "x":
            object.update(0,-100) 
        elif event.key == "d":
            object.update(100,0) 
    except AttributeError:
        if event.key == keyboard.Key.esc:
                return False
    object.updateImg()
    fig.canvas.draw_idle()

object= position()
object.updateImg()
objW = array1.shape[1]
objL = array1.shape[0]
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.grid(True)
obj1 = ax.imshow(img1,extent=(object.getx()-(objW/2),object.getx()+(objW/2),object.gety()-(objL/2),object.gety()+(objL/2)))
obj2 = ax.imshow(newImage,extent=(newX - (outW/2),newX + (outW/2),newY - (outH/2),newY + (outH/2)))
fig.canvas.mpl_connect('key_press_event',on_press)
plt.show()

         

