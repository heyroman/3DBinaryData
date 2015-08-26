from sklearn.decomposition import PCA
from struct import unpack
import countMatchingBits
import numpy as np


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