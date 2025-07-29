import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
u=[20,25,30,35,40,45,50,55]
v=[65.5,40,31,27,25,23.1,21.5,20.5]
InvU = []
InvV = []
n=len(u)
XSum=0
YSum=0
X2Sum = 0
Y2Sum = 0
XYSum = 0
for i in range(len(u)):
    x=1/u[i]
    InvU.append(x)
    XSum = XSum + x
    X2Sum = X2Sum + x**2
for i in range(len(v)):
    y=1/v[i]
    InvV.append(y)
    YSum = YSum + y
    Y2Sum = Y2Sum + y**2
for i in range(len(InvU)):
    XYSum = XYSum + (InvU[i] * InvV[i])
r = ((n*XYSum)-((XSum)*(YSum)))/np.sqrt((n*X2Sum-(XSum)**2)*(n*Y2Sum-(YSum)**2))
r2=r**2
print(": ",r2)

p = polyfit(InvU,InvV,1)
Fit=[]
for i in range(len(InvU)):
    x=(InvU[i] * p[1])+p[0]
    Fit.append(x)
plt.plot(InvU,Fit)
plt.plot(InvU,InvV)
plt.xlabel('1/u')
plt.ylabel('1/v')
plt.text(0.03,0.0475,"R^2 ="+str(r2))
s="y="+str(round(p[1],5)),"x +",str(round(p[0],5))
plt.text(0.03,0.045,s)
plt.text(0.03,0.0425,"1/f = 0.06689, therefore f = 14.95cm")
plt.show()