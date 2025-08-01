import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pyplot as mping
image1=Image.open('cat.jpg')
array1=np.array(image1)
R=1
class position:
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
object= position()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.grid(True)

array2=[]
for i in range(len(array1)):
    for j in range(len(array1[i])):
        curr = array1[i][j]
        x=i
        y=j
        theta = np.arctan(y/np.sqrt(*R**2) -(x**2))
        m = np.tan(2*theta)
        X = -(y/x) * ((m) *np.sqrt((R**2)-(y**2) - y)/((y/x)+m))
        Y = - m * ((np.sqrt((R**2) - (y**2)) - y)/((y/x) + m))
        array2.append((X,Y,array1[i][j]))
