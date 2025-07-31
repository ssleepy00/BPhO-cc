import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import figure
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
image = Image.open('cat.jpg')
array = np.array(image)
newArray=array[:,::-1]
newImage = Image.fromarray(newArray)
newImage.save('sillycat.jpg')

fig, ax = plt.subplots()
imagebox = OffsetImage(Image)
x = y = 0
ab=AnnotationBbox(imagebox,
                  (x,y),
                  boxcoords="data",
                  box_alignment=(0.5,0.5))
ax.imshow(image)
plt.show()