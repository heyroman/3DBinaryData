__author__ = 'user'

import os
from struct import unpack
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib.pyplot as plt

dataX = []
dataY = []
dataZ = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# filename = input("Enter file name: ")
filename = 'user_guide.pdf'
pathname = os.path.join('..', os.path.join('input_data_examples', filename))
file = open(pathname, 'rb')
try:
    byteX = file.read(1)
    byteY = file.read(1)
    byteZ = file.read(1)
    while (byteX.__len__() == 1) & (byteY.__len__() == 1) & (byteZ.__len__() == 1):
        # dot = [byteX, byteY, byteZ]
        # data.append(dot)
        dataX.append(unpack('B', byteX)[0])
        dataY.append(unpack('B', byteY)[0])
        dataZ.append(unpack('B', byteZ)[0])

        byteX = file.read(1)
        byteY = file.read(1)
        byteZ = file.read(1)
finally:
    file.close()
dataX = random.sample(dataX, 1500)
dataY = random.sample(dataY, 1500)
dataZ = random.sample(dataZ, 1500)
ax.scatter(dataX, dataY, dataZ, c='r', marker='.', s=1)
plt.show()