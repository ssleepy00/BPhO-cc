import numpy as numpy
import matplotlib.pyplot as plt
def q1b(frequency):
    return numpy.sqrt(1+numpy.sqrt(1/(1.731 - (0.261 * (frequency / 10e+15)**2))))
array=[]
for i in range(405,790):
    array.append(i*10e+12)
array2=[]
colour=[]
for i in range(len(array)):
    array2.append(q1b(array[i]))
    '''
    if array[i] < 480*10e+12:
        colour.append('Infra Red')
        '''
plt.plot(array,array2)
plt.title('Refractive Index of Water over Visible Range 405-790THz')
plt.xlabel('Frequency in Terahertz')
plt.ylabel('Refractive Index')
plt.show()