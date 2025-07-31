import numpy as np
import matplotlib.pyplot as plt
def q4(c1,c2,x,y,L):
    return (np.sqrt(x**2 + y**2)/c1) + (np.sqrt(((L-x)**2)+y**2)/ c2)
c1=345
c2=230
L=2
y=1
xArray = []
tArray = []
for i in range(1000):
    x=i*(L/1000)
    t=q4(c1,c2,x,y,L)
    xArray.append(x)
    tArray.append(t)
    sinTheta = x / np.sqrt(x**2 + y**2)
    sinOmega = (L - x) / np.sqrt((L-x)**2 + y**2)
    if abs(sinTheta/c1 - sinOmega/c2) < 0.00001:
        plt.plot(x,t,'ro')
plt.plot(xArray,tArray)
plt.xlabel('x (m)')
plt.ylabel('Time of Flight (s)')
plt.title('Refraction')
plt.show()