import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pynput import keyboard

image1=Image.open('cat.jpg')
array1=np.array(image1)
img1 = mpimg.imread('cat.jpg')
R=10000
newImage=None
outW = 0
outH = 0
newX=0
newY=0

class position:
    def __init__(self,userx,usery):
        self.x=3500
        self.y=2000
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
        global newImage, newX, newY, outH, outW
        objW = array1.shape[1]
        objL = array1.shape
        array2=[]
        maxX=-1e+19
        minX=1e+19
        maxY=-1e+19
        minY=1e+19
        objW = array1.shape[1]
        objL = array1.shape[0]
        for i in range(0,objW,2):
            for j in range(0,objL,2):
                x= (self.getx() - objW/2) + i
                y= (self.gety() - objL/2) + j
                if abs(x)< R and abs(y)< R:
                    theta = np.arctan(y/(np.sqrt((R**2) -(x**2)+1e-8)))
                    m = np.tan(2*theta)
                    d = (y/x) + m
                    if abs(d) > 1e-8:
                        X =  - ((m) *(np.sqrt((R**2)-(y**2)+1e-8) - y)/d)
                        Y =  (y/x) * X
                        array2.append((X,Y,array1[j,i,:]))
                        maxX = max(X,maxX)
                        maxY = max(Y,maxY)
                        minX = min(X,minX)
                        minY = min(Y,minY)
        newX= (maxX +minX) /2
        newY= (maxY + minY)/2
        rangeX = maxX-minX
        rangeY = maxY-minY
        outW = max(1,int(np.ceil(rangeX)))
        outH = max(1,int(np.ceil(rangeY)))
        draw = np.zeros((int(np.ceil(outH)), int(np.ceil(outW)), 3), dtype=np.uint8)
        for i in range(len(array2)):
            Xv = array2[i][0]
            Yv = array2[i][1]
            colour = array2[i][2]
            col = int(((Xv-minX)/rangeX)*(outW-1))
            row = int(((Yv-minY)/rangeY)*(outH-1))
            if 0<=row<outH and 0<=col<outW:
                draw[row, col,:] = colour
        newImage = draw


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
    obj2.set_data(newImage)
    obj2.set_extent((newX - outW/2,newX + outW/2,newY - outH/2,newY + outH/2))
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
obj2 = ax.imshow(newImage,extent=(newX - (outW/2),newX + (outW/2),newY - (outH/2),newY + (outH/2)),origin="lower")
fig.canvas.mpl_connect('key_press_event',on_press)
plt.show()

         

