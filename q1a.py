import numpy as numpy
import matplotlib.pyplot as plt
def q1a(lamda):
    B1 = 1.03961212
    B2 = 0.231792344
    B3 = 1.01046945
    C1 = 0.00600069867 / 1e+12
    C2 = 0.0200179144 / 1e+12
    C3 = 103.560653 / 1e+12
    n2 = 1 + (B1 * lamda**2)/(lamda**2 - C1) + (B2 * lamda**2)/(lamda**2 - C2) + (B3 * lamda**2)/(lamda**2 - C3)
    return numpy.sqrt(n2)
array = []
for i in range(400,800,1):
    array.append(i*1e-9)
array2=[]
for i in range(len(array)):
    array2.append(q1a(array[i]))
plt.plot(array,array2)
plt.xlabel('Wavelength (m)')
plt.xlabel()
plt.show()
