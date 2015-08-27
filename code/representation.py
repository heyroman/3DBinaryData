from sklearn.decomposition import PCA
from struct import unpack
import countMatchingBits
import numpy as np

# Function represent_simple takes file and file's size
# and reads the file bytewise.
# Then it packs this data into numpy array, where:
# first 3 columns are numeric represented bytes from file
# last column contains numbers of matching bits in bytes from first 3 columns of the same row

def represent_simple(file, filesize):
    n_dims = 3
    n_dots = filesize // n_dims
    data = np.zeros((n_dots, n_dims + 1))
    for i in range(n_dots):
        byteX = unpack('B', file.read(1))[0]
        byteY = unpack('B', file.read(1))[0]
        byteZ = unpack('B', file.read(1))[0]
        byteC = countMatchingBits.do(byteX, byteY, byteZ)
        data[i, :] = [byteX, byteY, byteZ, byteC]
    return data

# represent_PCA takes file and it's size and divides the file by 1000 (1000 is a number of desirable data points)
# to get the number of coordinates for each point.
# These numeric bytes are then being packed into a numpy matrix with n_dots rows and n_dims columns
# After that PCA is applied to the array reducing the number of columns to 4

def represent_PCA(file, filesize):
    n_dims = filesize // 1000
    n_dots = filesize // n_dims
    data = np.zeros((n_dots, n_dims))
    print(data.shape)
    for i in range(n_dots):
        for j in range(n_dims):
            data[i, j] = unpack('B', file.read(1))[0]
    pca = PCA(n_components=4)
    data = pca.fit_transform(data)
    print(data.shape)
    return data