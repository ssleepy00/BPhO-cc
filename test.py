import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image1 = Image.open('cat.jpg')
global array1
array1 = np.array(image1)
img1 = mpimg.imread('cat.jpg')
R = 1

class position:
    def __init__(self):
        self.x = 5000
        self.y = 0
        
    def update(self, Dx, Dy):
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
            self.y = self.y + Dy
            
    def getx(self):
        return self.x
        
    def gety(self):
        return self.y

def updateImg():
    objH, objW = array1.shape[0], array1.shape[1]
    left = object.getx() - objW/2
    right = object.getx() + objW/2
    bottom = object.gety() - objH/2
    top = object.gety() + objH/2
    return array1, [left, right, bottom, top]

def on_press(event):
    if event.key == "w":
        object.update(0, 100) 
    elif event.key == "a":
        object.update(-100, 0) 
    elif event.key == "x":
        object.update(0, -100) 
    elif event.key == "d":
        object.update(100, 0) 
    elif event.key == 'escape':
        plt.close(fig)
        return
    
    # Update image position on key press
    data, extent = updateImg()
    img.set_data(data)
    img.set_extent(extent)
    fig.canvas.draw_idle()

object = position()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.grid(True)

# Create initial image plot
data, extent = updateImg()
img = ax.imshow(data, extent=extent, aspect='auto', zorder=10)

# Connect keyboard event handler
fig.canvas.mpl_connect('key_press_event', on_press)
plt.show()