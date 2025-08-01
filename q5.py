import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pynput import keyboard
import matplotlib.figure as fig

image = Image.open('cat.jpg')
array = np.array(image)
newArray=array[:,::-1]
newImage = Image.fromarray(newArray)
newImage.save('sillycat.jpg')
class pos:
    def __init__(self):
        self.x=5000
        self.y=5000
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
img2 = mpimg.imread('sillycat.jpg')
image_h = img1.shape[0]
image_w = img1.shape[1]
obj1 = ax.imshow(img1,extent=(
    position.getx() - image_w/2,
    position.getx() + image_w/2,
    position.gety() - image_h/2,
    position.gety() + image_h/2)
)
obj2 = ax.imshow(img2,extent=(
    -position.getx() - image_w/2,
    -position.getx() + image_w/2,
    position.gety() - image_h/2,
    position.gety() + image_h/2)
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
    obj1.set_extent((
        position.getx() - image_w/2,
        position.getx() + image_w/2,
        position.gety() - image_h/2,
        position.gety() + image_h/2))
    obj2.set_extent((
        -position.getx() - image_w/2,
        -position.getx() + image_w/2,
        position.gety() - image_h/2,
        position.gety() + image_h/2))
    fig.canvas.draw_idle()
# Add vertical line at x=0 (center)
vline = ax.axvline(x=0, color='red')
fig.canvas.mpl_connect('key_press_event',on_press)
plt.show()