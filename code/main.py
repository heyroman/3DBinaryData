import os, sys
import representation as rps
import visualisation as vis

# filename = input("Enter file name: ")
filename = 'picture.jpg'
pathname = os.path.join('..', os.path.join('input_data_examples', filename))
filesize = os.path.getsize(pathname)
file = open(pathname, 'rb')
try:
    # if filesize < 4000:
    #     print("Using simple representation")
    #     data = rps.represent_simple(file, filesize)
    # else:
        print("Using advanced PCA representation")
        data = rps.represent_PCA(file, filesize)
finally:
    file.close()

vis.createPNGs(data)
# vis.visualizeIt(data)