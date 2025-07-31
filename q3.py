import numpy as np
import matplotlib.pyplot as plt
#all using m or ms-1
y=1
n=1
L=2
def q3(x,y,n,L):
    return (np.sqrt(x**2 + y**2)/(3e+8)/n) + (np.sqrt(((L-x)**2)+y**2)/ (3e+8)/n)
xArray=[]
tArray=[]

for i in range(1000):
    xArray.append(i*(L/1000))
    tArray.append(q3(i*(L/1000),y,n,L))
plt.plot(xArray,tArray)
plt.xlabel('x (m)')
plt.title('Law Of Reflection')
plt.ylabel('Time of Flight (s)')
plt.show()