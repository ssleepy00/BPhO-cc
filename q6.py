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

class pos:
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
position=pos()
fig,ax = plt.subplots(figsize=(8,6))
ax.set_xlim(-10000,10000)
ax.set_ylim(-10000,10000)
ax.grid(True)
img1 = mpimg.imread('cat.jpg')
img2 = mpimg.imread('upsidecat.jpg')
image_h = img1.shape[0]
image_w = img1.shape[1]
array2=[]
array3=[]
array2.append(position.getx() - image_w/2)
array2.append(position.getx() + image_w/2)
array2.append(position.gety() - image_h/2)
array2.append(position.gety() + image_h/2)
obj1 = ax.imshow(img1,extent=(
    array2[0],
    array2[1],
    array2[2],
    array2[3])
)
for i in range(len(array2)):
    array3.append((-f)/(array2[i]-f))
obj2 = ax.imshow(img2,extent=(
    array3[0],
    array3[1],
    array3[2],
    array3[3])
)
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
    array2=[]
    array3=[]
    array2.append(position.getx() - image_w/2)
    array2.append(position.getx() + image_w/2)
    array2.append(position.gety() - image_h/2)
    array2.append(position.gety() + image_h/2)
    obj1.set_extent((
    array2[0],
    array2[1],
    array2[2],
    array2[3]))
    for i in range(len(array2)):
        array3.append((-f)/(array2[i]-f))
    obj2.set_extent((
    array3[0],
    array3[1],
    array3[2],
    array3[3]))
    fig.canvas.draw_idle()
fig.canvas.mpl_connect('key_press_event',on_press)
plt.show()