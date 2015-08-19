import os
from struct import unpack
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors
from countMatchingBits import *

# initializing variable that will store our data
dataX = []
dataY = []
dataZ = []
dataC = []

# reading a file from 'input_data_examples' directory
filename = input("Enter file name: ")
# filename = 'comsol_chart.txt'
pathname = os.path.join('..', os.path.join('input_data_examples', filename))
file = open(pathname, 'rb')

try:
    # reading 3 bytes..
    byteX = file.read(1)
    byteY = file.read(1)
    byteZ = file.read(1)

    # while bytes are not empty do processing and reading
    while (byteX.__len__() == 1) & (byteY.__len__() == 1) & (byteZ.__len__() == 1):
        # unpacking read bytes into decimal integers (cartesian coordinates)
        byteX = unpack('B', byteX)[0]
        byteY = unpack('B', byteY)[0]
        byteZ = unpack('B', byteZ)[0]

        # adding these integers to our storages
        dataX.append(byteX)
        dataY.append(byteY)
        dataZ.append(byteZ)
        # and the result of function of these integers as well
        dataC.append(count_matching_bits(byteX, byteY, byteZ))

        #read next 3 bytes
        byteX = file.read(1)
        byteY = file.read(1)
        byteZ = file.read(1)
finally:
    file.close()

dataX = random.sample(dataX, 1500)
dataY = random.sample(dataY, 1500)
dataZ = random.sample(dataZ, 1500)
dataC = random.sample(dataC, 1500)

# creating colormap according to present data
cm = plt.get_cmap('brg')
cNorm = matplotlib.colors.Normalize(vmin=min(dataC), vmax=max(dataC))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)

# plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', axisbg='k')
ax.w_xaxis.set_pane_color((0, 0, 0))
ax.w_yaxis.set_pane_color((0, 0, 0))
ax.w_zaxis.set_pane_color((0, 0, 0))
ax.grid(False)
ax.scatter(dataX, dataY, dataZ, c=scalarMap.to_rgba(dataC), edgecolors=scalarMap.to_rgba(dataC), marker='.', s=1)
scalarMap.set_array(dataC)
fig.colorbar(scalarMap)
plt.show()