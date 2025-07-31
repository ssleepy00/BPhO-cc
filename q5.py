import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from pynput import keyboard
from itertools import count

image = Image.open('cat.jpg')
array = np.array(image)
newArray=array[:,::-1]
newImage = Image.fromarray(newArray)
newImage.save('sillycat.jpg')

fig,ax = plt.subplots(figsize=(8,6))
ax.set_xlim(-10000,10000)
ax.set_ylim(-10000,10000)
ax.grid = True
img1 = mpimg.imread('cat.jpg')
img2 = mpimg.imread('sillycat.jpg')
imagebox1 = OffsetImage(img1,zoom = 0.02)
imagebox2 = OffsetImage(img2,zoom = 0.02)
global x1,y1
x1 = y1 = 5000.0
ab = AnnotationBbox(imagebox1,(x1,y1),frameon=False, box_alignment=(0.5,0.5))
ac = AnnotationBbox(imagebox2,(-x1,y1),frameon=False, box_alignment=(0.5,0.5))
ax.add_artist(ab)
ax.add_artist(ac)
def on_press(key):
    try:
        if key.char == "w":
            y1 = y1 + 1
        elif key.char == "a":
            x1 = x1 - 1
        elif key.char == "s":
            y1 = y1 - 1
        elif key.char == "d":
            x1 = x1 + 1        
    except AttributeError:
        if key == keyboard.Key.esc:
                return False
def on_release(key):
    return
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
framegen = count(0)
def update_position(x,y):
    global x1 , y1
    ab.xy=(x1,y1)
    ac.xy=(-x1,y1)
    return ab,ac
ani = animation.FuncAnimation(fig,update_position(x1,y1),frames=framegen,interval=50,blit=True,cache_frame_data=False)
plt.show()