import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pynput import keyboard
import matplotlib.figure as fig
image = Image.open('cat.jpg')
array = np.array(image)
newArray = np.flipud(array)
newImage = Image.fromarray(newArray)
newImage.save('upsidecat.jpg')
f = 3000
class Lens:
    def __init__(self):
        self.x=-5000
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
    def transformation(self):
        u = self.x 
        if u == f:
            if u > 0:
                return 10000
            else:
                return -10000
        else:
            return (u * f)/(u - f)
position=Lens()
fig,ax = plt.subplots(figsize=(8,6))
ax.set_xlim(-10000,10000)
ax.set_ylim(-10000,10000)
ax.grid(True)
img1 = mpimg.imread('cat.jpg')
img2 = mpimg.imread('upsidecat.jpg')
image_h = img1.shape[0]
image_w = img1.shape[1]
obj1 = ax.imshow(image,extent=(1,1,1,1))
obj2 = ax.imshow(newImage,extent=(1,1,1,1)) #sizes are gonna be different, so need to account for this through figuring out magnifications
def updateImg():
    x = position.getx()
    y = position.gety()
    projX = position.transformation()
    projY = y
    newImage_w = image_w * (projX/x)
    newImage_h = image_h * (projX/x)  #because we dont actually use projY, we scale up the image based on the magnification found through the image and object x
    obj1.set_extent(
                    (x - (image_w/2),
                    x+(image_w/2),
                    y-(image_h/2),
                    y+(image_h/2) ))
    obj2.set_extent(
         (projX - (newImage_w/2),
          projX + (newImage_w/2),
          projY - (newImage_h/2),
          projY + (newImage_h/2)))
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
    updateImg()
    fig.canvas.draw_idle()
updateImg()
fig.canvas.mpl_connect('key_press_event',on_press)
vline = ax.axvline(x=0, color='red')
plt.show()